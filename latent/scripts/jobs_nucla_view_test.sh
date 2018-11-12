#!/usr/bin/env bash
OPT=mp_com_share
ITER=10000

bash scripts/test_nucla_cheat.sh nucla_view rgb 4000 1 5
bash scripts/test_nucla_cheat.sh nucla_view rgb 6000 2 5
bash scripts/test_nucla_cheat.sh nucla_view rgb 9000 3 5

bash scripts/test_nucla_cheat.sh nucla_view flow 8000 1 5
bash scripts/test_nucla_cheat.sh nucla_view flow 4000 2 5
bash scripts/test_nucla_cheat.sh nucla_view flow 4000 3 5

bash scripts/test_nucla_cheat.sh nucla_view rgb ${ITER} 1 5
bash scripts/test_nucla_cheat.sh nucla_view rgb ${ITER} 2 5
bash scripts/test_nucla_cheat.sh nucla_view rgb ${ITER} 3 5

bash scripts/test_nucla_cheat.sh nucla_view flow ${ITER} 1 5
bash scripts/test_nucla_cheat.sh nucla_view flow ${ITER} 2 5
bash scripts/test_nucla_cheat.sh nucla_view flow ${ITER} 3 5
