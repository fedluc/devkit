FROM python:3.12-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    UV_LINK_MODE=copy \
    VIRTUAL_ENV=/workspace/example/.venv \
    PATH=/workspace/example/.venv/bin:${PATH}

WORKDIR /workspace/example

RUN python -m pip install --no-cache-dir uv

COPY pyproject.toml foga.yml /workspace/example/
COPY src /workspace/example/src
COPY cpp /workspace/example/cpp

RUN uv sync \
    && uv run python -m build --version >/dev/null \
    && printf '\nsource /workspace/example/.venv/bin/activate\n' >> /root/.bashrc

RUN uv run foga --config foga.yml install --target system \
    && cmake --version >/dev/null \
    && ninja --version >/dev/null
