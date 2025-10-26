FROM ubuntu:22.04
FROM python:3.12
WORKDIR /ces

COPY ./requirements.txt /ces/requirements.txt

RUN apt-get update

COPY ./config /ces/config
COPY ./dataset /ces/dataset
COPY ./scripts /ces/scripts
COPY ./src /ces/src
COPY ./tree-sitter-python /ces/tree-sitter-python

RUN apt-get -y install graphviz graphviz-dev
RUN pip install pygraphviz

RUN pip3 install -r /ces/requirements.txt