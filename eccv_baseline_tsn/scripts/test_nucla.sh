#!/usr/bin/env bash

DATASET=$1
MODALITY=$2
OPTION=$3
SPLIT=$4

if [[ ${MODALITY} == rgb ]]; then
    ITER=3000
else
    ITER=3000
fi

DATA_PATH=../data/NUCLA/frames/
DEPLOY=models/${DATASET}/${OPTION}/split${SPLIT}/${MODALITY}_deploy.prototxt
MODEL=models/${DATASET}/${OPTION}/caffemodel/${MODALITY}_split${SPLIT}_iter_${ITER}.caffemodel
LOG_FILE=logs/${DATASET}_scores/${OPTION}/${MODALITY}_split${SPLIT}.log

mkdir -p logs/${DATASET}_scores/${OPTION}

CUDA_VISIBLE_DEVICE=2 #$(((${SPLIT}-1)/5+1))\
python tools/eval_net_nucla.py ${DATASET} ${SPLIT} ${MODALITY} ${DATA_PATH} ${DEPLOY} ${MODEL} --num_worker 1 --save_scores logs/${DATASET}_scores/${OPTION}/${MODALITY}_split${SPLIT}.npz 2>&1 | tee ${LOG_FILE}
