FROM python:3.12-bookworm

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /workspace/example

RUN python -m pip install --no-cache-dir foga

COPY pyproject.toml foga.yml CMakeLists.txt /workspace/example/
COPY src /workspace/example/src
COPY cpp /workspace/example/cpp
