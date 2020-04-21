#! /bin/bash

#TODO: Make this a proper script that also creates a crab_submit file
if [[ $# -ne 3 ]]; then
    echo "Must have two arguments: runCmsDriverNanoGen.sh <config fragment> <outputfile> input_pLHE.root"
    exit 1
fi

fragment=${1/python\//}

cmsDriver.py Configuration/WMassNanoGen/python/$fragment \
    --fileout file:$2 --mc --eventcontent NANOAODSIM \
    --filein file:$3 \
    --datatier NANOAODSIM --conditions auto:mc --step GEN,NANOGEN \
    --python_filename configs/${fragment/cff/cfg} \
    -n -1 --no_exec \
