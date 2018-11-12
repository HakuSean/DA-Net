#!/usr/bin/env bash

DATASET=$1
MODALITY=$2
OPTION=$3
SPLIT=$4
FRAME=5

if [[ ${OPTION} == *two* ]]; then
    ITER=7000
else
    ITER=2000
fi

DATA_PATH=../data/NUCLA/frames/
DEPLOY=models/${DATASET}/${OPTION}/split${SPLIT}/${MODALITY}_deploy.prototxt
MODEL=models/${DATASET}/${OPTION}/caffemodel/${MODALITY}_split${SPLIT}_iter_${ITER}.caffemodel
LOG_FILE=logs/${DATASET}_scores/${OPTION}_${FRAME}frames/${MODALITY}_split${SPLIT}.log

mkdir -p logs/${DATASET}_scores/${OPTION}_${FRAME}frames

CUDA_VISIBLE_DEVICES=0,1,2 \
python tools/eval_net_latent.py ${DATASET} ${SPLIT} ${MODALITY} ${DATA_PATH} ${DEPLOY} ${MODEL} --num_worker 3 --num_frame_per_video ${FRAME} --save_scores logs/${DATASET}_scores/${OPTION}_${FRAME}frames/${MODALITY}_split${SPLIT}.npz 2>&1 | tee ${LOG_FILE}
