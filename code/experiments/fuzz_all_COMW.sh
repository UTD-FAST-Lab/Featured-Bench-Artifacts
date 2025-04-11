# Evaluate all fuzzers on COMW group. 
# Expected to take 10 hours.
(cd $(pwd)/afl && bash build.sh exploit COMW 7200) &
pid1=$!

(cd $(pwd)/aflfast && bash build.sh fast COMW 7200) &
pid2=$!

(cd $(pwd)/aflplusplus && bash build.sh explore COMW 7200) &
pid3=$!

(cd $(pwd)/honggfuzz && bash build.sh COMW 7200) &
pid4=$!

(cd $(pwd)/ecofuzz && bash build.sh COMW 7200) &
pid5=$!

(cd $(pwd)/mopt && bash build.sh COMW 7200) &
pid6=$!

(cd $(pwd)/fairfuzz && bash build.sh COMW 7200) &
pid7=$!

(cd $(pwd)/tortoise-bb && bash build.sh COMW 7200) &
pid8=$!

(cd $(pwd)/tortoise-loop && bash build.sh COMW 7200) &
pid9=$!

(cd $(pwd)/memlock-heap && bash build.sh COMW 7200) &
pid10=$!

(cd $(pwd)/memlock-stack && bash build.sh COMW 7200) &
pid11=$!

(cd $(pwd)/redqueen && bash build.sh COMW 7200) &
pid12=$!

(cd $(pwd)/lafintel && bash build.sh COMW 7200) &
pid13=$!

# Wait for all processes to complete
wait $pid1
wait $pid2
wait $pid3
wait $pid4
wait $pid5
wait $pid6
wait $pid7
wait $pid8
wait $pid9
wait $pid10
wait $pid11
wait $pid12
wait $pid13

# clean all "Featured-Bench" directories
sudo find . -type d -name "Featured-Bench" -exec rm -rf {}