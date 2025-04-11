FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3-dev build-essential git wget cmake clang llvm

LABEL description="Dockerfile for AFLFast"

RUN git clone https://github.com/mboehme/aflfast && \
    cd aflfast && \
    make && make install

ENV CC=afl-gcc \
    CXX=afl-g++
