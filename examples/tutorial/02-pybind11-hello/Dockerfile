FROM python:3.12-bookworm

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /workspace/example

RUN python -m pip install --no-cache-dir foga

COPY pyproject.toml foga.yml CMakeLists.txt /workspace/example/
COPY container-welcome.txt /workspace/example/container-welcome.txt
COPY src /workspace/example/src
COPY cpp /workspace/example/cpp

RUN printf '\nif [ -z "${FOGA_TUTORIAL_WELCOME_SHOWN:-}" ]; then\n  export FOGA_TUTORIAL_WELCOME_SHOWN=1\n  cat /workspace/example/container-welcome.txt\nfi\n' >> /root/.bashrc
