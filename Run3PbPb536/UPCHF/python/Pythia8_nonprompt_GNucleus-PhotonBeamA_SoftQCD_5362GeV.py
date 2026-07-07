import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8PhotonFluxSettings_cfi import PhotonFlux_PbPb


generator = cms.EDFilter("Pythia8ConcurrentGeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(5362.),
    PhotonFlux = PhotonFlux_PbPb,
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        processParameters = cms.vstring('SoftQCD:all = on',
                                        'PhaseSpace:pTHatMin = 0.',
                                        'PhotonParton:all = on',
                                        'MultipartonInteractions:pT0Ref = 3.0',
                                        'PDF:beamA2gamma = on',# have the photon coming from beam A
                                        'PDF:proton2gammaSet = 0',
                                        'PDF:pSetB = LHAPDF6:EPPS21nlo_CT18Anlo_Pb208', # add nuclear modifications to beam B
                                        'PDF:gammaFluxApprox2bMin = 13.272',
                                        'PDF:beam2gammaApprox = 2',
                                        'Photon:sampleQ2 = off'
                                    ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'processParameters')
    )
)




partonfilter = cms.EDFilter("PythiaFilter",
                                    ParticleID = cms.untracked.int32(5) #non-prompt
                                    )

ProductionFilterSequence = cms.Sequence(generator*partonfilter)
