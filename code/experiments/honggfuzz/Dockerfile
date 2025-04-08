FROM ubuntu:22.04

LABEL description="Dockerfile for honggfuzz"

RUN apt update && apt install -y git binutils-dev build-essential libunwind-dev libblocksruntime-dev clang unzip wget llvm

RUN git clone https://github.com/google/honggfuzz.git &&\
    cd honggfuzz && git checkout master &&\
    make && cp /honggfuzz/honggfuzz /bin

WORKDIR /honggfuzz

ENV CC=/honggfuzz/hfuzz_cc/hfuzz-clang CXX=/honggfuzz/hfuzz_cc/hfuzz-clang++
