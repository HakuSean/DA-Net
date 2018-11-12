#!/usr/bin/env bash

DATASET=$1
MODALITY=$2
OPTION=mp_com_share_sgd
SPLIT=$4
FRAME=$5

DATA_PATH=../data/NUCLA/frames/
DEPLOY=models/${DATASET}/${OPTION}/split${SPLIT}/${MODALITY}_deploy.prototxt
mkdir -p logs/${DATASET}_scores/${OPTION}

ITER=$3 #$((i*1000))
MODEL=models/${DATASET}/${OPTION}/caffemodel/${MODALITY}_split${SPLIT}_iter_${ITER}.caffemodel
LOG_FILE=logs/${DATASET}_scores/${OPTION}/${MODALITY}_split${SPLIT}_${ITER}.log

CUDA_VISIBLE_DEVICES=0,1,2 \
python tools/eval_net_latent.py ${DATASET} ${SPLIT} ${MODALITY} ${DATA_PATH} ${DEPLOY} ${MODEL} --num_worker 3 --num_frame_per_video ${FRAME} --save_scores logs/${DATASET}_scores/${OPTION}/${MODALITY}_split${SPLIT}_${ITER}.npz 2>&1 | tee ${LOG_FILE}

