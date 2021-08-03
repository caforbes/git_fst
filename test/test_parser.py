from git_fst.parser import ParserError
import unittest
from test import TestFSTOutput

"""
This suite builds a parser object end-to-end from input files 
and tests the behavior of its objects.
Files are generated and cleaned up on close.
These tests use the actual FST (v1) as a dependency.
"""

CONFIG1 = 'config/basic_east.json'
CONFIG2 = 'config/basic_dialectal.json'
CONFIG3 = 'config/full_east.json'

class TestParser(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "g_$an",
                "gwil$a",
                "w$an",
                # "test",
                # "moretest",
            ],
            'IntransitiveVerb': ["w$an"],
            'Preverb': ["'nii"], 
            'Modifier': ["sim"]
        }
        super().setUpClass(CONFIG1, test_stems)

    # analyze/generate forms
    def test_analyzeSuccess(self):
        lookup_result = self.fst.analyze('gwila')
        self.assertIsInstance(lookup_result, list)
        self.assertIn('gwil$a+N', lookup_result)

    def test_analyzeFailure(self):
        lookup_result = self.fst.analyze('xxx')
        self.assertIsInstance(lookup_result, list)
        self.assertEqual(0, len(lookup_result),
            "Should return empty list")

    def test_analyzeEmpty(self):
        lookup_result = self.fst.analyze('')
        self.assertIsInstance(lookup_result, list)
        self.assertEqual(0, len(lookup_result),
            "Should return empty list, returns {}".format(lookup_result))

    def test_generateSuccess(self):
        lookup_result = self.fst.generate('gwil$a+N')
        self.assertIsInstance(lookup_result, list)
        self.assertIn('gwila', lookup_result)

    def test_generateFailure(self):
        lookup_result = self.fst.generate('xxx')
        self.assertIsInstance(lookup_result, list)
        self.assertEqual(0, len(lookup_result),
            "Should return empty list")

    def test_generateEmpty(self):
        lookup_result = self.fst.generate('')
        self.assertIsInstance(lookup_result, list)
        self.assertEqual(0, len(lookup_result),
            "Should return empty list")

    def test_analyzeLowLine(self):
        lookup_result = self.fst.analyze('g̲an')
        self.assertIn('g_$an+N', lookup_result)

    def test_generateLowLine(self):
        lookup_result = self.fst.generate('g_$an+N')
        self.assertIn('g̲an', lookup_result)

    # list pairs
    def test_pairsIsList(self):
        result = self.fst.pairs()
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], tuple)
        self.assertEqual(len(result), 100)
        self.assertNotIn(('', ''), result)

    def test_randomPairs(self):
        result = self.fst.random_pairs()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 100)

    def test_randomUniquePairs(self):
        result = self.fst.random_unique_pairs()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 50)
        self.assertEqual(len(set(result)), 50)

    def test_randomUniquePairsLimit(self):
        result = self.fst.random_unique_pairs(10)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 10)
        self.assertEqual(len(set(result)), 10)

    def test_randomUniquePairsTooMany(self):
        with self.assertRaises(ParserError):
            self.fst.random_unique_pairs(1000)
    
    # lemmatize - one form
    def test_lemmatizeEqual(self):
        result = self.fst.lemmatize('gwila')
        expected = [[("gwila", "N")]]
        self.assertEqual(result, sorted(expected))
    
    def test_lemmatizeOne(self):
        result = self.fst.lemmatize('gwilan')
        expected = [[("gwila", "N")]]
        self.assertEqual(result, sorted(expected))
    
    def test_lemmatizeLowLine(self):
        result = self.fst.lemmatize("g̲ani'm")
        expected = [[('g̲an', "N")]]
        self.assertEqual(result, sorted(expected))
    
    def test_lemmatizeManyParsesOneStem(self):
        result = self.fst.lemmatize('gwilat')
        expected = [[("gwila", "N")]]
        self.assertEqual(result, sorted(expected))
    
    def test_lemmatizeMultipleOptions(self):
        result = self.fst.lemmatize('want')
        expected = [[("wan", "N")], [("wan", "VI")]]
        self.assertEqual(result, sorted(expected))
        # result output should come sorted
    
    def test_lemmatizeMultipleStems(self):
        result = self.fst.lemmatize("'niiwani'm")
        expected = [[("'nii", "PVB"), ("wan", "VI")]]
        self.assertEqual(result, sorted(expected))
    
    def test_lemmatizeMultipleStemsOptions(self):
        result = self.fst.lemmatize("simiwani'm") # should be simwan
        expected = [[("sim", "MDF"), ("wan", "N")],
                    [("sim", "MDF"), ("wan", "VI")]]
        self.assertEqual(result, sorted(expected))
    
    def test_lemmaTuple(self):
        result = self.fst._lemma_str_to_tuple("w$an+N")
        expected = ("wan", "N")
        self.assertEqual(result, expected)



class TestParserVariant(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "l$an",
                "w$an",
            ],
            'IntransitiveVerb': ["w$an"],
            'Preverb': ["'nii"],
        }
        super().setUpClass(CONFIG2, test_stems)

    # lemmatize - one form

    def test_lemmatizeVariantsStandard(self):
        result = self.fst.lemmatize('lan')
        expected = [[("lan/len", "N")]]
        self.assertEqual(result, sorted(expected))

    def test_lemmatizeVariantsGenerated(self):
        result = self.fst.lemmatize('len')
        expected = [[("lan/len", "N")]]
        self.assertEqual(result, sorted(expected))

    def test_lemmatizeMultipleOptionsVariants(self):
        result = self.fst.lemmatize('want')
        expected = [[("wan/wen", "N")], [("wan/wen", "VI")]]
        self.assertEqual(result, sorted(expected))
    
    def test_lemmatizeCompoundWithVariants(self):
        result = self.fst.lemmatize("'niiwani'm")
        expected = [[("'nii", "PVB"), ("wan/wen", "VI")]]
        self.assertEqual(result, sorted(expected))
    
    def test_lemmaTupleVariants(self):
        result = self.fst._lemma_str_to_tuple("w$an+N")
        expected = ("wan/wen", "N")
        self.assertEqual(result, expected)


class TestParserFunctional(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Modal': ['dim'],
            'Noun': [
                "l$an",
                "w$an",
            ]
        }
        super().setUpClass(CONFIG3, test_stems)

    # lemmatize - one form

    def test_lemmatizeFunctionalFromDict(self):
        result = self.fst.lemmatize('dim')
        expected = [[("dim", "MOD")]]
        self.assertEqual(result, expected)

    def test_lemmatizeFunctionalWithCat(self):
        result = self.fst.lemmatize('dii')
        expected = [[("dii", "OP")]]
        self.assertEqual(result, expected)

    def test_lemmatizeFunctionalNoCat(self):
        result = self.fst.lemmatize('mi')
        expected = None
        self.assertEqual(result, expected)


# python -m unittest test
# python -m unittest discover # all test files in current dir
# python -m unittest discover -s tests # all test files in /tests