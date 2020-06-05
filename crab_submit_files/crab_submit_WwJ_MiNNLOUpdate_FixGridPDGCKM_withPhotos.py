from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'WminusJToMuNu_AuthorsUpdate_GridFixPDGCKM_13TeV-powheg-MiNNLO-pythia8-photos'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/WmJ_MiNNLOUpdate_FixGridPDGCKM_withPhotos.py'

config.Data.outputPrimaryDataset = 'WminusJToMuNu_AuthorsUpdate_GridFixPDGCKM_13TeV-powheg-MiNNLO-pythia8-photos'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 400
NJOBS = 10000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/kelong/'
config.Data.publication = False
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_CH_CERN'
