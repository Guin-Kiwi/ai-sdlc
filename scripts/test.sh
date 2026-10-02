#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

bash scripts/check-lifecycle.sh
bash scripts/test-lifecycle.sh
python3 -m unittest discover -s scripts/tests -q
PYTHONPATH=src python3 -m unittest discover -s tests -t . -q
