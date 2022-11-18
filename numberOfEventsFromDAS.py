import json
import subprocess

#datasets = [
#    "/DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM",
#    "/DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM",
#    "/DYJetsToTauTau_M-50_AtLeastOneEorMuDecay_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM",
#    "/DYJetsToTauTau_M-50_AtLeastOneEorMuDecay_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM",
#    "/WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM",
#    "/WminusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v1/MINIAODSIM",
#    "/WminusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM",
#    "/WminusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM",
#    "/WplusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM",
#    "/WplusJetsToMuNu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM",
#    "/WplusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM",
#    "/WplusJetsToTauNu_TauToMu_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM",
#	"/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIIFall17MiniAODv2-fixECALGT_LowPU_94X_mc2017_realistic_v10For2017H_v2-v1/MINIAODSIM",
#	"/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
#	"/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
#	"/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIIFall17MiniAODv2-fixECALGT_LowPU_94X_mc2017_realistic_v10For2017H_v2-v1/MINIAODSIM",
#	"/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
#	"/DYJetsToTauTau_M-50_AtLeastOneEorMuDecay_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
#	"/DYJetsToTauTau_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIIFall17MiniAODv2-fixECALGT_LowPU_94X_mc2017_realistic_v10For2017H_v2-v1/MINIAODSIM",
#    "/WminusJetsToENu_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIIFall17MiniAODv2-fixECALGT_LowPU_94X_mc2017_realistic_v10For2017H_v2-v1/MINIAODSIM",
#    "/WminusJetsToMuNu_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIIFall17MiniAODv2-fixECALGT_LowPU_94X_mc2017_realistic_v10For2017H_v2-v1/MINIAODSIM",
#    "/WminusJetsToTauNu_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIIFall17MiniAODv2-fixECALGT_LowPU_94X_mc2017_realistic_v10For2017H_v2-v1/MINIAODSIM",
#    "/WplusJetsToENu_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIIFall17MiniAODv2-fixECALGT_LowPU_94X_mc2017_realistic_v10For2017H_v2-v1/MINIAODSIM",
#    "/WplusJetsToMuNu_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIIFall17MiniAODv2-fixECALGT_LowPU_94X_mc2017_realistic_v10For2017H_v2-v1/MINIAODSIM",
#    "/WplusJetsToTauNu_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIIFall17MiniAODv2-fixECALGT_LowPU_94X_mc2017_realistic_v10For2017H_v2-v1/MINIAODSIM",
#]

datasets = [
    "/SingleMuon/Run2016B-21Feb2020_UL2016_HIPM_WMass-v2/MINIAOD",
    "/SingleMuon/Run2016C-21Feb2020_UL2016_HIPM_WMass-v1/MINIAOD",
    "/SingleMuon/Run2016D-21Feb2020_UL2016_HIPM_WMass-v1/MINIAOD",
    "/SingleMuon/Run2016E-21Feb2020_UL2016_HIPM_WMass-v1/MINIAOD",
    "/SingleMuon/Run2016F-21Feb2020_UL2016_HIPM_WMass-v1/MINIAOD",
    "/SingleMuon/Run2016F-21Feb2020_UL2016_WMass-v1/MINIAOD",
    "/SingleMuon/Run2016G-21Feb2020_UL2016_WMass-v1/MINIAOD",
    "/SingleMuon/Run2016H-21Feb2020_UL2016_WMass-v1/MINIAOD",
]

for dataset in datasets:
    info = subprocess.check_output([f'dasgoclient --query="dataset dataset={dataset}" --json'], shell=True)
    dasinfo = json.loads(info)
    print("numevents =", dasinfo[2][u"dataset"][0][u"nevents"], "for", dataset)

