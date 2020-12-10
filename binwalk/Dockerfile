FROM ubuntu:bionic
ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
RUN sed -ie 's/archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list

# install binwalk
RUN apt-get update
RUN apt-get install -y git python3 python3-pip mtd-utils gzip bzip2 tar arj lhasa p7zip p7zip-full cabextract cramfsswap squashfs-tools sleuthkit default-jdk lzop srecord
RUN git clone https://github.com/ReFirmLabs/binwalk /binwalk; \
    cd /binwalk; \
    ./deps.sh --yes; \ 
    python3 ./setup.py build; \ 
    python3 ./setup.py install

COPY ./app.py /app/app.py
WORKDIR /app
RUN pip3 install flask
ENTRYPOINT ["python3"]
