# Setup to store all genWeights

```
cmsrel CMSSW_11_1_0_pre2
cd CMSSW_11_1_0_pre2/src
cmsenv
git cms-init
git cms-merge-topic kdlong:NanoGenExpandedWeights_11_1_0_pre2
scram b

cd Configuration
git clone 
scram b
```

# Setup to run NanoGen with default weights

```
cmsrel CMSSW_11_0_2
cd CMSSW_11_0_2/src
cmsenv
git cms-init
git cms-merge-topic kdlong:NanoGen_11_0_2
scram b

cd Configuration
git clone 
scram b
```

# Making configs and running
First create a config fragment in python/<your config>. Follow the other examples there

generate the config for NanoGen with cmsDriver. If you want gridpack --> NanoGen, you can use the script runCmsDriverNanoGen.sh

```
scram b
runCmsDriverNanoGen.sh <fragmentName_cff.py> <outputFile.root>
cmsRun fragmentName_cfg.py
```

Example crab submit files are in the crab_submit_files directory. Note that you need to copy the gridpacks to a location readable from crab for this to work.
