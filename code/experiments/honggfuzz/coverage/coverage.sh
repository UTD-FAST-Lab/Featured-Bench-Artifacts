seed_dir=$1/queue

mkdir -p $1/profraw
profraw_dir=$1/profraw

mkdir -p $1/lcov
lcov_dir=$1/lcov

counter=0

# Collect coverage over time.
# find "$seed_dir" -type f | sort -n | while read -r file; do
#     echo "Processing file: $file"
#     filename=$(basename "$file")
#     export LLVM_PROFILE_FILE="$filename.profraw"
#     echo "LLVM_PROFILE_FILE: $LLVM_PROFILE_FILE"
#     ./$2 $file
#     mv $LLVM_PROFILE_FILE $profraw_dir
#     llvm-profdata merge -sparse -output=fuzzer.profdata $profraw_dir/*.profraw
#     llvm-cov export -instr-profile=fuzzer.profdata ./$2 -format=text > "id:$(printf '%010d' $counter):$filename.json"
#     mv "id:$(printf '%010d' $counter):$filename.json" $lcov_dir
#     ((counter++))
# done

# Collect final coverage.
find "$seed_dir" -type f | sort -n | while read -r file; do
    echo "Processing file: $file"
    filename=$(basename "$file")
    export LLVM_PROFILE_FILE="$filename.profraw"
    echo "LLVM_PROFILE_FILE: $LLVM_PROFILE_FILE"
    ./$2 $file
    mv $LLVM_PROFILE_FILE $profraw_dir
done
llvm-profdata merge -sparse -output=fuzzer.profdata $profraw_dir/*.profraw
llvm-cov export -instr-profile=fuzzer.profdata ./$2 -format=text > coverage.json
mv coverage.json $lcov_dir