import unittest
from src.parser import Parser, ParserError
from src.ilg_helpers import STEM_PAT
import unittest
from test import TestFSTOutput, BASIC_E, BASIC_EW, FULL_E

"""
This suite builds a parser object end-to-end from input files 
and tests the behavior of its objects.
Files are generated and cleaned up on close.
These tests use the actual FST (v1, v3) as a dependency.
"""


class TestParser(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "g_$an",
                "gwil$a",
                "w$an",
            ],
            "IntransitiveVerb": ["w$an"],
            "Preverb": ["'nii"],
            "Modifier": ["sim"],
        }
        super().setUpClass(BASIC_E, test_stems)

    # tests for analyze function
    def test_analyzeSuccess(self):
        lookup_result = self.fst.analyze("gwila")
        self.assertIsInstance(lookup_result, list)
        self.assertIn("gwil$a+N", lookup_result)

    def test_analyzeFailure(self):
        lookup_result = self.fst.analyze("xxx")
        self.assertIsInstance(lookup_result, list)
        self.assertEqual(0, len(lookup_result), "Should return empty list")

    def test_analyzeEmpty(self):
        lookup_result = self.fst.analyze("")
        self.assertIsInstance(lookup_result, list)
        self.assertEqual(
            0,
            len(lookup_result),
            "Should return empty list, returns {}".format(lookup_result),
        )

    def test_analyzeLowLine(self):
        lookup_result = self.fst.analyze("g̱an")
        self.assertIn("g_$an+N", lookup_result)

    def test_analyzeValidateGlossMatch(self):
        lookup_result = self.fst.analyze("g̱an", gloss_validator="tree")
        self.assertIn("g_$an+N", lookup_result)

    def test_analyzeValidateGlossNoMatch(self):
        # no matches when FST produces more morphemes than actually found
        lookup_result = self.fst.analyze("g̱anit", gloss_validator="tree")
        self.assertEqual(len(lookup_result), 0)
        # but note morphemes in validator string need not be matched

    # tests for generate function
    def test_generateSuccess(self):
        lookup_result = self.fst.generate("gwil$a+N")
        self.assertIsInstance(lookup_result, list)
        self.assertIn("gwila", lookup_result)

    def test_generateFailure(self):
        lookup_result = self.fst.generate("xxx")
        self.assertIsInstance(lookup_result, list)
        self.assertEqual(0, len(lookup_result), "Should return empty list")

    def test_generateEmpty(self):
        lookup_result = self.fst.generate("")
        self.assertIsInstance(lookup_result, list)
        self.assertEqual(0, len(lookup_result), "Should return empty list")

    def test_generateLowLine(self):
        lookup_result = self.fst.generate("g_$an+N")
        self.assertIn("g̱an", lookup_result)

    # test pairs, random pairs, unique pairs list functions
    def test_pairsIsList(self):
        result = self.fst.pairs()
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], tuple)
        self.assertEqual(len(result), 100)
        self.assertNotIn(("", ""), result)

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

    #  test lemmatize function for various input
    def test_lemmatizeEqual(self):
        result = self.fst.lemmatize("gwila")
        expected = [[("gwila", "N")]]
        self.assertEqual(result, sorted(expected))

    def test_lemmatizeOne(self):
        result = self.fst.lemmatize("gwilan")
        expected = [[("gwila", "N")]]
        self.assertEqual(result, sorted(expected))

    def test_lemmatizeLowLine(self):
        result = self.fst.lemmatize("g̱ani'm")
        expected = [[("g̱an", "N")]]
        self.assertEqual(result, sorted(expected))

    def test_lemmatizeManyParsesOneStem(self):
        result = self.fst.lemmatize("gwilat")
        expected = [[("gwila", "N")]]
        self.assertEqual(result, sorted(expected))

    def test_lemmatizeMultipleOptions(self):
        result = self.fst.lemmatize("want")
        expected = [[("wan", "N")], [("wan", "VI")]]
        self.assertEqual(result, sorted(expected))
        # result output should come sorted

    def test_lemmatizeMultipleStems(self):
        result = self.fst.lemmatize("'niiwani'm")
        expected = [[("'nii", "PVB"), ("wan", "VI")]]
        self.assertEqual(result, sorted(expected))

    def test_lemmatizeMultipleStemsOptions(self):
        result = self.fst.lemmatize("simiwani'm")  # TODO: should be simwan
        expected = [[("sim", "MDF"), ("wan", "N")], [("sim", "MDF"), ("wan", "VI")]]
        self.assertEqual(result, sorted(expected))

    # test make lemma tuple function
    def test_lemmaTuple(self):
        result = self.fst._analysis_to_lemma_tuple("w$an+N")
        expected = ("wan", "N")
        self.assertEqual(result, expected)

    # test analyze_complete function
    def test_analyzeProperties_basic(self):
        query = "gwila"
        result = self.fst.analyze_properties(query)

        self.assertEqual(result.get("input"), query)
        self.assertEqual(result.get("output"), self.fst.analyze(query))
        self.assertEqual(result.get("output"), ["gwil$a+N"])

        # no final validation because no validators input
        self.assertEqual(result.get("validated"), None)

    def test_analyzeProperties_validateGlossExact(self):
        query = "gwila"
        result = self.fst.analyze_properties(query, gloss_validator="blanket")

        # result object contains raw scored analyses
        raw_validated = result.get("valid_gloss_scored")
        self.assertIsInstance(raw_validated, list)
        self.assertNotEqual(len(raw_validated), 0)
        self.assertIsInstance(raw_validated[0], tuple)

        # result object contains list of validated analyses
        validated = result.get("valid_gloss")
        self.assertIsInstance(validated, list)
        self.assertIn("gwil$a+N", validated)

        self.assertEqual(validated, result.get("validated"))

    def test_analyzeProperties_validateGlossToSubset(self):
        query = "gwilat"
        result = self.fst.analyze_properties(query, gloss_validator="blanket-3.II")

        validated = result.get("valid_gloss")
        self.assertTrue(len(validated) < len(result.get("output")))
        self.assertIn("gwil$a+N-3.II", validated)
        self.assertNotIn("gwil$a+N-SX", validated)

        self.assertEqual(validated, result.get("validated"))

    def test_analyzeProperties_validateGlossNoMatches(self):
        query = "gwilan"
        result = self.fst.analyze_properties(query, gloss_validator="what-eggs")

        # result object with raw scores is empty list
        raw_validated = result.get("valid_gloss_scored")
        self.assertIsInstance(raw_validated, list)
        self.assertEqual(len(raw_validated), 0)

        # result object with valid analyses is empty list
        validated = result.get("valid_gloss")
        self.assertIsInstance(validated, list)
        self.assertEqual(len(validated), 0)

        self.assertEqual(validated, result.get("validated"))


class TestParserVariant(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "l$an",
                "w$an",
            ],
            "IntransitiveVerb": ["w$an"],
            "Preverb": ["'nii"],
        }
        super().setUpClass(BASIC_EW, test_stems)

    # test lemmatize function with dialect variation
    def test_lemmatizeVariantsStandard(self):
        result = self.fst.lemmatize("lan")
        expected = [[("lan/len", "N")]]
        self.assertEqual(result, sorted(expected))

    def test_lemmatizeVariantsGenerated(self):
        result = self.fst.lemmatize("len")
        expected = [[("lan/len", "N")]]
        self.assertEqual(result, sorted(expected))

    def test_lemmatizeMultipleOptionsVariants(self):
        result = self.fst.lemmatize("want")
        expected = [[("wan/wen", "N")], [("wan/wen", "VI")]]
        self.assertEqual(result, sorted(expected))

    def test_lemmatizeCompoundWithVariants(self):
        result = self.fst.lemmatize("'niiwani'm")
        expected = [[("'nii", "PVB"), ("wan/wen", "VI")]]
        self.assertEqual(result, sorted(expected))

    # test make lemma tuple function with dialect variation
    def test_lemmaTupleVariants(self):
        result = self.fst._analysis_to_lemma_tuple("w$an+N")
        expected = ("wan/wen", "N")
        self.assertEqual(result, expected)


class TestParserFunctional(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Modal": ["dim"],
            "Noun": [
                "l$an",
                "w$an",
            ],
        }
        super().setUpClass(FULL_E, test_stems)

    # test lemmatize function for functional lemmas
    def test_lemmatizeFunctionalFromDict(self):
        result = self.fst.lemmatize("dim")
        expected = [[("dim", "MOD")]]
        self.assertEqual(result, expected)

    def test_lemmatizeFunctionalWithCat(self):
        result = self.fst.lemmatize("dii")
        expected = [[("dii", "OP")]]
        self.assertEqual(result, expected)

    def test_lemmatizeFunctionalNoCat(self):
        result = self.fst.lemmatize("mi")
        expected = None
        self.assertEqual(result, expected)

    def test_lemmatizeDemonstrative(self):
        result = self.fst.lemmatize("tun")
        expected = [[("-un", "DEM")]]
        self.assertEqual(result, expected)

    def test_lemmatizeDemonstrativePl(self):
        result = self.fst.lemmatize("dipun")
        expected = [[("-un", "DEM")]]
        self.assertEqual(result, expected)

    def test_lemmatizeDemonstrativeComplex(self):
        result = self.fst.lemmatize("asun")
        expected = [[("a", "P"), ("-un", "DEM")]]
        self.assertEqual(result, expected)


# python -m unittest test
# python -m unittest discover # all test files in current dir
# python -m unittest discover -s tests # all test files in /tests
