#!/usr/bin/env bash

DATASET=$1
MODALITY=$2
OPTION=$3
SPLIT=$4

#if [[ ${MODALITY} == rgb ]]; then
#    ITER=5000
#else
#    ITER=2500
#fi

DATA_PATH=../data/IXMAS/img_flow/
DEPLOY=models/${DATASET}/${OPTION}/split${SPLIT}/${MODALITY}_deploy.prototxt
mkdir -p logs/${DATASET}_scores/${OPTION}

#for i in {1..5}
#do
    ITER=7000 #$((i*1000))
    MODEL=models/${DATASET}/${OPTION}/caffemodel/${MODALITY}_split${SPLIT}_iter_${ITER}.caffemodel
    LOG_FILE=logs/${DATASET}_scores/${OPTION}/${MODALITY}_split${SPLIT}_${ITER}.log
    #UDA_VISIBLE_DEVICES=0 \
    python tools/eval_net_latent.py ${DATASET} ${SPLIT} ${MODALITY} ${DATA_PATH} ${DEPLOY} ${MODEL} --num_worker 1 --save_scores logs/${DATASET}_scores/${OPTION}/${MODALITY}_split${SPLIT}_${ITER}.npz 2>&1 | tee ${LOG_FILE}
#done
