FROM ubuntu:20.04

ENV TERM=xterm
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    libopencv-dev \
    python3-opencv \
    python3-pip \
    cmake 
    # && apt-get clean \
    # && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /app
ADD . /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

EXPOSE 5001