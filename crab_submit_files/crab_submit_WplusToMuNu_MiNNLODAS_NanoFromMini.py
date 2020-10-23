from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'WplusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 4
config.JobType.maxMemoryMB = 8000
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs/SMP-RunIISummer16NanoAODv7-00336_1_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/WplusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM'
config.Data.allowNonValidInputDataset = True

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 4
config.Data.outLFNDirBase = '/store/group/cmst3/group/wmass/w-mass-13TeV/NanoAOD' 
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoAODv7'

config.Site.storageSite = 'T2_CH_CERN'
