#!/usr/bin/env bash
DATA=$1
if [[ ${DATA} == *_* ]]; then
    TEST=`echo ${DATA}| cut -d_ -f1`
else
    TEST=${DATA}
fi
OPT=mp_com
SPLIT=$2

#bash scripts/train.sh ${DATA} flow ${OPT} ${SPLIT}
bash scripts/train.sh ${DATA} rgb ${OPT} ${SPLIT}
#bash scripts/test_${TEST}.sh ${DATA} rgb ${OPT} ${SPLIT}
#bash scripts/test_${TEST}.sh ${DATA} flow ${OPT} ${SPLIT}

