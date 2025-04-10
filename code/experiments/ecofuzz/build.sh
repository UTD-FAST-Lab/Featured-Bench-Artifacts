# Check feature
if [ -z "$1" ]; then
  echo "Please choose a feature from (COMD, COMW, COMB, COMWE, LOOPI, LOOPDI, RECURI, RECURDI, MAGICD, MAGICL, MAGICS, CHECKSUMC, CHECKSUMD)."
  exit 1
fi

# Check timeout
if [ -z "$2" ]; then
  echo "Please set a timeout for fuzzing (unit: second)."
  exit 1
fi

# build EcoFuzz docker image 
docker build -t ecofuzz .

# Step1: System configuration
echo "" | sudo tee /proc/sys/kernel/core_pattern
echo 0 | sudo tee /proc/sys/kernel/core_uses_pid
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
echo 1 | sudo tee /proc/sys/kernel/sched_child_runs_first
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

# Step2: Compile target programs
mkdir Featured-Bench
cp -r ../../../FeatureBench/$1/* Featured-Bench
cd Featured-Bench
for dir in */; do
    if [ -f "$dir/Makefile" ]; then
        dir="${dir%/}"
        echo "Compiling binary in $dir"
        docker run --rm --privileged -it -w /work -v "$(pwd)":/work -e dir=$dir ecofuzz \
            sh -c 'cd "$dir" && timeout 1h make; \
                   mv ${dir%/} "${dir%/}_bin";'
    fi
done

# Step3: Running Static module
for dir in */; do
    if [ -f "$dir/Makefile" ]; then
        dir="${dir%/}"
        docker run --rm --privileged -it -w /work -v "$(pwd)":/work -e dir=$dir ecofuzz \
            sh -c '/EcoFuzz/static_module.sh "./$dir/${dir}_bin" "./$dir/${dir}_dict";'
    fi
done

# Compile target for coverage collection
for dir in */; do
    if [ -f "$dir/Makefile" ]; then
        dir="${dir%/}"
        echo "Compiling binary cov in $dir"
        docker run --rm --privileged -it -w /work -v "$(pwd)":/work -e dir=$dir \
            -e CFLAGS='-fcoverage-mapping -fprofile-instr-generate -gline-tables-only' \
            -e CC=/EcoFuzz/afl-clang \
            -e CXX=/EcoFuzz/afl-clang++ ecofuzz \
            sh -c 'cd "$dir" && timeout 1h make; \
                   mv ${dir%/} "${dir%/}_cov";'
    fi
done

# Step4: Fuzzing!
timestamp=$(date +"%Y%m%d%H%M")
for dir in */; do
    if [ -f "$dir/Makefile" ]; then
        dir="${dir%/}"
        dicname="${dir}/${dir}_dict"
        echo "Fuzzing binary in $dir"
        echo "Fuzzing $dir with dictionary $dicname"

        for i in {0..19}; do
            echo "Number: $i"
            docker run --rm --privileged -it \
            -w "/work" \
            -v "$(pwd)":/work \
            -v "$(pwd)/../../results/":/results \
            -v "$(pwd)/../coverage":/scripts \
            -e dir=$dir \
            -e dicname=$dicname \
            -e timestamp=$timestamp \
            -e feature=$1 \
            -e timeout=$2 \
            -e AFL_USE_ASAN=1 \
            -e AFL_NO_AFFINITY=1 \
            -e AFL_BENCH_UNTIL_CRASH=1 \
            -e index=$i \
            ecofuzz \
            sh -c 'chmod +x /scripts/coverage.sh && \
                   mkdir -p "/results/${feature}/ecofuzz/${timestamp}/${dir}/${index}" && \
                   log_file="runtime_log.txt" && \
                   results_dir="/results/${feature}/ecofuzz/${timestamp}/${dir}/${index}" && \
                   command="afl-fuzz -x $dicname -i ./seeds -o $results_dir -- ./${dir}/${dir}_bin @@" && \
                   echo "===================" >> ${results_dir}/${log_file} && \
                   echo "Command: $command" >> ${results_dir}/${log_file} && \
                   start_time=$(date +"%Y-%m-%d %H:%M:%S") && \
                   echo "Started at: ${start_time}" >> ${results_dir}/${log_file} && \

                   { timeout ${timeout}s $command; } 2>> ${results_dir}/${log_file} && \
                   
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

            log_path="../../results/${1}/ecofuzz/${timestamp}/${dir}/${i}/runtime_log.txt"
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

# Step5: Generate metrics & coverage report
cd .. && sudo chmod -R 777 ../results/$1/ecofuzz/$timestamp
python3 report.py ../results/$1/ecofuzz/$timestamp