FROM python:3.8.3-alpine 
#FROM alpine:edge
# zmap install 
LABEL maintainer "ilya@ilyaglotov.com"

# set work directory
#WORKDIR /usr/src/app
#
## set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## apk install 
RUN apk update \
  && apk add libcap \
             gmp-dev \
             json-c-dev \
             libpcap \ 
             libunistring-dev \
             postgresql-dev \
             gcc \
             python3-dev \
             musl-dev \
  && apk add --virtual .deps \
                        build-base \
                        byacc \
                        cmake \
                        flex \
                        gengetopt \
                        git \
                        libpcap-dev \
                        linux-headers \
                        \
  && ln -s /usr/bin/yacc /usr/bin/byacc \
  && git clone --branch=master \
               --depth=1 \
               https://github.com/zmap/zmap.git \
               \
  && cd zmap \
  && cmake . \
  && make -j4 \
  && make install \
  \
  && apk del .deps \
  && rm -rf /zmap /var/cache/apk/*



#RUN adduser -D zmap \
#  && setcap cap_net_raw=eip /usr/local/sbin/zmap
RUN pip3 install --upgrade pip
RUN pip3 install requests
RUN pip3 install psycopg2

COPY . /scanner
RUN pip3 install -r /scanner/requirements.txt
RUN pip3 install netaddr
RUN pip install geoip2 
RUN pip3 install pycvesearch

USER root
#ENTRYPOINT ["/usr/local/sbin/zmap"]