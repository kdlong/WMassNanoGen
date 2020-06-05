#! /bin/bash

#TODO: Make this a proper script that also creates a crab_submit file
if [[ $# -ne 2 ]]; then
    echo "Must have two arguments: runCmsDriverNanoGen.sh <config fragment> <outputfile>"
    exit 1
fi

fragment=${1/python\//}

cmsDriver.py Configuration/WMassNanoGen/python/$fragment \
    --fileout file:$2 --mc --eventcontent LHE,RAWSIM,NANOAODSIM \
    --datatier LHE,GEN,NANOAOD --conditions auto:mc --step LHE,GEN,NANOGEN \
    --python_filename configs/${fragment/cff/cfg} \
    --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=999 \
    -n 10 --no_exec \

