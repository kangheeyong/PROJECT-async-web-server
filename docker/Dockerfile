from python:3.7-slim
MAINTAINER cagojeiger@naver.com

ENV LC_ALL C.UTF-8

ADD requirements.txt ./

RUN pip3 install -r requirements.txt

ADD /src ./src
ADD /tests ./tests

WORKDIR ./


