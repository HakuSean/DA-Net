#!/usr/bin/env bash
OPT=$1
TEST=$2

#bash scripts/train.sh ixmas flow ${OPT} 1
#bash scripts/train.sh ixmas flow ${OPT} 5
#bash scripts/train.sh ixmas rgb ${OPT} 2
bash scripts/train.sh ixmas rgb ${OPT} 3
bash scripts/train.sh ixmas rgb ${OPT} 8
# #bash scripts/train.sh ixmas_branch rgb ${OPT} 1

# #bash scripts/train.sh ixmas_branch rgb ${OPT} 2

# #bash scripts/train.sh ixmas_branch rgb ${OPT} 3

# bash scripts/train.sh ixmas_branch flow ${OPT} 1

# bash scripts/train.sh ixmas_branch flow ${OPT} 2

# #bash scripts/train.sh ixmas_branch flow ${OPT} 3
# #bash scripts/test_${TEST}.sh ixmas_branch rgb ${OPT} 1
# #bash scripts/test_${TEST}.sh ixmas_branch rgb ${OPT} 2
# #bash scripts/test_${TEST}.sh ixmas_branch rgb ${OPT} 3
# #bash scripts/test_${TEST}.sh ixmas_branch flow ${OPT} 1
#bash scripts/test_${TEST}.sh ixmas flow ${OPT} 1
#bash scripts/test_${TEST}.sh ixmas flow ${OPT} 5
#bash scripts/test_${TEST}.sh ixmas rgb ${OPT} 2
bash scripts/test_${TEST}.sh ixmas rgb ${OPT} 3
bash scripts/test_${TEST}.sh ixmas rgb ${OPT} 8
