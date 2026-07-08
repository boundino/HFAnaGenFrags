import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *
from Configuration.Generator.Pythia8PhotonFluxSettings_cfi import PhotonFlux_PbPb


generator = cms.EDFilter("Pythia8GeneratorFilter",
                         maxEventsToPrint = cms.untracked.int32(1), # print when event number = 0, so process.source.numberEventsInLuminosityBlock will affect it
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(5362.),
                         PhotonFlux = PhotonFlux_PbPb,
                         ExternalDecays = cms.PSet(
                             EvtGen130 = cms.untracked.PSet(
                                 decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2020.DEC'), # cannot use *_NOLONGLIFE.DEC with K_S0 decay
                                 # https://github.com/cms-data/GeneratorInterface-EvtGenInterface/blob/master/DECAY_2014_NOLONGLIFE.DEC#L6764
                                 operates_on_particles = cms.vint32(),
                                 particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2020.pdl'),
                                 user_decay_embedded= cms.vstring(
                                     """
Alias myLambdaC      Lambda_c+
Alias myanti-LambdaC anti-Lambda_c-
ChargeConj myanti-LambdaC myLambdaC
Decay myLambdaC
1.000   K_S0 p+  PHSP;
Enddecay
CDecay myanti-LambdaC
End
"""
                                 ),
                                 list_forced_decays = cms.vstring('myLambdaC', 'myanti-LambdaC'),
                                 convertPythiaCodes = cms.untracked.bool(False),
                             ),
                             parameterSets = cms.vstring('EvtGen130')
                         ),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             processParameters = cms.vstring(
                                 'HardQCD:all = on',
                                 'PhaseSpace:pTHatMin = 2.',
                                 'PhotonParton:all = on',
                                 'MultipartonInteractions:pT0Ref = 3.0',
                                 'PDF:beamA2gamma = on',# have the photon coming from beam B
                                 'PDF:proton2gammaSet = 0',
                                 'PDF:pSetB = LHAPDF6:EPPS21nlo_CT18Anlo_Pb208', # add nuclear modifications to beam A
                                 'PDF:gammaFluxApprox2bMin = 13.272',
                                 'PDF:beam2gammaApprox = 2',
                                 'Photon:sampleQ2 = off'
                             ),
                             parameterSets = cms.vstring('pythia8CommonSettings',
                                                         'processParameters')
                         )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)
#Bypass concurrency check
"_generator=cms.EDFilter fromGeneratorInterface.Core.ExternalGeneratorFilterimportExternalGeneratorFilter generator=ExternalGeneratorFilter(_generator)"


partonfilter = cms.EDFilter("PythiaFilter",
                            ParticleID = cms.untracked.int32(4) # prompt
)

LambdaCDaufilter = cms.EDFilter("PythiaMomDauFilter",
                                ParticleID = cms.untracked.int32(4122),
                                MomMinPt = cms.untracked.double(0.9),
                                MomMinEta = cms.untracked.double(-10),
                                MomMaxEta = cms.untracked.double(10),
                                DaughterIDs = cms.untracked.vint32(310, 2212),
                                NumberDaughters = cms.untracked.int32(2),
                                NumberDescendants = cms.untracked.int32(0)
)

ProductionFilterSequence = cms.Sequence(generator*partonfilter*LambdaCDaufilter)
