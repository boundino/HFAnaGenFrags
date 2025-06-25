import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8ConcurrentGeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(5362.),
    PythiaParameters = cms.PSet(
        processParameters = cms.vstring(
            'Beams:idA = 1000080160',
            'Beams:idB = 1000080160',
            'Beams:frameType = 1',
            'Beams:eCM = 5362.',
            
            # MinBias events
            'SoftQCD:inelastic = on',
            
            # HI Angatyr setup https://pythia.org/latest-manual/HeavyIons.html
            'HeavyIon:mode = 1',
            
            # Harmonic Oscillator Shell model (light ion geometry)
            'Angantyr:NucleusModelA = 3',
            'Angantyr:NucleusModelB = 3',
        ),
        parameterSets = cms.vstring('processParameters')
    )
)
