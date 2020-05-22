from ubuntu:18.04
MAINTAINER cagojeiger@naver.com

ENV LC_ALL C.UTF-8

RUN apt-get update -y
RUN apt-get install git \
                    vim -y

RUN apt-get install python3-pip -y
RUN pip3 install sanic pytest aiocache

RUN git clone https://github.com/kangheeyong/PROJECT-async-web-server.git /root/PROJECT-async-web-server
RUN cd /root/PROJECT-async-web-server && git pull

ARG DEV="no"
RUN if [ "$DEV" = "yes" ]; then\
        cd /root/PROJECT-async-web-server && git checkout dev;\
    fi

EXPOSE 8080
WORKDIR /root/PROJECT-async-web-server
CMD ["make", "run"]


