#! /bin/bash

#TODO: Make this a proper script that also creates a crab_submit file
if [[ $# -ne 2 ]]; then
    echo "Must have two arguments: runCmsDriverNanoGen.sh <input_gen> <outputfile>"
    exit 1
fi

cmsDriver.py step2 \
    --fileout file:$2 --mc --eventcontent NANOAODSIM \
    --filein file:$1 \
    --datatier NANOAODSIM --conditions auto:mc --step NANOGEN \
    --python_filename configs/${2/root/py} \
    --customise PhysicsTools/NanoAOD/nanogen_cff.customizeNanoGEN \
    -n -1 --no_exec 
