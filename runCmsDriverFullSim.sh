if [[ $# -lt 2 ]]; then
    echo "Must have at least two arguments: runCmsDriverFullSim.sh <config fragment> <outputfile>"
    exit 1
fi

fragment=${1/python\//}
config="configs/${fragment/cff/MINIAOD_cfg}"

customize="--customise_commands process.patAlgosToolsTask.remove(process.patTrigger)\nprocess.slimmingTask.remove(process.patTrigger)\nprocess.slimmingTask.remove(process.selectedPatTrigger)\nprocess.slimmingTask.remove(process.slimmedPatTrigger)"

if [[ $# -gt 2 ]]; then
    if [[ $3 -gt 0 ]]; then
        customize="${customize}\nprocess.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.DeltaIntersection=1e-6\nprocess.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.DeltaOneStep=1e-4\nprocess.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.MaximumEpsilonStep=1e-6\nprocess.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.MinimumEpsilonStep=5e-7"
        config=${config/cfg/fineStepGeant_cfg}
    fi
fi

echo "Fragment is $fragment"

cmsDriver.py Configuration/WMassNanoGen/python/$fragment --mc --fileout file:$2 \
    --eventcontent MINIAODSIM --datatier MINIAODSIM --conditions 106X_mcRun2_asymptotic_v13 \
        --beamspot Realistic25ns13TeV2016Collision --step LHE,GEN,SIM,DIGI,L1,DIGI2RAW,RAW2DIGI,L1Reco,RECO,RECOSIM,PAT \
        --geometry DB:Extended --era Run2_2016  --runUnscheduled --no_exec -n 100 --nThreads 8 \
        --python_filename $config \
        $customize
