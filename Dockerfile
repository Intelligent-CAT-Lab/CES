FROM python:3.9
WORKDIR /ces

COPY ./requirements.txt /ces/requirements.txt

RUN apt-get update
RUN apt-get -y install graphviz graphviz-dev
RUN pip install pygraphviz

RUN pip3 install -r /re2bench/requirements.txt