FROM python:3.12.1-alpine3.19
LABEL maintainer="wenzexu"
ARG USERNAME=wenzexu
ARG GROUPNAME=devusers
ARG USER_UID=1001
ARG USER_GID=$USER_UID
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt && \
    addgroup -g $USER_GID $GROUPNAME && \
    adduser -u $USER_UID -G $GROUPNAME -D $USERNAME
USER $USERNAME
