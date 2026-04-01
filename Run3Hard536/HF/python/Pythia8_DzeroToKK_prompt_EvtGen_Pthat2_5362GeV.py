import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
# from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(5362.),
                         ExternalDecays = cms.PSet(
                             EvtGen130 = cms.untracked.PSet(
                                 decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
                                 operates_on_particles = cms.vint32(),
                                 particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
                                 list_forced_decays = cms.vstring('myD0', 'myanti-D0'),
                                 user_decay_embedded = cms.vstring(
                                     """
                                     Alias myD0      D0
                                     Alias myanti-D0 anti-D0
                                     ChargeConj myanti-D0 myD0

                                     Decay myD0
                                     1.000   K- K+  PHSP;
                                     Enddecay
                                     CDecay myanti-D0
                                     
                                     End
                                     """
                                 ),
                                 convertPythiaCodes = cms.untracked.bool(False),
                             ),
                             parameterSets = cms.vstring('EvtGen130')
                         ),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CP5SettingsBlock,
                             processParameters = cms.vstring(
                                 'HardQCD:all = on',
                                 'PhaseSpace:pTHatMin = 2.',
                             ),
                             parameterSets = cms.vstring(
                                 'pythia8CommonSettings',
                                 'pythia8CP5Settings',
                                 'processParameters'
                             )
                         )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)
#Bypass concurrency check
"_generator=cms.EDFilter fromGeneratorInterface.Core.ExternalGeneratorFilterimportExternalGeneratorFilter generator=ExternalGeneratorFilter(_generator)"


partonfilter = cms.EDFilter("PythiaFilter",
                            ParticleID = cms.untracked.int32(4) # prompt
)

D0Daufilter = cms.EDFilter("PythiaMomDauFilter",
                           ParticleID = cms.untracked.int32(421),
                           MomMinPt = cms.untracked.double(0.),
                           MomMinEta = cms.untracked.double(-10),
                           MomMaxEta = cms.untracked.double(10),
                           DaughterIDs = cms.untracked.vint32(-321, 321),
                           NumberDaughters = cms.untracked.int32(2),
                           NumberDescendants = cms.untracked.int32(0),
)

ProductionFilterSequence = cms.Sequence(generator*partonfilter*D0Daufilter)
