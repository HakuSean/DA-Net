#!/usr/bin/env bash
OPT=$2
DATA=$1
#TEST=$2 #ixmas for normal multi-clf, latent for combined clf

if [[ ${TEST} == 'ixmas_view' ]]; then
    SP=5
else
    SP=3
fi

if [[ ${DATA} == *_* ]]; then
    TEST=`echo ${DATA}| cut -d_ -f1`
else
    TEST=${DATA}
    SP=10
fi

for ((i=1; i<=${SP}; i++))
do
    bash scripts/test_${TEST}.sh ${DATA} flow ${OPT} $i 15
    bash scripts/test_${TEST}.sh ${DATA} rgb ${OPT} $i 15
done

#for ((i=1; i<=${SP}; i++))
#do
#    bash scripts/test_${TEST}.sh ${DATA} ${MOD} ${OPT} $i
#done
