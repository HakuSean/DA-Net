#!/usr/bin/env bash

DATASET=ntu_view
MODALITY=$1
OPTION=$2
SPLIT=1
ITER=$3

TOOLS=lib/caffe-action/build/install/bin
LOG_FILE=logs/${DATASET}_logs/${OPTION}/${MODALITY}_split${SPLIT}.log
N_GPU=2
MPI_BIN_DIR= /home/dwan3342/Documents/openmpi/bin/
MODEL=models/${DATASET}_init/${OPTION}/${MODALITY}_split${SPLIT}_iter_${ITER}.caffemodel

mkdir -p logs/${DATASET}_logs/${OPTION}
echo "logging to ${LOG_FILE}"

${MPI_BIN_DIR}mpirun -np $N_GPU \
$TOOLS/caffe train --solver=models/${DATASET}/${OPTION}/split${SPLIT}/${MODALITY}_solver.prototxt \
   --weights=${MODEL} 2>&1 | tee ${LOG_FILE}
