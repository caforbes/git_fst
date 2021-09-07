import unittest
from test import TestFSTOutput, BASIC_E

"""
This suite checks the existence of expected morphotactic combinations
that attach to the major categories (N, VI, VT) in the base parser.
These tests use the actual FST (v1) as a dependency.
"""

class TestNounPaths(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': ['gwil$a']
        }
        super().setUpClass(BASIC_E, test_stems)
        cls.uppers = [pair[0] for pair in cls.fst.pairs()]

    def test_uniquePairs(self):
        pairs = self.fst.pairs()
        self.assertTrue(len(pairs) == len(set(pairs)))

    def test_numUniquePaths(self):
        expected = 11   # bare + 8 sII + ATTR + SX
        expected += 9   # VAL: 8 sII + SX
        expected += 8   # T: 8 sII
        self.assertEqual(len(set(self.uppers)), expected)

    def test_inclN(self):
        path = 'gwil$a+N'
        self.assertIn(path, self.uppers)

    def test_exclBare(self):
        path = 'gwil$a'
        self.assertNotIn(path, self.uppers)

    def test_inclSeriesIIandCons(self):
        paths = [
            'gwil$a+N-1SG.II',
            'gwil$a+N-1PL.II',
            'gwil$a+N-2SG.II',
            'gwil$a+N-2PL.II',
            'gwil$a+N-3.II',
            'gwil$a+N-3PL.II',
            'gwil$a+N[-3.II]=CN',
            'gwil$a+N[-3.II]=PN',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertIn(path, self.uppers)

    def test_inclAttr(self):
        path = 'gwil$a+N-ATTR'
        self.assertIn(path, self.uppers)
        self.assertTrue(self.uppers.count(path) == 2) # m and a

        endings = {form[-1] for form in self.fst.generate(path)}
        self.assertEqual(sorted(list(endings)), ['a', 'm'])

    def test_inclSX(self):
        path = 'gwil$a+N-SX'
        self.assertIn(path, self.uppers)

    def test_inclPossXW(self):
        path = 'gwil$a+N-VAL'
        self.assertNotIn(path, self.uppers)
        path = 'gwil$a+N-VAL'
        self.assertIn(path+'-3.II', self.uppers)

    def test_inclTposs(self):
        path = 'gwil$a+N-T-3.II'
        self.assertIn(path, self.uppers)
        path = 'gwil$a+N-T[-3.II]=CN'
        self.assertIn(path, self.uppers)
        path = 'gwil$a+N-T'
        self.assertNotIn(path, self.uppers)

    def test_exclTR(self):
        paths = [
            'gwil$a+N-TR',
            'gwil$a+N-TR-3.II',
            'gwil$a+VT-TR-3.II',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertNotIn(path, self.uppers)


class TestVerbIntransPaths(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'IntransitiveVerb': ['y$ee']
        }
        super().setUpClass(BASIC_E, test_stems)
        cls.pairs = cls.fst.pairs()
        cls.uppers = [pair[0] for pair in cls.pairs]

    def test_uniquePairs(self):
        self.assertTrue(len(self.pairs) == len(set(self.pairs)))

    def test_numUniquePaths(self):
        expected = 10 # bare, sII, -da
        expected += 2 # attr, sx
        # expected += 8 # caus + sII
        # expected += 8 # caus + tr + sII
        self.assertEqual(len(set(self.uppers)), expected)

    def test_inclVI(self):
        path = 'y$ee+VI'
        self.assertIn(path, self.uppers)

    def test_exclBare(self):
        path = 'y$ee'
        self.assertNotIn(path, self.uppers)

    def test_inclSeriesIIandCons(self):
        paths = [
            'y$ee+VI-1SG.II',
            'y$ee+VI-1PL.II',
            'y$ee+VI-2SG.II',
            'y$ee+VI-2PL.II',
            'y$ee+VI-3.II',
            'y$ee+VI-3PL.II',
            'y$ee+VI-3PL.INDP',
            'y$ee+VI[-3.II]=CN',
            'y$ee+VI[-3.II]=PN',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertIn(path, self.uppers)

    @unittest.skip("derivational morphemes no longer included")
    def test_inclCaus(self):
        stem = 'y$ee+VI'
        paths = [
            '-CAUS-1SG.II',
            '-CAUS[-3.II]=CN',
            '-CAUS-TR-1SG.II',
            '-CAUS-TR[-3.II]=CN',
        ]
        for path in paths:
            path = stem + path
            with self.subTest(path=path):
                self.assertIn(path, self.uppers)
        self.assertNotIn(stem + '-CAUS', self.uppers)

    def test_inclAttr(self):
        path = 'y$ee+VI-ATTR'
        self.assertIn(path, self.uppers)

    def test_inclSX(self):
        path = 'y$ee+VI-SX'
        self.assertIn(path, self.uppers)

    def test_exclXW(self):
        path = 'y$ee+VI-VAL'
        self.assertNotIn(path, self.uppers)

    def test_exclT(self):
        path = 'y$ee+VI-T-3.II'
        self.assertNotIn(path, self.uppers)
        path = 'y$ee+VI-T[-3.II]=CN'
        self.assertNotIn(path, self.uppers)

    def test_exclTR(self):
        paths = [
            'y$ee+VI-TR',
            'y$ee+VI-TR-3.II',
            'y$ee+VT-TR',
            'y$ee+VT-TR-3.II',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertNotIn(path, self.uppers)


class TestVerbTransPaths(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'TransitiveVerb': ['j$ap']
        }
        super().setUpClass(BASIC_E, test_stems)
        cls.pairs = cls.fst.pairs()
        cls.uppers = [pair[0] for pair in cls.pairs]

    def test_uniquePairs(self):
        self.assertTrue(len(self.pairs) == len(set(self.pairs)))

    def test_numUniquePaths(self):
        expected = 9    # bare + sII
        expected += 8    # TR: 8 sII
        expected += 16    # T: 8 sII + 8 TR/sII
        # expected += 11    # PASS: bare + 8 sII + ATTR + SX
        # expected += 11    # ANTIP: bare + 8 sII + ATTR + SX
        self.assertEqual(len(set(self.uppers)), expected)

    def test_inclVT(self):
        # grammatically we don't want this, practically we do
        path = 'j$ap+VT'
        self.assertIn(path, self.uppers)

    def test_exclBare(self):
        path = 'j$ap'
        self.assertNotIn(path, self.uppers)

    def test_inclSeriesIIandCons(self):
        paths = [
            'j$ap+VT-1SG.II',
            'j$ap+VT-1PL.II',
            'j$ap+VT-2SG.II',
            'j$ap+VT-2PL.II',
            'j$ap+VT-3.II',
            'j$ap+VT-3PL.II',
            'j$ap+VT[-3.II]=CN',
            'j$ap+VT[-3.II]=PN',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertIn(path, self.uppers)

    def test_inclTRSeriesIIandCons(self):
        paths = [
            'j$ap+VT-TR-1SG.II',
            'j$ap+VT-TR-1PL.II',
            'j$ap+VT-TR-2SG.II',
            'j$ap+VT-TR-2PL.II',
            'j$ap+VT-TR-3.II',
            'j$ap+VT-TR-3PL.II',
            'j$ap+VT-TR[-3.II]=CN',
            'j$ap+VT-TR[-3.II]=PN',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertIn(path, self.uppers)

    def test_exclAttr(self):
        path = 'j$ap+VT-ATTR'
        self.assertNotIn(path, self.uppers)

    def test_inclBigTderiv(self):
        paths = [
            'j$ap+VT-T-3.II',
            'j$ap+VT-T-TR-3.II',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertIn(path, self.uppers)

    @unittest.skip("derivational morphemes no longer included")
    def test_inclANTIPderiv(self):
        paths = [
            'j$ap+VT-ANTIP',
            'j$ap+VT-ANTIP-3.II',
            'j$ap+VT-ANTIP-ATTR',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertIn(path, self.uppers)

    def test_exclSX(self):
        path = 'j$ap+VT-SX'
        self.assertNotIn(path, self.uppers)


if __name__ == '__main__':
    unittest.main()

# python -m unittest test
# python -m unittest discover # all test files in current dir
# python -m unittest discover -s tests # all test files in /tests
