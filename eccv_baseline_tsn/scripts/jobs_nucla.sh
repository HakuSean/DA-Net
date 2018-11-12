#!/usr/bin/env bash
OPT=$1

bash scripts/train_tsn.sh nucla flow ${OPT} 1
bash scripts/train_tsn.sh nucla flow ${OPT} 2
bash scripts/train_tsn.sh nucla flow ${OPT} 3
bash scripts/train_tsn.sh nucla flow ${OPT} 4
bash scripts/train_tsn.sh nucla flow ${OPT} 5
bash scripts/train_tsn.sh nucla flow ${OPT} 6
bash scripts/train_tsn.sh nucla flow ${OPT} 7
bash scripts/train_tsn.sh nucla flow ${OPT} 8
bash scripts/train_tsn.sh nucla flow ${OPT} 9
bash scripts/train_tsn.sh nucla flow ${OPT} 10

# # bash scripts/test_nucla.sh nucla rgb ${OPT} 1
# # bash scripts/test_nucla.sh nucla rgb ${OPT} 2
# # bash scripts/test_nucla.sh nucla rgb ${OPT} 3
# # bash scripts/test_nucla.sh nucla rgb ${OPT} 4
# # bash scripts/test_nucla.sh nucla rgb ${OPT} 5
# bash scripts/test_nucla.sh nucla rgb ${OPT} 6
# bash scripts/test_nucla.sh nucla rgb ${OPT} 7
# bash scripts/test_nucla.sh nucla rgb ${OPT} 8
# bash scripts/test_nucla.sh nucla rgb ${OPT} 9
# bash scripts/test_nucla.sh nucla rgb ${OPT} 10

# # bash scripts/test_nucla.sh nucla flow ${OPT} 1
# # bash scripts/test_nucla.sh nucla flow ${OPT} 2
# # bash scripts/test_nucla.sh nucla flow ${OPT} 3
# # bash scripts/test_nucla.sh nucla flow ${OPT} 4
# # bash scripts/test_nucla.sh nucla flow ${OPT} 5
# bash scripts/test_nucla.sh nucla flow ${OPT} 6
# bash scripts/test_nucla.sh nucla flow ${OPT} 7
# bash scripts/test_nucla.sh nucla flow ${OPT} 8
# bash scripts/test_nucla.sh nucla flow ${OPT} 9
# bash scripts/test_nucla.sh nucla flow ${OPT} 10
