#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGE_NAME="foga-tutorial-pybind11-profiles"

echo "Building ${IMAGE_NAME} from ${SCRIPT_DIR} without Docker cache..."
docker build --no-cache -t "${IMAGE_NAME}" "${SCRIPT_DIR}"

echo "Starting interactive container. You will land in /workspace/example."
exec docker run --rm -it "${IMAGE_NAME}" bash
