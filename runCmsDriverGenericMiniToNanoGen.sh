#!/bin/bash

if [[ $# -lt 2 ]]; then
    echo "Requires at least two command line arguments!"
    echo "ex. (last two args optional): bash genericNanoGenFromMini.sh <das_path> <outfile.root> <config_name.py> <nevents>"
    exit 1
fi

das_name=$1
outfile=$2
config_name=${2/.root/_cfg.py}
nevents=1000
if [[ $# -gt 2 ]]; then
    config_name=$3
fi
if [[ $# -gt 3 ]]; then
    nevents=$4
fi

cmsDriver.py step1 --filein "dbs:$das_name" \
    --fileout $outfile --mc --eventcontent NANOAODGEN --datatier NANOAODSIM \
    --conditions 102X_mcRun2_asymptotic_v7 --step NANOGEN --nThreads 4 --python_filename $config_name \
    --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $nevents

