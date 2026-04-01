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

D0filter = cms.EDFilter("PythiaFilter",
                        ParticleID = cms.untracked.int32(421)
)

ProductionFilterSequence = cms.Sequence(generator*partonfilter*D0filter)
