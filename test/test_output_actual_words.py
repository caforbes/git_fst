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
    
    def test_singleWord(self):
        upper, lower = ("gwil$a+N", "gwila")
        generated = self.fst.generate(upper)
        self.assertEqual(len(generated), 1)
        analyzed = self.fst.analyze(lower)
        self.assertEqual(len(analyzed), 1)
    
    def test_polysemousWord(self):
        upper, lower = ("h$ix+VI", "hix")
        generated = self.fst.generate(upper)
        self.assertEqual(len(generated), 1)
        analyzed = self.fst.analyze(lower)
        self.assertEqual(len(analyzed), 2) # VI and N
    
    def test_multiWordConcat(self):
        upper, lower = ("'amg$iikw+N", "amgiikw")
        generated = self.fst.generate(upper)
        self.assertEqual(len(generated), 1)
        analyzed = self.fst.analyze(lower)
        self.assertEqual(len(analyzed), 1)
    
    def test_multiWordApostr(self):
        upper, lower = ("'wii'am$e+VI", "'wii'ame")
        generated = self.fst.generate(upper)
        self.assertEqual(len(generated), 1)
        analyzed = self.fst.analyze(lower)
        self.assertEqual(len(analyzed), 1)
    
    def test_bats_bigT_bare(self):
        root = "b$atsT"
        bare_result = self.fst.generate(root+'+VT')

        self.assertNotEqual(len(bare_result), 0)
        self.assertIn("bats(t)", bare_result)
    
    def test_bats_bigT_paths(self):
        root = "b$atsT"
        # path should exist
        paths = [
            '+VT-3.II',
            '+VT-TR-3.II',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertNotEqual(len(self.fst.generate(root+path)), 0)
        # path should not exist
        paths = [
            '+VT-T-3.II',
            '+VT-T-TR-3.II',
        ]
        for path in paths:
            with self.subTest(path='no '+path):
                self.assertEqual(len(self.fst.generate(root+path)), 0)

    def test_tahl_PLbigT_bare(self):
        root = "t'$ahlT"
        bare_result = self.fst.generate(root+'+VT')

        self.assertNotEqual(len(bare_result), 0)
        self.assertIn("t'ahl(t)", bare_result)

    def test_tahl_PLbigT_paths(self):
        root = "t'$ahlT"
        # path should exist
        paths = [
            '+VT-3.II',
            '+VT-TR-3.II',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertNotEqual(len(self.fst.generate(root+path)), 0)
        # path should not exist
        paths = [
            '+VT-T-3.II',
            '+VT-T-TR-3.II',
        ]
        for path in paths:
            with self.subTest(path='no '+path):
                self.assertEqual(len(self.fst.generate(root+path)), 0)
    
    def test_noFreeModal(self):
        result = self.fst.generate('+MOD')
        self.assertEqual(result, [])
        result = self.fst.generate('+MOD=3.I')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
