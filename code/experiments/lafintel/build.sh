if [ -z "$1" ]; then
  echo "Please choose a feature from (comp, prob, location, magic, loop, memo, hard)."
  exit 1
fi

# Step0: Build Docker image
docker build -t lafintel .

# Step1: System configuration
echo "" | sudo tee /proc/sys/kernel/core_pattern
echo 0 | sudo tee /proc/sys/kernel/core_uses_pid
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
echo 1 | sudo tee /proc/sys/kernel/sched_child_runs_first
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

# Step2: Compile target programs
git clone https://github.com/UTD-FAST-Lab/Featured-Bench.git
cd Featured-Bench
git checkout v2.0-$1
for dir in */; do
    if [ -f "$dir/Makefile" ]; then
        dir="${dir%/}"
        echo "Compiling binary in $dir"
        docker run --rm -w /work -it -v "$(pwd)":/work --privileged \
            -e dir=$dir \
            -e CFLAGS='-fcoverage-mapping -fprofile-instr-generate -gline-tables-only' lafintel \
            sh -c 'cd "$dir" && timeout 1h make'
    fi
done

# Step3: Fuzzing!
timestamp=$(date +"%Y%m%d%H%M")
for dir in */; do
    if [ -f "$dir/Makefile" ]; then
        dir="${dir%/}"
        echo "Fuzzing binary in $dir"
        for i in {0..19}; do
            echo "Number: $i"
            docker run --rm --privileged -it \
                -w "/work" \
                -v "$(pwd)":/work \
                -v "/data/miao/featured_bench/results/":/results \
                -v "/home/miao/Featured-Bench-Experiments/lafintel/coverage":/scripts \
                -e dir=$dir \
                -e timestamp=$timestamp \
                -e AFL_USE_ASAN=1 \
                -e AFL_NO_AFFINITY=1 \
                -e AFL_BENCH_UNTIL_CRASH=1 \
                -e index=$i \
                -e feature=$1 \
                lafintel \
                sh -c 'mkdir -p "/results/${feature}/lafintel/${timestamp}/${dir}/${index}" && \
                       log_file="runtime_log.txt" && \
                       results_dir="/results/${feature}/lafintel/${timestamp}/${dir}/${index}" && \
                       command="afl-fuzz -i ./seeds -o $results_dir -- ./${dir}/${dir} @@" && \
                       echo "===================" >> ${results_dir}/${log_file} && \
                       echo "Command: $command" >> ${results_dir}/${log_file} && \
                       start_time=$(date +"%Y-%m-%d %H:%M:%S") && \
                       echo "Started at: ${start_time}" >> ${results_dir}/${log_file} && \
                       { timeout 2h $command; } 2>> ${results_dir}/${log_file} && \
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

            log_path="../../results/${1}/lafintel/${timestamp}/${dir}/${i}/runtime_log.txt"
            if [[ -f "$log_path" ]] && grep -q "Duration (seconds):" "$log_path"; then
                echo "Continue to next iteration."
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
cd .. && python3 report.py ../results/$1/lafintel/$timestamp
