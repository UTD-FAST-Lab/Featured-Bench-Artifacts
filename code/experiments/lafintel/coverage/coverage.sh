seed_dir=$1/default/queue

mkdir -p $1/default/profraw
profraw_dir=$1/default/profraw

mkdir -p $1/default/lcov
lcov_dir=$1/default/lcov

# Collect coverage over time.
# find $seed_dir -type f ! -path "*/.state/*" | sort | while read -r file; do
#     echo "Processing file: $file"
#     filename=$(basename "$file")
#     export LLVM_PROFILE_FILE="$filename.profraw"
#     echo "LLVM_PROFILE_FILE: $LLVM_PROFILE_FILE"
#     ./$2 $file
#     mv $LLVM_PROFILE_FILE $profraw_dir
#     llvm-profdata merge -sparse -output=fuzzer.profdata $profraw_dir/*.profraw
#     llvm-cov export -instr-profile=fuzzer.profdata ./$2 -format=text > $filename.json
#     mv $filename.json $lcov_dir
# done

# Collect final coverage.
find $seed_dir -type f ! -path "*/.state/*" | sort | while read -r file; do
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