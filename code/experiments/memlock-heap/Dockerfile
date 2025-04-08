FROM ubuntu:22.04

RUN apt update && apt install -y llvm wget git build-essential tmux cmake libtool automake autoconf autotools-dev m4 autopoint help2man bison flex texinfo zlib1g-dev libexpat1-dev libfreetype6 libfreetype6-dev sudo

ENV PATH="/MemLock/clang+llvm/bin:$PATH" LD_LIBRARY_PATH="/MemLock/clang+llvm/lib:$LD_LIBRARY_PATH"

RUN git clone https://github.com/wcventure/MemLock-Fuzz /MemLock --depth 1 &&\
    cd MemLock &&\
    sed -i 's/6.0.1/8.0.0/g' ./tool/install_llvm.sh &&\
    ./tool/install_llvm.sh &&\
    ./tool/install_MemLock.sh
WORKDIR /MemLock

ENV CC=/MemLock/tool/MemLock/memlock-heap-clang
ENV CXX=/MemLock/tool/MemLock/memlock-heap-clang++