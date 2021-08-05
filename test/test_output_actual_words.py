import unittest
from test import TestFSTOutput, FULL_E

"""
This suite checks that certain gitksan words are correctly imported
from the given CSV dictionary, and are parsed accurately.
"""

class TestLexiconImport(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        super().setUpClass(FULL_E, None)
    
    def test_anyWord(self):
        root = "y$al+VI"
        result = self.fst.generate(root)
        self.assertNotEqual(len(result), 0)
    
    
    def test_multiWordConcat(self):
        root = "'amg$iikw+N"
        result = self.fst.generate(root)
        self.assertNotEqual(len(result), 0)
    
    def test_multiWordApostr(self):
        root = "lax_'am$aaxws+N"
        result = self.fst.generate(root)
        self.assertNotEqual(len(result), 0)
    
    def test_bats_bigT(self):
        root = "b$atsT"
        self.assertNotEqual(len(self.fst.generate(root+'+VT')), 0)

        # path should exist
        paths = [
            '+VT-3',
            '+VT-TR-3',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertNotEqual(len(self.fst.generate(root+path)), 0)
        
        # path should not exist
        paths = [
            '+VT-T-3',
            '+VT-T-TR-3',
        ]
        for path in paths:
            with self.subTest(path='no '+path):
                self.assertEqual(len(self.fst.generate(root+path)), 0)

    def test_tahl_bigT(self):
        root = "t'$ahlT"
        self.assertNotEqual(len(self.fst.generate(root+'+VT')), 0)

        paths = [
            '+VT-3',
            '+VT-TR-3',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertNotEqual(len(self.fst.generate(root+path)), 0)

        # path should not exist
        paths = [
            '+VT-T-3',
            '+VT-T-TR-3',
        ]
        for path in paths:
            with self.subTest(path='no '+path):
                self.assertEqual(len(self.fst.generate(root+path)), 0)


if __name__ == '__main__':
    unittest.main()
