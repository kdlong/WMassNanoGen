from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ZToMuMu_AuthorsUpdate_LowCutoff_TuneCUETP8M1_13TeV-powheg-MiNNLO-pythia8-photos'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/ZJ_MiNNLO_lowCutoff_update2020_03_05_cfg.py'

config.Data.outputPrimaryDataset = 'ZToMuMu_AuthorsUpdate_LowCutoff_TuneCUETP8M1_13TeV-powheg-MiNNLO-pythia8-photos'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 2000
NJOBS = 4000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_CH_CERN'
