FROM python:3.12.1-alpine3.19
LABEL maintainer="wenzexu"
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        wenzexu
USER wenzexu