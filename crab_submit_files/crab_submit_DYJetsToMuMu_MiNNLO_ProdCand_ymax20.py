from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_ymax20grids'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/SMP-RunIISummer20UL16wmLHEGEN-00020_1_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = 'DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos_ymax20grids'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 400
NJOBS = 5000  # This is not a configuration parameter, but an auxiliary variable that we use in the nfailtest line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/cmst3/user/kelong/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer20UL16wmLHEGEN'

config.Site.storageSite = 'T2_CH_CERN'
