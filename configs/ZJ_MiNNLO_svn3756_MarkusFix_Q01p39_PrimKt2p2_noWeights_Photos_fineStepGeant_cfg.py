# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/WMassNanoGen/python/ZJ_MiNNLO_svn3756_MarkusFix_Q01p39_PrimKt2p2_noWeights_Photos_cff.py --mc --fileout file:ZJ_MiNNLO_svn3756_MarkusFix_Q01p39_PrimKt2p2_noWeights_Photos_fullSim.root --eventcontent AODSIM --datatier AODSIM --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step LHE,GEN,SIM,DIGI,L1,DIGI2RAW,RAW2DIGI,L1Reco,RECO,RECOSIM --geometry DB:Extended --era Run2_2016 --runUnscheduled --no_exec -n 20 --nThreads 2 --python_filename configs/ZJ_MiNNLO_svn3756_MarkusFix_Q01p39_PrimKt2p2_noWeights_Photos_fineStepGeant_cfg.py --customise_commands process.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.DeltaIntersection=1e-6
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_cff import Run2_2016

process = cms.Process('RECO',Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeV2016Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.RecoSim_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/WMassNanoGen/python/ZJ_MiNNLO_svn3756_MarkusFix_Q01p39_PrimKt2p2_noWeights_Photos_cff.py nevts:20'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(31457280),
    fileName = cms.untracked.string('file:ZJ_MiNNLO_svn3756_MarkusFix_Q01p39_PrimKt2p2_noWeights_Photos_fullSim.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_v13', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    ExternalDecays = cms.PSet(
        Photospp = cms.untracked.PSet(
            forceBremForDecay = cms.PSet(
                Wm = cms.vint32(0, -24),
                Wp = cms.vint32(0, 24),
                Z = cms.vint32(0, 23),
                parameterSets = cms.vstring(
                    'Z', 
                    'Wp', 
                    'Wm'
                )
            ),
            parameterSets = cms.vstring(
                'setExponentiation', 
                'setInfraredCutOff', 
                'setMeCorrectionWtForW', 
                'setMeCorrectionWtForZ', 
                'setMomentumConservationThreshold', 
                'setPairEmission', 
                'setPhotonEmission', 
                'setStopAtCriticalError', 
                'suppressAll', 
                'forceBremForDecay'
            ),
            setExponentiation = cms.bool(True),
            setInfraredCutOff = cms.double(0.00011),
            setMeCorrectionWtForW = cms.bool(True),
            setMeCorrectionWtForZ = cms.bool(True),
            setMomentumConservationThreshold = cms.double(0.1),
            setPairEmission = cms.bool(True),
            setPhotonEmission = cms.bool(True),
            setStopAtCriticalError = cms.bool(False),
            suppressAll = cms.bool(True)
        ),
        parameterSets = cms.vstring('Photospp')
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'pythia8PowhegEmissionVetoSettings', 
            'pythia8PSweightsSettings', 
            'processParameters'
        ),
        processParameters = cms.vstring(
            'POWHEG:nFinal = 2', 
            'ParticleDecays:allowPhotonRadiation = on', 
            'TimeShower:QEDshowerByL = off', 
            'BeamRemnants:hardKTOnlyLHE = on', 
            'BeamRemnants:primordialKThard = 2.225001', 
            'SpaceShower:dipoleRecoil = 1'
        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118', 
            'SigmaTotal:mode = 0', 
            'SigmaTotal:sigmaEl = 21.89', 
            'SigmaTotal:sigmaTot = 100.309', 
            'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'
        ),
        pythia8PSweightsSettings = cms.vstring(
            'UncertaintyBands:doVariations = on', 
            'UncertaintyBands:List = {isrRedHi isr:muRfac=0.707,fsrRedHi fsr:muRfac=0.707,isrRedLo isr:muRfac=1.414,fsrRedLo fsr:muRfac=1.414,isrDefHi isr:muRfac=0.5,fsrDefHi fsr:muRfac=0.5,isrDefLo isr:muRfac=2.0,fsrDefLo fsr:muRfac=2.0,isrConHi isr:muRfac=0.25,fsrConHi fsr:muRfac=0.25,isrConLo isr:muRfac=4.0,fsrConLo fsr:muRfac=4.0,fsr_G2GG_muR_dn fsr:G2GG:muRfac=0.5,fsr_G2GG_muR_up fsr:G2GG:muRfac=2.0,fsr_G2QQ_muR_dn fsr:G2QQ:muRfac=0.5,fsr_G2QQ_muR_up fsr:G2QQ:muRfac=2.0,fsr_Q2QG_muR_dn fsr:Q2QG:muRfac=0.5,fsr_Q2QG_muR_up fsr:Q2QG:muRfac=2.0,fsr_X2XG_muR_dn fsr:X2XG:muRfac=0.5,fsr_X2XG_muR_up fsr:X2XG:muRfac=2.0,fsr_G2GG_cNS_dn fsr:G2GG:cNS=-2.0,fsr_G2GG_cNS_up fsr:G2GG:cNS=2.0,fsr_G2QQ_cNS_dn fsr:G2QQ:cNS=-2.0,fsr_G2QQ_cNS_up fsr:G2QQ:cNS=2.0,fsr_Q2QG_cNS_dn fsr:Q2QG:cNS=-2.0,fsr_Q2QG_cNS_up fsr:Q2QG:cNS=2.0,fsr_X2XG_cNS_dn fsr:X2XG:cNS=-2.0,fsr_X2XG_cNS_up fsr:X2XG:cNS=2.0,isr_G2GG_muR_dn isr:G2GG:muRfac=0.5,isr_G2GG_muR_up isr:G2GG:muRfac=2.0,isr_G2QQ_muR_dn isr:G2QQ:muRfac=0.5,isr_G2QQ_muR_up isr:G2QQ:muRfac=2.0,isr_Q2QG_muR_dn isr:Q2QG:muRfac=0.5,isr_Q2QG_muR_up isr:Q2QG:muRfac=2.0,isr_X2XG_muR_dn isr:X2XG:muRfac=0.5,isr_X2XG_muR_up isr:X2XG:muRfac=2.0,isr_G2GG_cNS_dn isr:G2GG:cNS=-2.0,isr_G2GG_cNS_up isr:G2GG:cNS=2.0,isr_G2QQ_cNS_dn isr:G2QQ:cNS=-2.0,isr_G2QQ_cNS_up isr:G2QQ:cNS=2.0,isr_Q2QG_cNS_dn isr:Q2QG:cNS=-2.0,isr_Q2QG_cNS_up isr:Q2QG:cNS=2.0,isr_X2XG_cNS_dn isr:X2XG:cNS=-2.0,isr_X2XG_cNS_up isr:X2XG:cNS=2.0}', 
            'UncertaintyBands:nFlavQ = 4', 
            'UncertaintyBands:MPIshowers = on', 
            'UncertaintyBands:overSampleFSR = 10.0', 
            'UncertaintyBands:overSampleISR = 10.0', 
            'UncertaintyBands:FSRpTmin2Fac = 20', 
            'UncertaintyBands:ISRpTmin2Fac = 1'
        ),
        pythia8PowhegEmissionVetoSettings = cms.vstring(
            'POWHEG:veto = 1', 
            'POWHEG:pTdef = 1', 
            'POWHEG:emitted = 0', 
            'POWHEG:pTemt = 0', 
            'POWHEG:pThard = 0', 
            'POWHEG:vetoCount = 100', 
            'SpaceShower:pTmaxMatch = 2', 
            'TimeShower:pTmaxMatch = 2'
        )
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc700/13TeV/powheg/Vj_NNLOPS/Zj_slc6_amd64_gcc700_CMSSW_10_2_23_ZJToMuMu-suggested-nnpdf31-ncalls-doublefsr-q139-powheg-MiNNLO31-svn3756-ew-rwl5-j200-st2fix-ana-hoppetweights-norwl.tgz'),
    generateConcurrently = cms.untracked.bool(True),
    nEvents = cms.untracked.uint32(20),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.recosim_step = cms.Path(process.recosim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.recosim_step,process.endjob_step,process.AODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(2)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path).insert(0, process.ProductionFilterSequence)

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

process.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.DeltaIntersection=1e-6
#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
