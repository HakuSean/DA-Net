#!/usr/bin/env bash
DATA=ixmas_view
if [[ ${DATA} == *_* ]]; then
    TEST=`echo ${DATA}| cut -d_ -f1`
else
    TEST=${DATA}
fi
OPT=$1 #tsn_manual1
SPLIT=5

#for SPLIT in {1..10}
#do
    bash scripts/train_tsn.sh ${DATA} rgb ${OPT} ${SPLIT}
    bash scripts/train_tsn.sh ${DATA} flow ${OPT} ${SPLIT}
    bash scripts/test_${TEST}.sh ${DATA} rgb ${OPT} ${SPLIT}
    bash scripts/test_${TEST}.sh ${DATA} flow ${OPT} ${SPLIT}
#done

