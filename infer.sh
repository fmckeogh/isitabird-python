#!/bin/sh
export TF_CPP_MIN_LOG_LEVEL=2
NAME=$1
python3 infer.py uploads/$NAME &
