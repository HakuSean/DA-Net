#!/usr/bin/env bash
OPT=$1
GPU=$2

if [[ ${GPU} == 0 ]]; then
    bash scripts/train_tsn.sh ixmas_view rgb ${OPT} 1
    bash scripts/train_tsn.sh ixmas_view rgb ${OPT} 2
    bash scripts/train_tsn.sh ixmas_view rgb ${OPT} 3
    bash scripts/train_tsn.sh ixmas_view rgb ${OPT} 4
    bash scripts/train_tsn.sh ixmas_view flow ${OPT} 1
    bash scripts/train_tsn.sh ixmas_view flow ${OPT} 2
    bash scripts/train_tsn.sh ixmas_view flow ${OPT} 3
    bash scripts/train_tsn.sh ixmas_view flow ${OPT} 4
    # bash scripts/test_ixmas.sh ixmas_view rgb ${OPT} 1
    # bash scripts/test_ixmas.sh ixmas_view rgb ${OPT} 2
    # bash scripts/test_ixmas.sh ixmas_view rgb ${OPT} 3
    # bash scripts/test_ixmas.sh ixmas_view rgb ${OPT} 4
    # bash scripts/test_ixmas.sh ixmas_view rgb ${OPT} 5
    # bash scripts/test_ixmas.sh ixmas_view rgb ${OPT} 6
    # bash scripts/test_ixmas.sh ixmas_view rgb ${OPT} 7
    # bash scripts/test_ixmas.sh ixmas_view rgb ${OPT} 8
    # bash scripts/test_ixmas.sh ixmas_view rgb ${OPT} 9
    # bash scripts/test_ixmas.sh ixmas_view rgb ${OPT} 10

elif [[ ${GPU} == 1 ]]; then
    bash scripts/train_tsn.sh ixmas_view flow ${OPT} 5
    bash scripts/train_tsn.sh ixmas_view flow ${OPT} 6
    bash scripts/train_tsn.sh ixmas_view flow ${OPT} 7
    bash scripts/train_tsn.sh ixmas_view flow ${OPT} 8
    bash scripts/train_tsn.sh ixmas_view rgb ${OPT} 5
    bash scripts/train_tsn.sh ixmas_view rgb ${OPT} 6
    bash scripts/train_tsn.sh ixmas_view rgb ${OPT} 7
    bash scripts/train_tsn.sh ixmas_view rgb ${OPT} 8

    # bash scripts/test_ixmas.sh ixmas_view flow ${OPT} 1
    # bash scripts/test_ixmas.sh ixmas_view flow ${OPT} 2
    # bash scripts/test_ixmas.sh ixmas_view flow ${OPT} 3
    # bash scripts/test_ixmas.sh ixmas_view flow ${OPT} 4
    # bash scripts/test_ixmas.sh ixmas_view flow ${OPT} 5
else
    bash scripts/train_tsn.sh ixmas_view rgb ${OPT} 9
    bash scripts/train_tsn.sh ixmas_view rgb ${OPT} 10
    bash scripts/train_tsn.sh ixmas_view rgb ${OPT} 11
    bash scripts/train_tsn.sh ixmas_view flow ${OPT} 9
    bash scripts/train_tsn.sh ixmas_view flow ${OPT} 10
    bash scripts/train_tsn.sh ixmas_view flow ${OPT} 11

    # bash scripts/test_ixmas.sh ixmas_view flow ${OPT} 6
    # bash scripts/test_ixmas.sh ixmas_view flow ${OPT} 7
    # bash scripts/test_ixmas.sh ixmas_view flow ${OPT} 8
    # bash scripts/test_ixmas.sh ixmas_view flow ${OPT} 9
    # bash scripts/test_ixmas.sh ixmas_view flow ${OPT} 10
fi



