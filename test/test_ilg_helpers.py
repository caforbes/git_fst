import unittest

from src import ilg_helpers
from src.parser import Parser

"""
Tests helper functions having to do with conversion to and from
the abbreviations/format used in interlinear data (e.g. analyzed 
stories).
"""

class TestFSTtoStoryGloss(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.stem_pat = Parser._stem_pat
    
    def convert(self, fst_ver):
        return ilg_helpers.fst_to_story_gloss(fst_ver, self.stem_pat)

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
        fst_ver, expected = ('1SG+QUOT', '1=QUOT')
        self.assertEqual(self.convert(fst_ver), expected)

    def test_quotativeThirdPl(self):
        fst_ver, expected = ('3PL+QUOT-3PL.INDP', '3=QUOT.3PL-3PL.INDP')
        self.assertEqual(self.convert(fst_ver), expected)
