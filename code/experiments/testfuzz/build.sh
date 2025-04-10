# Check if power schedule is provided
if [ -z "$1" ]; then
  echo "Please provide a power schedule from (fast, lin, explore, quad, exploit, coe)."
  exit 1
fi

# Check feature
if [ -z "$2" ]; then
  echo "Please choose a feature from (COMD, COMW, COMB, COMWE, LOOPI, LOOPDI, RECURI, RECURDI, MAGICD, MAGICL, MAGICS, CHECKSUMC, CHECKSUMD)."
  exit 1
fi

# Check timeout
if [ -z "$3" ]; then
  echo "Please set a timeout for fuzzing (unit: second)."
  exit 1
fi

# Build AFL++ Docker image
docker build -t testfuzz .

# Step1: System configuration
echo "" | sudo tee /proc/sys/kernel/core_pattern
echo 0 | sudo tee /proc/sys/kernel/core_uses_pid
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
echo 1 | sudo tee /proc/sys/kernel/sched_child_runs_first
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

# Step2: Compile target programs
cd testbench
for dir in */; do
    if [ -f "$dir/Makefile" ]; then
        dir="${dir%/}"
        echo "Compiling binary in $dir"
        docker run --rm -w /work -it -v "$(pwd)":/work --privileged \
            -e dir=$dir \
            -e CFLAGS='-fcoverage-mapping -fprofile-instr-generate -gline-tables-only' testfuzz \
            sh -c 'cd "$dir" && timeout 1h make'
    fi
done

# Step3: Fuzzing!
timestamp=$(date +"%Y%m%d%H%M")
for dir in */; do
    if [ -f "$dir/Makefile" ]; then
        dir="${dir%/}"
        echo "Fuzzing binary in $dir"
        echo "Fuzzing $dir with power strategy $1"
        for i in {0..19}; do
            echo "Number: $i"
            docker run --rm --privileged -it \
                -w "/work" \
                -v "$(pwd)":/work \
                -v "$(pwd)/../../results/":/results \
                -v "$(pwd)/../coverage":/scripts \
                -e dir=$dir \
                -e timestamp=$timestamp \
                -e AFL_USE_ASAN=1 \
                -e AFL_NO_AFFINITY=1 \
                -e AFL_BENCH_UNTIL_CRASH=1 \
                -e index=$i \
                -e power=$1 \
                -e feature=$2 \
                -e timeout=$3 \
                testfuzz \
                sh -c 'chmod +x /scripts/coverage.sh && \
                       mkdir -p "/results/${feature}/testfuzz_${power}/${timestamp}/${dir}/${index}" && \
                       log_file="runtime_log.txt" && \
                       results_dir="/results/${feature}/testfuzz_${power}/${timestamp}/${dir}/${index}" && \
                       command="afl-fuzz -p ${power} -i ./seeds -o $results_dir -- ./${dir}/${dir} @@" && \
                       echo "===================" >> ${results_dir}/${log_file} && \
                       echo "Command: $command" >> ${results_dir}/${log_file} && \
                       start_time=$(date +"%Y-%m-%d %H:%M:%S") && \
                       echo "Started at: ${start_time}" >> ${results_dir}/${log_file} && \
                       { timeout ${timeout}s $command; } 2>&1 | tee ${results_dir}/${log_file} && \
                       end_time=$(date +"%Y-%m-%d %H:%M:%S") && \
                       echo "Ended at: ${end_time}" >> ${results_dir}/${log_file} && \
                       start_timestamp=$(date -d "$start_time" +"%s") && \
                       end_timestamp=$(date -d "$end_time" +"%s") && \
                       duration=$((end_timestamp - start_timestamp)) && \
                       echo "Duration (seconds): ${duration}" >> ${results_dir}/${log_file} && \
                       echo "===================" >> ${results_dir}/${log_file} && \
                       echo "Command runtime has been logged to ${results_dir}/${log_file}" && \
                       echo "+++++++++++++++++++" >> ${results_dir}/${log_file} && \
                       echo "Extract coverage for ${dir}_${index}" >> ${results_dir}/${log_file} && \
                       cd ${dir} && bash /scripts/coverage.sh ${results_dir} ${dir} >> ${results_dir}/${log_file} && \
                       echo "+++++++++++++++++++" >> ${results_dir}/${log_file}'
            log_path="../../results/${2}/testfuzz_${1}/${timestamp}/${dir}/${i}/runtime_log.txt"
            if [[ -f "$log_path" ]] && grep -q "Duration (seconds):" "$log_path"; then
                duration=$(grep -oP 'Duration \(seconds\): \K[0-9]+' "$log_path")
                if [[ "$duration" -ge 7200 ]]; then
                    echo "Duration is $duration seconds, which is >= 7200. Exiting loop."
                    break
                else
                    echo "Duration is $duration seconds. Continue to next iteration."
                fi
            else
                echo "Timed out. Exiting loop."
                break
            fi                      
        done

        echo "Fuzzing completed for $dir"
    else
        echo "No Makefile found in $dir, skipping."
    fi
done

# Step4: Generate metrics & coverage report
cd .. && sudo chmod -R 777 ../results/$2/testfuzz_$1/$timestamp
python3 report.py ../results/$2/testfuzz_$1/$timestamp