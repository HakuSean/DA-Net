#!/usr/bin/env bash

DATASET=ixmas_branch
FEAT=$1
MODALITY=$2
OPTION=$3
SPLIT=$4
TRAIN=$5

if [[ ${MODALITY} == rgb ]]; then
    ITER=7000
else
    ITER=7000
fi

FOLDER=`echo ${FEAT}| cut -d / -f 1`

DATA_PATH=../data/IXMAS/img_flow/
DEPLOY=models/${DATASET}/${OPTION}/split${SPLIT}/${MODALITY}_deploy.prototxt
MODEL=models/${DATASET}/${OPTION}/caffemodel/${MODALITY}_split${SPLIT}_iter_${ITER}.caffemodel

mkdir -p logs/${DATASET}_scores/${OPTION}/${TRAIN}_${FOLDER}

CUDA_VISIBLE_DEVICES=$((${SPLIT}-1)) python analysis/extract_feat.py ${DATASET} 1 ${MODALITY} ${DATA_PATH} ${DEPLOY} ${MODEL} --oversample --train_test ${TRAIN} --num_worker 1 --feat ${FEAT} --save_features logs/${DATASET}_scores/${OPTION}/${TRAIN}_${FEAT}_${MODALITY}_split${SPLIT}.npz
