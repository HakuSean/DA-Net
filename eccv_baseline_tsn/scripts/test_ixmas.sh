#!/usr/bin/env bash

DATASET=$1
MODALITY=$2
OPTION=$3
SPLIT=$4

if [[ ${MODALITY} == rgb ]]; then
    ITER=7000
else
    ITER=8000
fi

DATA_PATH=../data/IXMAS/img_flow/
DEPLOY=models/${DATASET}/${OPTION}/split${SPLIT}/${MODALITY}_deploy.prototxt
MODEL=models/${DATASET}/${OPTION}/caffemodel/${MODALITY}_split${SPLIT}_iter_${ITER}.caffemodel

mkdir -p logs/${DATASET}_scores/${OPTION}
LOG_FILE=logs/${DATASET}_scores/${OPTION}/${MODALITY}_split${SPLIT}.log

#CUDA_VISIBLE_DEVICES=$((${SPLIT}-1)) \
CUDA_VISIBLE_DEVICES=2 \
python tools/eval_net.py ${DATASET} ${SPLIT} ${MODALITY} ${DATA_PATH} ${DEPLOY} ${MODEL} --num_worker 1 --save_scores logs/${DATASET}_scores/${OPTION}/${MODALITY}_split${SPLIT}.npz 2>&1 | tee ${LOG_FILE}
