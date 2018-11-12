#!/usr/bin/env bash
OPT=$1
GPU=$2

if [[ ${GPU} == 0 ]]; then
    bash scripts/train_tsn.sh ixmas rgb ${OPT} 1
    bash scripts/train_tsn.sh ixmas rgb ${OPT} 2
    bash scripts/train_tsn.sh ixmas rgb ${OPT} 3
    bash scripts/train_tsn.sh ixmas rgb ${OPT} 4
    bash scripts/train_tsn.sh ixmas rgb ${OPT} 5
    bash scripts/train_tsn.sh ixmas rgb ${OPT} 6
    bash scripts/train_tsn.sh ixmas rgb ${OPT} 7
    bash scripts/train_tsn.sh ixmas rgb ${OPT} 8
    bash scripts/train_tsn.sh ixmas rgb ${OPT} 9
    bash scripts/train_tsn.sh ixmas rgb ${OPT} 10
    # bash scripts/test_ixmas.sh ixmas rgb ${OPT} 1
    # bash scripts/test_ixmas.sh ixmas rgb ${OPT} 2
    # bash scripts/test_ixmas.sh ixmas rgb ${OPT} 3
    # bash scripts/test_ixmas.sh ixmas rgb ${OPT} 4
    # bash scripts/test_ixmas.sh ixmas rgb ${OPT} 5
    # bash scripts/test_ixmas.sh ixmas rgb ${OPT} 6
    # bash scripts/test_ixmas.sh ixmas rgb ${OPT} 7
    # bash scripts/test_ixmas.sh ixmas rgb ${OPT} 8
    # bash scripts/test_ixmas.sh ixmas rgb ${OPT} 9
    # bash scripts/test_ixmas.sh ixmas rgb ${OPT} 10

elif [[ ${GPU} == 1 ]]; then
    bash scripts/train_tsn.sh ixmas flow ${OPT} 1
    bash scripts/train_tsn.sh ixmas flow ${OPT} 2
    bash scripts/train_tsn.sh ixmas flow ${OPT} 3
    bash scripts/train_tsn.sh ixmas flow ${OPT} 4
    bash scripts/train_tsn.sh ixmas flow ${OPT} 5
    # bash scripts/test_ixmas.sh ixmas flow ${OPT} 1
    # bash scripts/test_ixmas.sh ixmas flow ${OPT} 2
    # bash scripts/test_ixmas.sh ixmas flow ${OPT} 3
    # bash scripts/test_ixmas.sh ixmas flow ${OPT} 4
    # bash scripts/test_ixmas.sh ixmas flow ${OPT} 5
else
    bash scripts/train_tsn.sh ixmas flow ${OPT} 6
    bash scripts/train_tsn.sh ixmas flow ${OPT} 7
    bash scripts/train_tsn.sh ixmas flow ${OPT} 8
    bash scripts/train_tsn.sh ixmas flow ${OPT} 9
    bash scripts/train_tsn.sh ixmas flow ${OPT} 10

    # bash scripts/test_ixmas.sh ixmas flow ${OPT} 6
    # bash scripts/test_ixmas.sh ixmas flow ${OPT} 7
    # bash scripts/test_ixmas.sh ixmas flow ${OPT} 8
    # bash scripts/test_ixmas.sh ixmas flow ${OPT} 9
    # bash scripts/test_ixmas.sh ixmas flow ${OPT} 10
fi



