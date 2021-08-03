import unittest
from test import TestFSTOutput


"""
This suite checks the existence of expected morphotactic combinations
of more extended possibilities including functional morphemes like
dependent markers, as well as (not yet) the behavior of clitics.
These tests use the actual FST (v2) as a dependency.
"""


CONFIG = 'config/full_east.json'

class TestAuxiliaryPaths(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Auxiliary': ['y$ukw'],
        }
        cls.stem = 'y$ukw+AUX'
        super().setUpClass(CONFIG, test_stems)

    def test_bare(self):
        path = self.stem
        self.assertNotEqual(len(self.fst.generate(path)), 0)

    def test_goodSeriesI(self):
        pairs = {
            '1=' + self.stem: ['niyukw'],
            '2=' + self.stem: ['miyukw'],
            self.stem + '=1': ['yugwin'],
            self.stem + '=2': ['yugwim', 'yugum'],
            self.stem + '=3': ['yukwt'],
        }
        for gloss, expected_list in pairs.items():
            with self.subTest(path=gloss):
                result = sorted(self.fst.generate(gloss))
                self.assertNotEqual(len(result), 0)
                self.assertEqual(result, sorted(expected_list))

    def test_badSeriesI(self):
        paths = [
            '3=' + self.stem,           # initial 3
            '1=' + self.stem + '=1',    # doubled both sides
            '1=' + self.stem + '=2',    # mismatching
            self.stem + '=2=1',         # stacked
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
#         super().setUpClass(CONFIG, test_stems)


# class TestSubordinatorPaths(TestFSTOutput):

#     @classmethod
#     def setUpClass(cls):
#         test_stems = {
#             'Subordinator': ["$ii"],
#         }
#         cls.stem = "$ii+SUB"
#         super().setUpClass(CONFIG, test_stems)


if __name__ == '__main__':
    unittest.main()

# python -m unittest test
# python -m unittest discover # all test files in current dir
# python -m unittest discover -s tests # all test files in /tests
