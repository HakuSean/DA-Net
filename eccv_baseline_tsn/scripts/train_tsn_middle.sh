#!/usr/bin/env bash

DATASET=$1
MODALITY=$2
OPTION=$3
SPLIT=$4
ITER=$5

TOOLS=lib/caffe-action/build/install/bin
LOG_FILE=logs/${DATASET}_logs/${OPTION}/${MODALITY}_split${SPLIT}
N_GPU=1
MPI_BIN_DIR= #/usr/local/openmpi/bin/

mkdir -p logs/${DATASET}_logs/${OPTION}
echo "logging to ${LOG_FILE}"

#${MPI_BIN_DIR}mpirun -np $N_GPU \
$TOOLS/caffe train --solver=models/${DATASET}/${OPTION}/split${SPLIT}/${MODALITY}_solver.prototxt \
   --snapshot=models/${DATASET}/${OPTION}/caffemodel/${MODALITY}_split${SPLIT}_iter_${ITER}.solverstate 2>&1 | tee ${LOG_FILE}_${ITER}.log
