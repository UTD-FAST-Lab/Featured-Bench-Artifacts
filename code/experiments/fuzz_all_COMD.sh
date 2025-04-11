# Evaluate all fuzzers on COMD group. 
# Expected to take 10 hours.
bash afl/build.sh exploit COMD 7200 &
bash aflfast/build.sh fast COMD 7200 &
bash aflplusplus/build.sh explore COMD 7200 &
bash honggfuzz/build.sh COMD 7200 &
bash ecofuzz/build.sh COMD 7200 &
bash mopt/build.sh COMD 7200 &
bash fairfuzz/build.sh COMD 7200 &
bash tortoise-bb/build.sh COMD 7200 &
bash tortoise-loop/build.sh COMD 7200 &
bash memlock-heap/build.sh COMD 7200 &
bash memlock-stack/build.sh COMD 7200 &
bash redqueen/build.sh COMD 7200 &
bash laf-intel/build.sh COMD 7200 &