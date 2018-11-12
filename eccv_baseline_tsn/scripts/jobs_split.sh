#!/usr/bin/env bash
DATA=$1
OPT=in4e_branch
GPU=$2

bash scripts/train_tsn.sh ${DATA} rgb ${OPT} $((1+${GPU}*3))
bash scripts/train_tsn.sh ${DATA} rgb ${OPT} $((2+${GPU}*3))
bash scripts/train_tsn.sh ${DATA} rgb ${OPT} $((3+${GPU}*3))

bash scripts/train_tsn.sh ${DATA} flow ${OPT} $((1+${GPU}*3))
bash scripts/train_tsn.sh ${DATA} flow ${OPT} $((2+${GPU}*3))
bash scripts/train_tsn.sh ${DATA} flow ${OPT} $((3+${GPU}*3))

bash scripts/test_ixmas.sh ${DATA} rgb ${OPT} $((1+${GPU}*3))
bash scripts/test_ixmas.sh ${DATA} rgb ${OPT} $((2+${GPU}*3))
bash scripts/test_ixmas.sh ${DATA} rgb ${OPT} $((3+${GPU}*3))

bash scripts/test_ixmas.sh ${DATA} flow ${OPT} $((1+${GPU}*3))
bash scripts/test_ixmas.sh ${DATA} flow ${OPT} $((2+${GPU}*3))
bash scripts/test_ixmas.sh ${DATA} flow ${OPT} $((3+${GPU}*3))

if [[ ${GPU} == 2 ]]; then
    bash scripts/train_tsn.sh ${DATA} rgb ${OPT} $((4+${GPU}*3))
    bash scripts/train_tsn.sh ${DATA} flow ${OPT} $((4+${GPU}*3))
    bash scripts/test_ixmas.sh ${DATA} rgb ${OPT} $((4+${GPU}*3))
    bash scripts/test_ixmas.sh ${DATA} flow ${OPT} $((4+${GPU}*3))
fi


