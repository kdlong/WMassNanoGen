# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/WplusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM --fileout test.root --mc --eventcontent NANOAODGEN --datatier NANOAODSIM --conditions 102X_mcRun2_asymptotic_v7 --step NANOGEN --nThreads 4 --python_filename configs/MassWeightsTest_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10
import FWCore.ParameterSet.Config as cms



process = cms.Process('NANOGEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nanogen_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/group/cmst3/group/wmass/w-mass-13TeV/edmLHE/WplusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/LHE_massWeights_svn3900/220409_181954/0004/SMP-RunIISummer20UL16MiniAOD-massWeights_4812.root'),
    secondaryFileNames = cms.untracked.vstring( (
        #'/store/mc/RunIISummer20UL16MiniAOD/WplusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230001/88BB2121-1432-2D44-A70A-DD67836AFF62.root'        
        'file:88BB2121-1432-2D44-A70A-DD67836AFF62.root'
     ) )
)


process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODGENoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('test.root'),
    outputCommands = process.NANOAODGENEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_mcRun2_asymptotic_v7', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanogenSequence)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODGENoutput_step = cms.EndPath(process.NANOAODGENoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODGENoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nanogen_cff
from PhysicsTools.NanoAOD.nanogen_cff import customizeNanoGENFromMini 

#call to customisation function customizeNanoGENFromMini imported from PhysicsTools.NanoAOD.nanogen_cff
process = customizeNanoGENFromMini(process)

process.lheWeightsNano.lheSourceLabels = ["correctMassWeights"]
process.lheWeightsNano.debug = cms.untracked.bool(True)

process.massWeights = cms.EDProducer("LHEWeightProductProducer",
    lheSourceLabels = cms.vstring("correctMassWeights"),
)

process.genWeightsTable.maxGroupsPerType = [-1, -1, -1, -1, -1]

process.massWeightsTable = process.genWeightsTable.clone(
    lheWeights = cms.VInputTag("massWeights"),
    weightgroups = cms.vstring(['scale', 'matrix element', 'unknown']),
    outputNames = cms.vstring(['H2BugFixWeight', 'CorrectedMassWeight', 'UnknownWeight']),
    maxGroupsPerType = cms.vint32([-1, -1, -1]),
)
process.massWeightsTable.weightgroups = ['scale', 'PDF', 'matrix element', 'unknown', 'parton shower']
process.massWeightsTable.outputNames = ['H2BugFixWeight', 'PdfWeight', 'CorrectedMassWeight', 'UnknownWeight', 'PSWeight']
process.massWeightsTable.maxGroupsPerType = [1, 0, 1, -1, 0]

process.nanogenSequence.insert(-1, process.massWeights)
process.nanogenSequence.insert(-1, process.massWeightsTable)
    

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
