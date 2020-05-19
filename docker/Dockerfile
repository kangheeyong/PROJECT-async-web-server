from ubuntu:18.04
MAINTAINER cagojeiger@naver.com

ENV LC_ALL C.UTF-8

RUN apt-get update -y
RUN apt-get install git \
                    vim -y

RUN apt-get install python3-pip -y
RUN pip3 install sanic

RUN git clone https://github.com/kangheeyong/PROJECT-async-web-server.git /root/PROJECT-async-web-server


EXPOSE 8080
WORKDIR /root/PROJECT-async-web-server
CMD ["make", "run"]


