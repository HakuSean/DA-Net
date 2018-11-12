#!/usr/bin/env bash
OPT=$2 #in5b_branch
DATA=$1
if [[ ${DATA} == *_* ]]; then
    TEST=`echo ${DATA}| cut -d_ -f1`
else
    TEST=${DATA}
fi
#MOD=$2

if [[ ${TEST} == 'ixmas' ]]; then
    SP=5
else
    SP=3
fi

for ((i=1; i<=${SP}; i++))
do
    bash scripts/train.sh ${DATA} flow ${OPT} $i
#    bash scripts/train.sh ${DATA} rgb ${OPT} $i
done

#for ((i=1; i<=${SP}; i++))
#do
#    bash scripts/test_${TEST}.sh ${DATA} ${MOD} ${OPT} $i
#done
