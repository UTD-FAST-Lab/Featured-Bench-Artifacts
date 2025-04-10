import os
import re
import shutil
import argparse

def replace_program_in_c_file(program, input, output):
    FUNC_path = 'template_num/FUNC.c'
    if os.path.exists(FUNC_path):
        with open(FUNC_path, 'r') as FUNC_file:
            FUNC_content = FUNC_file.read()
    FUNC_path = 'template_num/FUNC.c'
    if os.path.exists(FUNC_path):
        with open(f'{input}/{program}', 'r') as program_file:
            program_content = program_file.read()

    func_name = os.path.splitext(program)[0]

    updated_FUNC_content = FUNC_content.replace('// INSERT PROGRAM HERE', program_content)
    updated_FUNC_content = updated_FUNC_content.replace('FUNC', func_name)
    # print(updated_FUNC_content)
    
    output_dir = os.path.join(output, func_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, program)  
    
    with open(output_file_path, 'w') as output_file:
        output_file.write(updated_FUNC_content)

    makefile_path = 'template_num/Makefile'
    if os.path.exists(makefile_path):
        with open(makefile_path, 'r') as makefile:
            makefile_content = makefile.read()
        updated_makefile_content = makefile_content.replace('FUNC', func_name)
        with open(os.path.join(output_dir, 'Makefile'), 'w') as makefile:
            makefile.write(updated_makefile_content)
            
    header_file_path = 'template_num/getHash.h'
    if os.path.exists(header_file_path):
        shutil.copy(header_file_path, os.path.join(output_dir, 'getHash.h'))
        
    body_file_path = 'template_num/getHash.c'
    if os.path.exists(body_file_path):
        with open(body_file_path, 'r') as body_file:
            body_file_content = body_file.read()
        wmatch = re.search(r'W(\d+)', func_name)
        dmatch = re.search(r'D(\d+)', func_name)
        if not wmatch or not dmatch:
            updated_body_file_content = body_file_content.replace('return hash % (int)pow(2222, 9999);', 'return hash % 65536;')
        else:
            updated_body_file_content = body_file_content.replace('2222', wmatch.group(1))
            updated_body_file_content = updated_body_file_content.replace('9999', dmatch.group(1))
        with open(os.path.join(output_dir, 'getHash.c'), 'w') as body_file:
            body_file.write(updated_body_file_content)
        
    
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description="Generate C benchmark")
    parser.add_argument("input", help="Input location")
    parser.add_argument("--out", help="Output location")
    args = parser.parse_args()
    
    for filename in os.listdir(args.input):
        if filename.endswith('.c'):
            replace_program_in_c_file(filename, args.input, args.out)
            print(f'Genrated benchmark {filename}...')
