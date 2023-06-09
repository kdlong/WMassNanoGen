import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/afs/cern.ch/work/m/mseidel/public/MiNNLO-gridpacks/slc6_amd64_gcc700_CMSSW_10_2_29_WminusToMuNu-13TeV-nnpdf31-winhac-born.tar.gz'),
    generateConcurrently = cms.untracked.bool(True),
    nEvents = cms.untracked.uint32(10000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'SpaceShower:pTmaxMatch = 2',
            'TimeShower:pTmaxMatch = 2',
            'ParticleDecays:allowPhotonRadiation = on',
            'TimeShower:QEDshowerByL = off',
            'TimeShower:QEDshowerByOther = off',
            'BeamRemnants:hardKTOnlyLHE = on',
            'BeamRemnants:primordialKThard = 2.225001',
            'SpaceShower:dipoleRecoil = 1'
        ),
		parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    #'pythia8PSweightsSettings',
                                    'processParameters')
    ),
	ExternalDecays = cms.PSet(
        Photospp = cms.untracked.PSet(
            parameterSets = cms.vstring("setExponentiation", "setInfraredCutOff", "setMeCorrectionWtForW", "setMeCorrectionWtForZ", "setMomentumConservationThreshold", "setPairEmission", "setPhotonEmission", "setStopAtCriticalError", "suppressAll", "forceBremForDecay"),
            setExponentiation = cms.bool(True),
            setMeCorrectionWtForW = cms.bool(True),
            setMeCorrectionWtForZ = cms.bool(True),
            setInfraredCutOff = cms.double(0.0000001),
            setMomentumConservationThreshold = cms.double(0.1),
            setPairEmission = cms.bool(False), # retain pair emission in MiNNLO(pair=true) x NLOEW(nopair) / this(nopair)
            setPhotonEmission = cms.bool(True),
            setStopAtCriticalError = cms.bool(False),
            # Use Photos only for W/Z decays
            suppressAll = cms.bool(True),
            forceBremForDecay = cms.PSet(
                parameterSets = cms.vstring("Z", "Wp", "Wm"),
                Z = cms.vint32(0, 23),
                Wp = cms.vint32(0, 24),
                Wm = cms.vint32(0, -24),
            ),
        ),
        parameterSets = cms.vstring("Photospp")
    )
)

ProductionFilterSequence = cms.Sequence(generator)
