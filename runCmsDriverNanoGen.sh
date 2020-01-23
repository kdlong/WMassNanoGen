#! /bin/bash

#TODO: Make this a proper script that also creates a crab_submit file
if [[ $# -ne 2 ]]; then
    echo "Must have two arguments: runCmsDriverNanoGen.sh <config fragment> <outputfile>"
    exit 1
fi

cmsDriver.py Configuration/WMassNanoGen/python/$1 \
    --fileout file:$2 --mc --eventcontent NANOAODSIM \
    --datatier NANOAOD --conditions auto:mc --step LHE,GEN,NANOGEN \
    --python_filename configs/${1/cff/cfg} -n 500 --no_exec
