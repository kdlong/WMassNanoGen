from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ZJToMuMu_svn3756_DoubleFSR_DipolePrimKt2p5_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/ZJ_MiNNLO_svn3756_widthRunning_DoubleFSR_DipolePrimKt2p5_Photos_cfg.py'

config.Data.outputPrimaryDataset = 'ZJToMuMu_svn3756_DoubleFSR_DipolePrimKt2p5_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 2500
NJOBS = 2000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/kelong/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_CH_CERN'
