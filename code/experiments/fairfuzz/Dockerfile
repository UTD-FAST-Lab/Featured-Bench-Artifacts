FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3-dev build-essential git wget cmake clang llvm

LABEL description="Dockerfile for FairFuzz"

RUN git clone https://github.com/carolemieux/afl-rb && \
    cd afl-rb && \
    make && make install

ENV CC=afl-gcc \
    CXX=afl-g++
