from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ZJToMuMu_mWPilot_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 4
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs/ZJToMuMu_mWPilot_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos_NanoGen.py'

config.Data.inputDataset = '/ZJToMuMu_mWPilot_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM'
config.Data.allowNonValidInputDataset = True

config.Data.splitting = 'Automatic'
config.Data.outLFNDirBase = '/store/user/kelong/' 
config.Data.publication = False
config.Data.outputDatasetTag = 'NanoGen'

config.Site.storageSite = 'T2_CH_CERN'
