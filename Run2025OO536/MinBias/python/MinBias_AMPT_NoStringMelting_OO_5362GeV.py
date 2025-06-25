import FWCore.ParameterSet.Config as cms
from GeneratorInterface.Core.ExternalGeneratorFilter import ExternalGeneratorFilter
# https://github.com/cms-sw/cmssw/blob/master/GeneratorInterface/AMPTInterface/python/amptDefaultParameters_cff.py
from GeneratorInterface.AMPTInterface.amptDefaultParameters_cff import *
amptNoMelting = amptDefaultParameters.clone()
amptNoMelting.ntmax = cms.int32(1000)
amptNoMelting.amptmode = cms.int32(1) # no melting
# LHC suggestion in v1.26t9b-v2.26t9b https://myweb.ecu.edu/linz/ampt/
amptNoMelting.stringFragA = cms.double(0.3)
amptNoMelting.stringFragB = cms.double(0.15)
amptNoMelting.alpha = cms.double(0.47140452)
amptNoMelting.mu = cms.double(3.2264)

generator = ExternalGeneratorFilter(
    cms.EDFilter("AMPTGeneratorFilter",
                 amptNoMelting,
                 firstEvent = cms.untracked.uint32(1),
                 firstRun = cms.untracked.uint32(1),
                 comEnergy = cms.double(5362.0),
                 frame = cms.string('CMS'),                         
                 proj = cms.string('A'),
                 targ = cms.string('A'),
                 iap  = cms.int32(16),
                 izp  = cms.int32(8),
                 iat  = cms.int32(16),
                 izt  = cms.int32(8),
                 bMin = cms.double(0),
                 bMax = cms.double(15)
    )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: $'),
    name = cms.untracked.string('$Source: $'),
    annotation = cms.untracked.string('AMPT OO 5362 GeV Minimum Bias')
)
