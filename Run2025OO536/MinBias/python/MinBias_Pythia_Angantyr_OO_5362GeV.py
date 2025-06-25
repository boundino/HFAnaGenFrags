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
            'Beams:eCM = 5362',
            
            # MinBias events
            'SoftQCD:inelastic = on',
            
            # HI Angatyr setup (https://www.pythia.org/latest-manual/htmldoc/examples/main422.html)
            'HeavyIon:mode = 1',
            'HeavyIon:SigFitErr = 0.02,0.02,0.1,0.05,0.05,0.0,0.1,0.0',
            'HeavyIon:SigFitNGen = 20',
            'HeavyIon:SigFitDefPar = 2.15,17.24,0.33',
            
            # Harmonic Oscillator Shell model (light ion geometry)
            'Angantyr:NucleusModelA = 3',
            'Angantyr:NucleusModelB = 3',
        ),
        parameterSets = cms.vstring('processParameters')
    )
)
