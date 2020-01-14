import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *
# from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

# https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/BPH-RunIIFall17GS-00115/0

generator = cms.EDFilter("Pythia8GeneratorFilter",
	comEnergy = cms.double(5020.0),
	crossSection = cms.untracked.double(54000000000),
	filterEfficiency = cms.untracked.double(3.0e-4),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaPylistVerbosity = cms.untracked.int32(0),
	ExternalDecays = cms.PSet(
		EvtGen130 = cms.untracked.PSet(
			decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'), # diff w/o NOLONGLIFE
			# particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
			particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'), # after (including) CMSSW_9_4_12
			user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Bd_JpsiKstar_mumuKpi.dec'),
			list_forced_decays = cms.vstring('MyB0','Myanti-B0'),
			operates_on_particles = cms.vint32()
		),
        parameterSets = cms.vstring('EvtGen130')
	),
	PythiaParameters = cms.PSet(
		pythia8CommonSettingsBlock,
		pythia8CP5SettingsBlock,
        # pythia8PSweightsSettingsBlock,
		processParameters = cms.vstring(            
			'HardQCD:all = on',
			'PhaseSpace:pTHatMin = 4.',					 
			'PhaseSpace:bias2Selection = on',
            'PhaseSpace:bias2SelectionPow = 3.',
            'PhaseSpace:bias2SelectionRef = 1.'
		),
        parameterSets = cms.vstring(
			'pythia8CommonSettings',
			'pythia8CP5Settings',
            # 'pythia8PSweightsSettings',
			'processParameters',
		)
	)
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

###########
# Filters #
###########
mumugenfilter = cms.EDFilter("MCParticlePairFilter",
							 Status = cms.untracked.vint32(1, 1),
							 MinPt = cms.untracked.vdouble(0.5, 0.5),
							 MinP = cms.untracked.vdouble(0., 0.),
							 MaxEta = cms.untracked.vdouble(10000., 10000.),
							 MinEta = cms.untracked.vdouble(-10000., -10000.),
							 MinInvMass = cms.untracked.double(2.0),
							 MaxInvMass = cms.untracked.double(4.0),
							 ParticleCharge = cms.untracked.int32(-1),
							 ParticleID1 = cms.untracked.vint32(13),
							 ParticleID2 = cms.untracked.vint32(13)
)

BJpsiDaufilter = cms.EDFilter("PythiaMomDauFilter",
							  ParticleID = cms.untracked.int32(511),
							  MomMinPt = cms.untracked.double(4.),
							  MomMinEta = cms.untracked.double(-10000.),
							  MomMaxEta = cms.untracked.double(10000.),
							  DaughterIDs = cms.untracked.vint32(443, 313),
							  NumberDaughters = cms.untracked.int32(2),
							  DaughterID = cms.untracked.int32(443),
							  DescendantsIDs = cms.untracked.vint32(13, -13),
							  NumberDescendants = cms.untracked.int32(2),
							  MinEta = cms.untracked.double(-10000.),
							  MaxEta = cms.untracked.double(10000.),
)

BKstarDaufilter = cms.EDFilter("PythiaMomDauFilter",
							 ParticleID = cms.untracked.int32(511),
							 MomMinPt = cms.untracked.double(4.),
							 MomMinEta = cms.untracked.double(-10000.),
							 MomMaxEta = cms.untracked.double(10000.),
							 DaughterIDs = cms.untracked.vint32(443, 313),
							 NumberDaughters = cms.untracked.int32(2),
							 DaughterID = cms.untracked.int32(313),
							 DescendantsIDs = cms.untracked.vint32(321, -211),
							 NumberDescendants = cms.untracked.int32(2),
							 MinEta = cms.untracked.double(-10000.),
							 MaxEta = cms.untracked.double(10000.),
)

ProductionFilterSequence = cms.Sequence(generator*mumugenfilter*BJpsiDaufilter*BKstarDaufilter)
