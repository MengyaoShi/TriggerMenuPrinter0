import FWCore.ParameterSet.Config as cms

process = cms.Process("TRIGGERANALYZER")

process.load("FWCore.MessageService.MessageLogger_cfi")

#stuff you need for the trigger for some unknown reason
process.load('Configuration/StandardSequences/Services_cff')
process.load('Configuration/StandardSequences/EndOfProcess_cff')

#global tag: needed for trigger stuff
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string('MCRUN2_74_V9::All')

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'root://eoscms//eos/cms/store/user/mshi/step_3/RECO_test_3_999.root'
    )
                            )
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.load('BBA/TriggerAnalyzer/triggeranalyzer_cfi')
process.TriggerAnalyzer.outputFile = cms.untracked.string(
    'dummy.root'
    )
process.TriggerAnalyzer.unprescaledHLTPaths = cms.untracked.vstring('HLT_BTagMu_DiJet20_Mu5_v2')

process.p = cms.Path(process.TriggerAnalyzer)


