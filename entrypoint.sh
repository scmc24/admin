#!/usr/bin/env sh
set -e

if [ "$1" = "test" ]; then
    exec pytest -v
else
    exec python admin.py
fi
