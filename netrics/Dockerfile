# FROM python:3.10 as builder 
FROM python:3.10-slim
RUN apt-get update && apt-get install -y curl iputils-ping git scamper dnsutils vim gcc jc jq && apt-get clean autoclean
RUN curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | /bin/bash
RUN apt-get install -y speedtest 


RUN pip install --upgrade pip && pip install --no-cache-dir netrics-measurements

COPY defaults.toml measurements.toml /root/.config/netrics/
COPY ookla /usr/local/bin/netrics-speed
COPY latencyload /usr/local/bin/netrics-latencyload
COPY bashping /usr/local/bin/netrics-bashping
