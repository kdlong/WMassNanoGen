from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ZJToMuMu_svn3756_ProductionCand_GeantFineStep_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos_ext1_NANO'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ZJ_MiNNLO_svn3756_MarkusFix_Q01p39_PrimKt2p2_noWeights_Photos_fullSim_NANOAOD_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 16000
config.JobType.maxJobRuntimeMin = 180

config.Data.inputDataset = '/ZJToMuMu_svn3756_ProductionCand_GeantFineStep_TuneCP5_13TeV-powheg-MiNNLO-pythia8-photos_ext1/kelong-RunIISummer20ULMINIAODSIM-a30f4833d72eaa68c8689dc0a0693102/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 50
config.Data.outLFNDirBase = '/store/group/cmst3/user/kelong/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer20ULNANOAODSIM'

config.Site.storageSite = 'T2_CH_CERN'
