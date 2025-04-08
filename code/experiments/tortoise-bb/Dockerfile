FROM ubuntu:22.04

LABEL description="Dockerfile for tortoise-bb"

RUN apt-get update && \
    apt-get install -y python3-dev build-essential git wget cmake xz-utils

RUN wget https://releases.llvm.org/6.0.0/llvm-6.0.0.src.tar.xz && wget https://releases.llvm.org/6.0.0/cfe-6.0.0.src.tar.xz
RUN tar --no-same-owner -xvf llvm-6.0.0.src.tar.xz && mv llvm-6.0.0.src llvm && tar --no-same-owner -xvf cfe-6.0.0.src.tar.xz && mv cfe-6.0.0.src llvm/tools/clang
    
RUN wget https://releases.llvm.org/6.0.0/clang+llvm-6.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz
RUN tar -xf clang+llvm-6.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz && mv clang+llvm-6.0.0-x86_64-linux-gnu-ubuntu-16.04 llvm1
RUN mkdir build
RUN cd build && cmake -G "Unix Makefiles" -DLLVM_ENABLE_ASSERTIONS=On -DCMAKE_BUILD_TYPE=Release ../llvm && make -j16

RUN cd /build && make install
ENV PATH=/build/bin/:$PATH
RUN mkdir -p /build/lib/clang/6.0.0/lib/linux/
RUN cp /llvm1/lib/clang/6.0.0/lib/linux/libclang_rt.profile-x86_64.a /build/lib/clang/6.0.0/lib/linux/

RUN git clone https://github.com/TortoiseFuzz/TortoiseFuzz.git 
WORKDIR /TortoiseFuzz
RUN make

ENV CC=/TortoiseFuzz/bb_metric/afl-clang-fast
ENV CXX=/TortoiseFuzz/bb_metric/afl-clang-fast++

