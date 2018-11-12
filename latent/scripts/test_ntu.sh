#!/usr/bin/env bash

DATASET=ntu_view
MODALITY=$1
OPTION=$2
SPLIT=1
ITER=$3

#if [[ ${MODALITY} == rgb ]]; then
#    ITER=12000 #24000
#else
#    ITER=9000   # 18000
#fi

DATA_PATH=../data/NTU/frames/
DEPLOY=models/${DATASET}/${OPTION}/split${SPLIT}/${MODALITY}_deploy.prototxt
MODEL=models/${DATASET}/${OPTION}/caffemodel/${MODALITY}_split${SPLIT}_iter_${ITER}.caffemodel
LOG_FILE=logs/${DATASET}_scores/${OPTION}/${MODALITY}_split${SPLIT}.log

mkdir -p logs/${DATASET}_scores/${OPTION}

CUDA_VISIBLE_DEVICES=0,1,2 \
python tools/eval_net_latent_rebuttal.py ${DATASET} ${SPLIT} ${MODALITY} ${DATA_PATH} ${DEPLOY} ${MODEL} --num_worker 3 --save_scores logs/${DATASET}_scores/${OPTION}/${MODALITY}_split${SPLIT}.npz #2>&1 | tee ${LOG_FILE}
