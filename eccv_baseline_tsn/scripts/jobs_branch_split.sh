#!/usr/bin/env bash
DATA=ixmas_branch
if [[ ${DATA} == *_* ]]; then
    TEST=`echo ${DATA}| cut -d_ -f1`
else
    TEST=${DATA}
fi
OPT=$1
SPLIT=$2

bash scripts/train_tsn.sh ${DATA} flow ${OPT} ${SPLIT}
bash scripts/train_tsn.sh ${DATA} rgb ${OPT} ${SPLIT}
bash scripts/test_${TEST}.sh ${DATA} rgb ${OPT} ${SPLIT}
bash scripts/test_${TEST}.sh ${DATA} flow ${OPT} ${SPLIT}

