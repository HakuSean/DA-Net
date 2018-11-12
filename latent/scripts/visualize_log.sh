#!/usr/bin/env bash
FILE=$1
TRTE=$2
Y=$3

python tools/parse_log.py ${FILE}
gnuplot -c scripts/gnu.sh ${FILE}.${TRTE} ${FILE}_${TRTE}_${Y}.png ${Y}
