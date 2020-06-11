from python:3.7-slim
MAINTAINER cagojeiger@naver.com

ENV LC_ALL C.UTF-8

ADD requirements.txt ./
RUN pip3 install -r requirements.txt

ADD /src /app

WORKDIR /app
CMD ["python3", "app.py"]


