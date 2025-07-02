import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8ConcurrentGeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(9617.),
    HeavyIonInitialState = cms.PSet( ),
    PythiaParameters = cms.PSet(
        processParameters = cms.vstring(
            'Beams:idA = 1000080160',
            'Beams:idB = 2212',
            'Beams:frameType = 2',
            'Beams:eA = 3400',
            'Beams:eB = 6800',
            
            # MinBias events
            'SoftQCD:inelastic = on',
            
            # HI Angatyr setup https://pythia.org/latest-manual/HeavyIons.html
            'HeavyIon:mode = 1',
            # HeavyIon fitting of SubCollisionModel to cross sections
            'HeavyIon:SigFitNGen = 0',
            'HeavyIon:SigFitDefPar = 2.23,17.27,0.30',
            
            # Harmonic Oscillator Shell model (light ion geometry)
            'Angantyr:NucleusModelA = 3',

            #Forward tune (https://arxiv.org/pdf/2309.08604)
            'BeamRemnants:dampPopcorn=0',
            'BeamRemnants:hardRemnantBaryon=on',
            'BeamRemnants:aRemnantBaryon=0.36',
            'BeamRemnants:bRemnantBaryon=1.69',
            'BeamRemnants:primordialKTsoft=0.58',
            'BeamRemnants:primordialKThard=1.8',
            'BeamRemnants:halfScaleForKT=10',
            'BeamRemnants:halfMassForKT=1',
            'BeamRemnants:primordialKTremnant=0.58',
        ),
        parameterSets = cms.vstring('processParameters')
    )
)
