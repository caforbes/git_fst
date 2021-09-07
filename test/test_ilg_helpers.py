import unittest

from src import ilg_helpers
from src.parser import Parser

"""
Tests helper functions having to do with conversion to and from
the abbreviations/format used in interlinear data (e.g. analyzed 
stories).
"""

class TestFSTtoStoryGloss(unittest.TestCase):
    def convert(self, fst_ver):
        return ilg_helpers.fst_to_story_gloss(fst_ver)

    def test_justLemma(self):
        fst_ver, expected = ('w$an+VI', '___')
        self.assertEqual(self.convert(fst_ver), expected)

    def test_Inflected(self):
        fst_ver, expected = ('w$an+VI-3.II', '___-3.II')
        self.assertEqual(self.convert(fst_ver), expected)

    def test_functionalInDict(self):
        fst_ver, expected = ('n$ee+AUX', 'NEG')
        self.assertEqual(self.convert(fst_ver), expected)

    def test_functionalInDictComplex(self):
        fst_ver, expected = ('n$ee+AUX=EPIS=CN', 'NEG=EPIS=CN')
        self.assertEqual(self.convert(fst_ver), expected)

    def test_looOblique(self):
        fst_ver, expected = ('2PL+OBL', 'OBL-2PL.II')
        self.assertEqual(self.convert(fst_ver), expected)

    def test_pronounIII(self):
        fst_ver, expected = ('3.III+PRO', '3.III')
        self.assertEqual(self.convert(fst_ver), expected)

    def test_demonstrative(self):
        fst_ver, expected = ('PN=PROX+DEM', 'PN=DEM.PROX')
        self.assertEqual(self.convert(fst_ver), expected)

    def test_demonstrativePl(self):
        fst_ver, expected = ('ASSOC=PROX+DEM', 'ASSOC=DEM.PROX')
        self.assertEqual(self.convert(fst_ver), expected)

    def test_quotative(self):
        fst_ver, expected = ('1SG+QUOT', '1.I=QUOT')
        self.assertEqual(self.convert(fst_ver), expected)

    def test_quotativeThirdPl(self):
        fst_ver, expected = ('3PL+QUOT-3PL.INDP', '3.I=QUOT.3PL-3PL.INDP')
        self.assertEqual(self.convert(fst_ver), expected)

class TestAnalysisMatching(unittest.TestCase):
    
    def test_scoreSimpleMatch(self):
        inputs = ('NEG', 'NEG')
        self.assertEqual(ilg_helpers.match_score(*inputs), 1)
    
    def test_scoreBadMatch(self):
        inputs = ('X', 'NEG')
        self.assertEqual(ilg_helpers.match_score(*inputs), 0)
    
    def test_scoreBadPrefix(self):
        inputs = ('1=___', 'test')
        self.assertEqual(ilg_helpers.match_score(*inputs), 0)
    
    def test_scoreBadSuffix(self):
        inputs = ('___-3', 'test')
        self.assertEqual(ilg_helpers.match_score(*inputs), 0)
    
    def test_scoreMaybePrefix(self):
        inputs = ('1=___', '1=test')
        self.assertLess(ilg_helpers.match_score(*inputs), 1)
        self.assertGreater(ilg_helpers.match_score(*inputs), 0)
    
    def test_scoreMaybeSuffix(self):
        inputs = ('___-3', 'test-3')
        self.assertLess(ilg_helpers.match_score(*inputs), 1)
        self.assertGreater(ilg_helpers.match_score(*inputs), 0)
    
    def test_scoreMaybeElaborateStem(self):
        inputs = ('___-3', 'CAUS-test-VAL-3')
        self.assertLess(ilg_helpers.match_score(*inputs), 1)
        self.assertGreater(ilg_helpers.match_score(*inputs), 0)
    
    def test_scoreGoodHiddenTr(self):
        inputs = ('___-TR-3PL.II', 'test[-TR]-3PL.II')
        self.assertLess(ilg_helpers.match_score(*inputs), 1)
        self.assertGreater(ilg_helpers.match_score(*inputs), 0)

    def test_scoreHiddenTrButBad(self):
        inputs = ('___-TR-2PL.II', 'test[-TR]-3PL.II')
        self.assertEqual(ilg_helpers.match_score(*inputs), 0)
    
    def test_scoreMaybeExtraMorphemes(self):
        # e.g. da'ak_hlxw with annotated "able[-3]((=CN))"
        inputs = ('___', 'test[-3]((=CN))')
        self.assertLess(ilg_helpers.match_score(*inputs), 1)
        self.assertGreater(ilg_helpers.match_score(*inputs), 0)

    def test_filterAnalysesExact(self):
        input_analyses = ['n$ee+AUX']
        input_gloss = 'NEG'
        res = ilg_helpers.filter_matching_glosses(input_analyses, input_gloss)
        self.assertEqual(res, [('n$ee+AUX', 1)])

    def test_filterAnalysesReduceRoot(self):
        input_analyses = ['n$ee+AUX', 'n$ee+VI']
        input_gloss = 'NEG'
        res = ilg_helpers.filter_matching_glosses(input_analyses, input_gloss)
        self.assertEqual(res, [('n$ee+AUX', 1)])

    def test_filterAnalysesReduceMorpheme(self):
        input_analyses = ['n$ee+AUX', 'n$ee+AUX-3.II']
        input_gloss = 'NEG'
        res = ilg_helpers.filter_matching_glosses(input_analyses, input_gloss)
        self.assertEqual(res, [('n$ee+AUX', 1)])

    def test_filterAnalysesEmpty(self):
        input_analyses = []
        input_gloss = 'NEG'
        res = ilg_helpers.filter_matching_glosses(input_analyses, input_gloss)
        self.assertEqual(res, [])

    def test_filterAnalysesNoMatch(self):
        input_analyses = ['n$ee+AUX-3.II']
        input_gloss = 'PROG'
        res = ilg_helpers.filter_matching_glosses(input_analyses, input_gloss)
        self.assertEqual(res, [])

    def test_filterAnalysesSupersetGloss(self):
        input_analyses = ['n$ee+AUX-3.II']
        input_gloss = 'NEG'
        res = ilg_helpers.filter_matching_glosses(input_analyses, input_gloss)
        self.assertEqual(res, [])

    def test_filterAnalysesSubsetGloss(self):
        input_analyses = ["'$am+VI[-3.II]=CN", "'$am+VI=CN"]
        input_gloss = 'good[-3.II]=CN'
        res = ilg_helpers.filter_matching_glosses(input_analyses, input_gloss)
        self.assertEqual(
            res, [("'$am+VI[-3.II]=CN", 0.628), ("'$am+VI=CN", 0.546)])
    # add tests to do with option sort?
