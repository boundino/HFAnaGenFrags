import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *
from Configuration.Generator.Pythia8PhotonFluxSettings_cfi import PhotonFlux_PbPb


generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(5362.),
    PhotonFlux = PhotonFlux_PbPb,
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2020_NOLONGLIFE.DEC'),
            operates_on_particles = cms.vint32(),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2020.pdl'),
            convertPythiaCodes = cms.untracked.bool(False),
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        processParameters = cms.vstring('SoftQCD:all = on',
                                        'PhaseSpace:pTHatMin = 0.',
                                        'PhotonParton:all = on',
                                        'MultipartonInteractions:pT0Ref = 3.0',
                                        'PDF:beamB2gamma = on', # have the photon coming from beam B
                                        'PDF:proton2gammaSet = 0',
                                        'PDF:pSet = LHAPDF6:EPPS21nlo_CT18Anlo_Pb208', # add nuclear modifications to beam A
                                        'PDF:gammaFluxApprox2bMin = 13.272',
                                        'PDF:beam2gammaApprox = 2',
                                        'Photon:sampleQ2 = off'
                                    ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'processParameters')
    )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)
# Bypass concurrency check
"_generator=cms.EDFilter fromGeneratorInterface.Core.ExternalGeneratorFilterimportExternalGeneratorFilter generator=ExternalGeneratorFilter(_generator)"

partonfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(5) # nonprompt
)

ProductionFilterSequence = cms.Sequence(generator*partonfilter)
