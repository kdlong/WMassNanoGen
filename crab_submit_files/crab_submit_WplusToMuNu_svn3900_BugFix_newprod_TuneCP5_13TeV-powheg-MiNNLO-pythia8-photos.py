from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'WplusToMuNu_svn3900_newprod_BugFix_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 4
config.JobType.maxMemoryMB = 2000*4
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/WplusJetsToMuNu_svn3900_BugFix_newprod_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = 'WplusToMuNu_svn3900_newprod_BugFix_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 2000
NJOBS = 5000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/cmst3/group/wmass/w-mass-13TeV/NanoGen/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_CH_CERN'
