if [[ $# -lt 2 ]]; then
    echo "Must have at least two arguments: runCmsDriverFullSim.sh <config fragment> <inputfile>"
    exit 1
fi

cmsDriver.py step1 --filein $2 --fileout ${2/.root/_NANOAOD.root} \
    --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 106X_mcRun2_asymptotic_v13 \
        --mc --step NANO --era Run2_2016  --no_exec -n -1 --nThreads 8 \
        --customise_commands "process.nanoSequenceMC.remove(process.nanoSequenceOnlyFullSim)" \
        --python_filename $1
