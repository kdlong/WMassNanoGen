# Setup to run NanoGen with default weights

```
cmsrel CMSSW_11_2_0_pre7
cd CMSSW_11_0_0_pre7/src
cmsenv
# The following merge is not strictly necessary, but it enables a bit of functionality
git cms-init
git cms-merge-topic kdlong:NanoGen_dqm
scram b -j 5

mkdir Configuration
cd Configuration
git clone git@github.com:kdlong/WMassNanoGen.git #or just create your fragment in a <name>/python subfolder
scram b
```


# Setup to store all genWeights

```
cmsrel CMSSW_10_6_18
cd CMSSW_10_6_18/src
cmsenv
git cms-init
git cms-merge-topic kdlong:NanoGenWeights_10_6_18
scram b -j 5

mkdir Configuration
cd Configuration
git clone git@github.com:kdlong/WMassNanoGen.git
scram b
```

# Making configs and running
First create a config fragment in python/<your config>. Follow the other examples there

generate the config for NanoGen with cmsDriver. If you want gridpack --> NanoGen, you can use the script [runCmsDriverNanoGen.sh](runCmsDriverNanoGen.sh). To generate a full config from your fragment and run:

```
scram b
runCmsDriverNanoGen.sh <fragmentName_cff.py> <outputFile.root>
cmsRun fragmentName_cfg.py
```

An example to generate NanoGen from a MiniAOD file (useful to keep more gen particles or more LHE weights) is in [runCmsDriverGenericMiniToNanoGen.sh](runCmsDriverGenericMiniToNanoGen.sh).


```
scram b
cmsDriverZJMiNNLONanoGen.sh
cmsRun fragmentName_cfg.py
```

Example crab submit files are in the crab_submit_files directory. Note that you need to copy the gridpacks to a location readable from crab for this to work.
