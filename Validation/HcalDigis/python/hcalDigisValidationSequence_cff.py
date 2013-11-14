import FWCore.ParameterSet.Config as cms

from Validation.HcalDigis.HcalDigisParam_cfi import *
import Validation.HcalDigis.HcalDigisParam_cfi
from Validation.HcalDigis.hcalDigiAnalyzer_cfi import *
AllHcalDigisValidation = Validation.HcalDigis.HcalDigisParam_cfi.hcaldigisAnalyzer.clone()
hcaldigisValidationSequence = cms.Sequence(hcalDigiAnalyzer)

# the folowing one is a twin of the above and is kept for back compatibility 
# with some old Validation/Configuration/python  sequences... 
hcalDigisValidationSequence = cms.Sequence(hcalDigiAnalyzer)



