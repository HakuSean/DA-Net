#!/usr/bin/env bash
DATA=$1
if [[ ${DATA} == *_* ]]; then
    TEST=`echo ${DATA}| cut -d_ -f1`
else
    TEST=${DATA}
fi
OPT=in5b_branch
SPLIT=$2

bash scripts/train_tsn.sh ${DATA} flow ${OPT} ${SPLIT}
#bash scripts/train_tsn.sh ${DATA} rgb ${OPT} ${SPLIT}
#bash scripts/test_${TEST}.sh ${DATA} rgb ${OPT} ${SPLIT}
#bash scripts/test_${TEST}.sh ${DATA} flow ${OPT} ${SPLIT}

