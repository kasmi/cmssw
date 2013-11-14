import FWCore.ParameterSet.Config as cms

hcalDigiAnalyzer = cms.EDAnalyzer("HcalDigisValidation",
    outputFile                = cms.untracked.string('HcalDigisValidationRelVal.root'),
#    digiLabel                = cms.InputTag("simHcalDigis"),
#    subdetector               = cms.untracked.string('HE'),

#### for 2017 data sets
    HBHEDigisCollectionLabel = cms.InputTag("simHcalDigis"),
    HFDigisCollectionLabel   = cms.InputTag("simHcalDigis"),
    HODigisCollectionLabel   = cms.InputTag("simHcalDigis"),
#### for 2019 data sets
#    HBHEDigisCollectionLabel = cms.InputTag("simHcalDigis","HBHEUpgradeDigiCollection"),
#    HFDigisCollectionLabel   = cms.InputTag("simHcalDigis","HFUpgradeDigiCollection"),
#    HODigisCollectionLabel   = cms.InputTag("simHcalDigis"),

    zside                     = cms.untracked.string('*'),
    mode                      = cms.untracked.string('multi'),
    hcalselector              = cms.untracked.string('all'),
    mc                        = cms.untracked.string('yes'), # 'yes' for MC
    doSLHC                    = cms.untracked.bool(False) #  False for SLHC and True for regular rel val 
)
