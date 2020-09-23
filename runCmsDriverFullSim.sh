if [[ $# -lt 2 ]]; then
    echo "Must have at least two arguments: runCmsDriverFullSim.sh <config fragment> <outputfile>"
    exit 1
fi

fragment=${1/python\//}
config="configs/${fragment/cff/cfg}"

if [[ $# -gt 2 ]]; then
    if [[ $3 -gt 0 ]]; then
        customize="--customise_commands process.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.DeltaIntersection=1e-6"
        config=${config/cfg/fineStepGeant_cfg}
    fi
fi

echo "Fragment is $fragment"


cmsDriver.py Configuration/WMassNanoGen/python/$fragment --mc \
    --eventcontent AODSIM --datatier AODSIM --conditions 106X_mcRun2_asymptotic_v13 \
        --beamspot Realistic25ns13TeV2016Collision --step GEN,SIM,DIGI,L1,DIGI2RAW,RAW2DIGI,L1Reco,RECO,RECOSIM \
        --geometry DB:Extended --era Run2_2016  --runUnscheduled --no_exec -n 20 --nThreads 2 \
        --python_filename $config \
        $customize
