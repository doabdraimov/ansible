FROM python:3.10.6-alpine3.16
MAINTAINER Daniiar Abdraimov (doabdraimov@gmail.com)

# ========= Instaling gcc and linux headers. Dependencies off psutil ==============
RUN apk add build-base linux-headers

WORKDIR /opt/ansible

ENV PATH="/root/.local/bin:${PATH}"

# ========= Create config dir and install ansible with dependencies ==============
RUN /bin/sh -c set -ex && \
    mkdir /opt/ansible/configs && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install ansible paramiko netmiko psutil

COPY app/. /opt/ansible/.


CMD [ "python" ]