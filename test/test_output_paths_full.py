import unittest
from test import TestFSTOutput, FULL_E


"""
This suite checks the existence of expected morphotactic combinations
of more extended possibilities including functional morphemes like
dependent markers, as well as (not yet) the behavior of clitics.
These tests use the actual FST (v2) as a dependency.
"""


class TestAuxiliaryPaths(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Auxiliary': ['y$ukw'],
        }
        cls.stem = 'y$ukw+AUX'
        super().setUpClass(FULL_E, test_stems)

    def test_bare(self):
        path = self.stem
        self.assertNotEqual(len(self.fst.generate(path)), 0)

    def test_goodSeriesI(self):
        pairs = {
            '1.I=' + self.stem: ['niyukw'],
            '2.I=' + self.stem: ['miyukw'],
            self.stem + '=1.I': ['yugwin'],
            self.stem + '=2.I': ['yugwim', 'yugum'],
            self.stem + '=3.I': ['yukwt'],
        }
        for gloss, expected_list in pairs.items():
            with self.subTest(path=gloss):
                result = sorted(self.fst.generate(gloss))
                self.assertNotEqual(len(result), 0)
                self.assertEqual(result, sorted(expected_list))

    def test_badSeriesI(self):
        paths = [
            '3.I=' + self.stem,             # initial 3.I
            '1.I=' + self.stem + '=1.I',    # doubled both sides
            '1.I=' + self.stem + '=2.I',    # mismatching
            self.stem + '=2.I=1.I',         # stacked
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertEqual(len(self.fst.generate(path)), 0)

# good
    # Ximaa
    # Ximaahl
    # Ximaas (hard!)
    # Ximaat/n = SI
    # Xhl
    # Xit
    # Xii
    # Xiihl
# bad
    # Xgi
    # Xt = PN
    # Xaa
    # Xhlimaa


# class TestModalPaths(TestFSTOutput):

#     @classmethod
#     def setUpClass(cls):
#         test_stems = {
#             'Modal': ['d$im']
#         }
#         cls.stem = 'd$im+MOD'
#         super().setUpClass(FULL_E, test_stems)


# class TestSubordinatorPaths(TestFSTOutput):

#     @classmethod
#     def setUpClass(cls):
#         test_stems = {
#             'Subordinator': ["$ii"],
#         }
#         cls.stem = "$ii+SUB"
#         super().setUpClass(FULL_E, test_stems)


if __name__ == '__main__':
    unittest.main()

# python -m unittest test
# python -m unittest discover # all test files in current dir
# python -m unittest discover -s tests # all test files in /tests
