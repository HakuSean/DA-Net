#!/usr/bin/env bash

DATASET=$1
MODALITY=$2
OPTION=$3
SPLIT=$4

if [[ ${MODALITY} == rgb ]]; then
    ITER=5000
else
    ITER=5000
fi

TOOLS=lib/caffe-action/build/install/bin
LOG_FILE=logs/${DATASET}_logs/${OPTION}/${MODALITY}_split${SPLIT}.log
N_GPU=1
#MPI_BIN_DIR= ~/Documents/openmpi/bin/ 
MODEL=`ls models/${DATASET}_init/${OPTION}/${MODALITY}_split${SPLIT}_iter_*`

mkdir -p logs/${DATASET}_logs/${OPTION}
echo "logging to ${LOG_FILE}"

#${MPI_BIN_DIR}mpirun -np $N_GPU \
$TOOLS/caffe train --solver=models/${DATASET}/${OPTION}/split${SPLIT}/${MODALITY}_solver.prototxt \
   --weights=${MODEL} 2>&1 | tee ${LOG_FILE}
