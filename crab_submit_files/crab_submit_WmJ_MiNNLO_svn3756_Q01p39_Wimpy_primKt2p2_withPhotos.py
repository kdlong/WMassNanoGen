from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'WminusJToMuNu_svn3756_Q01p39_WimpyPrimKt2p2_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos_scaleWeights'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/WmJ_MiNNLO_svn3756_Q01p39_Wimpy_PrimKt2p2_Photos_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = 'WminusJToMuNu_svn3756_Q01p39_WimpyPrimKt2p2_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 800
NJOBS = 4000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/cmst3/user/kelong/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_CH_CERN'
