#!/usr/bin/env bash
DATA=$1
OPT=in5b_share
MOD=$2

# bash scripts/train_tsn.sh ${DATA} rgb ${OPT} 3
# bash scripts/train_tsn.sh ${DATA} flow ${OPT} 3
# bash scripts/train_tsn.sh ${DATA} rgb ${OPT} 6
# bash scripts/train_tsn.sh ${DATA} flow ${OPT} 6
# bash scripts/train_tsn.sh ${DATA} rgb ${OPT} 10
# bash scripts/train_tsn.sh ${DATA} flow ${OPT} 10

bash scripts/train_tsn.sh ${DATA} ${MOD} ${OPT} 1
bash scripts/train_tsn.sh ${DATA} ${MOD} ${OPT} 5
bash scripts/train_tsn.sh ${DATA} ${MOD} ${OPT} 2

#bash scripts/train_tsn.sh ${DATA} rgb in5b_branch 10
#bash scripts/train_tsn.sh ${DATA} flow in5b_branch 10
#bash scripts/train_tsn.sh ${DATA} rgb in5b_seg2 3
#bash scripts/train_tsn.sh ${DATA} flow in5b_seg2 3
#bash scripts/train_tsn.sh ${DATA} rgb in5b_seg4 3
#bash scripts/train_tsn.sh ${DATA} flow in5b_seg4 3
