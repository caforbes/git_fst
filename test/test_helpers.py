import unittest

from src import helpers

"""
Tests helper functions having to do with case changing,
stress annotation, and (TODO) git orthography.
"""

class TestCamelcase (unittest.TestCase):
    def test_singleword(self):
        result = helpers.camelcase('hello')
        self.assertEqual(result, 'Hello')

    def test_multiword(self):
        result = helpers.camelcase('hello world')
        self.assertEqual(result, 'HelloWorld')

class TestStressMarking (unittest.TestCase):

    def test_stress_unknown(self):
        inputwds = ['bat']
        result = helpers.assign_stress(inputwds, '?')

        self.assertEqual(['bat'], result)

    def test_stress_blank_CV(self):
        inputwds = ['ba']
        result = helpers.assign_stress(inputwds, '')

        self.assertEqual(['b$a'], result)

    def test_stress_blank_CVC(self):
        inputwds = ['bat']
        result = helpers.assign_stress(inputwds, '')

        self.assertEqual(['b$at'], result)

    def test_stress_blank_CVVC(self):
        inputwds = ['baat']
        result = helpers.assign_stress(inputwds, '')

        self.assertEqual(['b$aat'], result)

    def test_stress_one_CV(self):
        inputwds = ['ba']
        result = helpers.assign_stress(inputwds, '1')

        self.assertEqual(['b$a'], result)
    def test_stress_one_CVC(self):
        inputwds = ['bat']
        result = helpers.assign_stress(inputwds, '1')

        self.assertEqual(['b$at'], result)

    def test_stress_one_CVVC(self):
        inputwds = ['baat']
        result = helpers.assign_stress(inputwds, '1')

        self.assertEqual(['b$aat'], result)

    def test_stress_one_CVCV(self):
        inputwds = ['baba']
        result = helpers.assign_stress(inputwds, '1')

        self.assertEqual(['b$aba'], result)

    def test_stress_one_CVVCV(self):
        inputwds = ['baaba']
        result = helpers.assign_stress(inputwds, '1')

        self.assertEqual(['b$aaba'], result)

    def test_stress_two_CVCV(self):
        inputwds = ['baba']
        result = helpers.assign_stress(inputwds, '2')

        self.assertEqual(['bab$a'], result)

    def test_stress_two_CVVCV(self):
        inputwds = ['baaba']
        result = helpers.assign_stress(inputwds, '2')

        self.assertEqual(['baab$a'], result)

    def test_stress_two_echoCVVV(self):
        inputwds = ['baa\'a']
        result = helpers.assign_stress(inputwds, '2')

        self.assertEqual(['baa\'$a'], result)

    def test_stress_multiword_two(self):
        inputwds = ['baba', 'bibatxws']
        result = helpers.assign_stress(inputwds, '2')

        self.assertEqual(['bab$a', 'bib$atxws'], result)

    def test_stress_multiword_two_four(self):
        inputwds = ['baba', 'bibaxbaba']
        result = helpers.assign_stress(inputwds, '2; 4')

        self.assertEqual(['bab$a', 'bibaxbab$a'], result)

    def test_stress_multistress_onefour(self):
        inputwds = ['biibaxbaba']
        result = helpers.assign_stress(inputwds, '1,4')

        self.assertEqual(['b$iibaxbab$a'], result)

    def test_stress_stress_outofrange(self):
        with self.assertRaises(IndexError):
            inputwds = ['baat']
            helpers.assign_stress(inputwds, '4')

    def test_stress_no_onset_single(self):
        inputwds = ['aa']
        result = helpers.assign_stress(inputwds, '1')

        self.assertEqual(['$aa'], result)

    def test_stress_no_onset_initial(self):
        inputwds = ['aba']
        result = helpers.assign_stress(inputwds, '1')

        self.assertEqual(['$aba'], result)

    def test_stress_no_onset_later(self):
        inputwds = ['aba']
        result = helpers.assign_stress(inputwds, '2')

        self.assertEqual(['ab$a'], result)

if __name__ == '__main__':
    unittest.main()
