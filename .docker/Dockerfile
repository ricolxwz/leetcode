FROM python:3.12.1-alpine3.19
LABEL maintainer="wenzexu"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY ./requirements.txt /tmp/requirements.txt
RUN apk update && \
    apk add --no-cache git && \
    git config --global user.name "wenzexu" && \
    git config --global user.email "ricol.xwz@outlook.com" && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt && \
    adduser --disabled-password wenzexu
USER wenzexu