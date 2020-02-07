#!/bin/bash
cmsDriver.py step1 --filein "dbs:/ZJToMuMu_TuneCUETP8M1_13TeV-powheg-MiNNLO-pythia8-photos/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM" \
    --fileout ZJToMuMu_TuneCUETP8M1_13TeV-powheg-MiNNLO-pythia8-photos_NanoGen.root --mc --eventcontent NANOAODGEN --datatier NANOAODSIM \
    --conditions 102X_mcRun2_asymptotic_v7 --step NANOGEN --nThreads 4 --python_filename configs/ZJToMuMu_TuneCUETP8M1_13TeV-powheg-MiNNLO-pythia8-photos_NanoGen.py \
    --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000 
