if [[ $# -lt 2 ]]; then
    echo "Must have at least two arguments: runCmsDriverFullSim.sh <config fragment> <outputfile>"
    exit 1
fi

cmsDriver.py step1 --filein $2 --fileout ${2/.root/_MINIAOD.root} \
    --eventcontent MINIAODSIM --datatier MINIAODSIM --conditions 106X_mcRun2_asymptotic_v13 \
        --beamspot Realistic25ns13TeV2016Collision --mc --step PAT \
        --geometry DB:Extended --era Run2_2016  --runUnscheduled --no_exec -n 20 --nThreads 2 \
        --customise_commands "process.patAlgosToolsTask.remove(process.patTrigger)\nprocess.slimmingTask.remove(process.patTrigger)\nprocess.slimmingTask.remove(process.selectedPatTrigger)\nprocess.slimmingTask.remove(process.slimmedPatTrigger)" \
        --python_filename $1
