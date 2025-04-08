import os
import argparse
import csv
import glob
import json


def extract_execs_done(fuzzer_stats_path):
    cycles_done = None
    execs_done = None
    paths_total = None
    paths_found = None
    bitmap_cvg = None
    unique_crashes = None
  
    with open(fuzzer_stats_path, 'r') as file:
        for line in file:
            if line.startswith('cycles_done'):
                cycles_done = line.split(':')[1].strip()

            if line.startswith('execs_done'):
                execs_done = line.split(':')[1].strip()

            if line.startswith('paths_total'):
                    paths_total = line.split(':')[1].strip()

            if line.startswith('paths_found'):
                paths_found = line.split(':')[1].strip()

            if line.startswith('bitmap_cvg'):
                bitmap_cvg = line.split(':')[1].strip()

            if line.startswith('unique_crashes'):
                unique_crashes = line.split(':')[1].strip()

    return (cycles_done, execs_done, paths_total, paths_found, bitmap_cvg, unique_crashes)

def extract_duration(runtime_log_path):
    with open(runtime_log_path, 'r') as file:
        for line in file:
            if 'Duration (seconds):' in line:
                return line.split(':')[-1].strip()
    return None

def extract_coverage(lcov_path):
    region_rate = None
    region_cov = None
    region_tol = None
    line_rate = None
    line_cov = None
    line_tol = None
    function_rate = None
    function_cov = None
    function_tol = None
    
    with open(lcov_path, 'r') as f:
        try:
            data = json.load(f)
            region_rate = data['data'][0]['totals']['regions']['percent']
            region_cov = data['data'][0]['totals']['regions']['covered']
            region_tol = data['data'][0]['totals']['regions']['count']
            line_rate = data['data'][0]['totals']['lines']['percent']
            line_cov = data['data'][0]['totals']['lines']['covered']
            line_tol = data['data'][0]['totals']['lines']['count']
            function_rate = data['data'][0]['totals']['functions']['percent']
            function_cov = data['data'][0]['totals']['functions']['covered']
            function_tol = data['data'][0]['totals']['functions']['count']
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON from {lcov_path}: {e}")
    
    return (region_rate, region_cov, region_tol, line_rate, line_cov, line_tol, function_rate, function_cov, function_tol)

def extract_metrics_for_all(base_dir):
    results = []

    for root, dirs, _ in os.walk(base_dir):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            
            fuzzer_stats_path = os.path.join(folder_path, 'fuzzer_stats')
            runtime_log_path = os.path.join(folder_path, 'runtime_log.txt')
            
            lcovdir_path = os.path.join(folder_path, 'lcov')
            lcov_jsons = glob.glob(os.path.join(lcovdir_path, "*.json"))
            lcov_path = None if not lcov_jsons else max(lcov_jsons, key=os.path.getmtime)

            cycles_done = None
            execs_done = None
            paths_total = None
            paths_found = None
            bitmap_cvg = None
            unique_crashes = None
            duration = None
            region_rate = None
            region_cov = None
            region_tol = None
            line_rate = None
            line_cov = None
            line_tol = None
            function_rate = None
            function_cov = None
            function_tol = None
            
            if os.path.exists(fuzzer_stats_path):
                cycles_done, execs_done, paths_total, paths_found, bitmap_cvg, unique_crashes = extract_execs_done(fuzzer_stats_path)

            if os.path.exists(runtime_log_path):
                duration = extract_duration(runtime_log_path)
                
            if lcov_path and os.path.exists(lcov_path):
                region_rate, region_cov, region_tol, line_rate, line_cov, line_tol, function_rate, function_cov, function_tol = extract_coverage(lcov_path)

            if unique_crashes is not None and unique_crashes != '0':
                results.append({
                        'fuzzer': folder_path.split('/')[3],
                        'program': folder_path.split('/')[5],
                        'cycles': -1 if cycles_done is None else cycles_done,
                        'execs': -1 if execs_done is None else execs_done,
                        'paths_total': -1 if paths_total is None else paths_total,
                        'paths_found': -1 if paths_found is None else paths_found,
                        'total_edges': -1,
                        'edges_found': -1,
                        'bitmap_cvg': -1 if bitmap_cvg is None else bitmap_cvg,
                        'crashes': -1 if unique_crashes is None else unique_crashes,
                        'duration': -1 if duration is None else duration,
                        'region_rate': -1 if region_rate is None else region_rate,
                        'region_cov': -1 if region_cov is None else region_cov,
                        'region_tol': -1 if region_tol is None else region_tol,
                        'line_rate': -1 if line_rate is None else line_rate,
                        'line_cov': -1 if line_cov is None else line_cov,
                        'line_tol': -1 if line_tol is None else line_tol,
                        'branch_rate': -1,
                        'branch_cov': -1,
                        'branch_tol': -1,
                        'function_rate': -1 if function_rate is None else function_rate,
                        'function_cov': -1 if function_cov is None else function_cov,
                        'function_tol': -1 if function_tol is None else function_tol
                })
    return results

def extract_coverage_for_all(base_dir):
    results = []

    for root, dirs, _ in os.walk(base_dir):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            lcovdir_path = os.path.join(folder_path, 'lcov')
                
            if os.path.exists(lcovdir_path):
                for lcov in glob.glob(os.path.join(lcovdir_path, "*.json")):
                    region_rate = None
                    region_cov = None
                    region_tol = None
                    line_rate = None
                    line_cov = None
                    line_tol = None
                    function_rate = None
                    function_cov = None
                    function_tol = None
                    region_rate, region_cov, region_tol, line_rate, line_cov, line_tol, function_rate, function_cov, function_tol = extract_coverage(lcov)
                    results.append({
                            'fuzzer': lcov.split('/')[3],
                            'program': lcov.split('/')[5],
                            'iteration': lcov.split('/')[6],
                            'seed': lcov.split('/')[8].replace('.json', ''),
                            'region_rate': -1 if region_rate is None else region_rate,
                            'region_cov': -1 if region_cov is None else region_cov,
                            'region_tol': -1 if region_tol is None else region_tol,
                            'line_rate': -1 if line_rate is None else line_rate,
                            'line_cov': -1 if line_cov is None else line_cov,
                            'line_tol': -1 if line_tol is None else line_tol,
                            'branch_rate': -1,
                            'branch_cov': -1,
                            'branch_tol': -1,
                            'function_rate': -1 if function_rate is None else function_rate,
                            'function_cov': -1 if function_cov is None else function_cov,
                            'function_tol': -1 if function_tol is None else function_tol
                    })
    return results

def generate_metrics_csv(base_dir):
    results = extract_metrics_for_all(base_dir)
    
    headers = results[0].keys()
    values = [result.values() for result in results]
    
    feature = base_dir.split('/')[2]
    fuzzer = base_dir.split('/')[3]
    timestamp = base_dir.split('/')[4]

    csv_dir_path = f'../reports/csvs/{feature.upper()}/{timestamp[:8]}/metrics'
    os.makedirs(csv_dir_path, exist_ok=True)
    csv_path = f'{csv_dir_path}/{fuzzer}.csv'
    print(f'metrics report is generated at {csv_path}...')
    with open(csv_path, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(values)
        
def generate_coverage_csv(base_dir):
    results = extract_coverage_for_all(base_dir)
        
    headers = results[0].keys()
    values = [result.values() for result in results]
    
    feature = base_dir.split('/')[2]
    fuzzer = base_dir.split('/')[3]
    timestamp = base_dir.split('/')[4]

    csv_dir_path = f'../reports/csvs/{feature.upper()}/{timestamp[:8]}/coverage'
    os.makedirs(csv_dir_path, exist_ok=True)
    csv_path = f'{csv_dir_path}/{fuzzer}.csv'
    print(f'coverage report is generated at {csv_path}...')
    with open(csv_path, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(values)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('results', type=str)

    args = parser.parse_args()
    generate_metrics_csv(args.results)
    generate_coverage_csv(args.results)