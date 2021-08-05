import unittest

from test import FIX_DIR
from src.lexicon import Lexicon, LexiconError

"""
This suite tests the creation of lexc-compatible dictionary object
based on an input python dictionary or csv file.
"""

class TestLexiconFromDict (unittest.TestCase):

    def setUp(self):
        self.config = {
            'dictionary': {
                'Noun': ['apple', 'cat'],
                'Intransitive verb': ['talk']
            },
            'legal_categories': ['Noun', 'Intransitive verb']
        }
        self.lexicon = Lexicon(self.config)

    def test_category_setup(self):
        # imports all listed legal categories in camelcase
        self.assertIn('Noun', self.lexicon.categories)
        self.assertIn('IntransitiveVerb', self.lexicon.categories)
        self.assertEqual(len(self.lexicon.categories), 2)
        self.assertEqual(len(self.lexicon.illegal_categories), 0)

        # doesn't import other stuff
        self.assertNotIn('Intransitive verb', self.lexicon.categories)
        self.assertNotIn('Random', self.lexicon.categories)
    
    def test_doubled_category(self):
        self.config['legal_categories'].append('Noun')
        self.config['legal_categories'].append('noun')

        lexicon = Lexicon(self.config)
        self.assertEqual(len(lexicon.categories), 2)

    def test_dict_is_setup(self):
        self.assertIsInstance(self.lexicon.dict, dict)
        self.assertEqual(len(self.lexicon.dict.keys()), 2)

    def test_imports_entries(self):
        self.assertIn('apple', self.lexicon.dict['Noun'])
        self.assertIn('talk', self.lexicon.dict['IntransitiveVerb'])

    def test_doesnt_import_extra_category(self):
        self.config['dictionary'].update({'Random': ['bad']})
        
        lexicon = Lexicon(self.config)
        self.assertNotIn('Random', lexicon.dict)
        self.assertIn('Random', lexicon.illegal_categories)

    def test_validates_no_dict(self):
        del self.config['dictionary']
        with self.assertRaises(LexiconError):
            Lexicon(self.config)
        
    def test_validates_bad_dict_path(self):
        self.config['dictionary'] = 'lalala.csv'
        with self.assertRaises(FileNotFoundError):
            Lexicon(self.config)
        
    def test_validates_bad_dict_type(self):
        self.config['dictionary'] = 1
        with self.assertRaises(LexiconError):
            Lexicon(self.config)
    
    def test_lexc_string(self):
        actual = self.lexicon.as_lexc_str()
        # apple should be imported as 'apple
        self.assertRegex(actual, 'LEXICON RootNoun\n\'apple \tNoun ;\ncat \tNoun ;')


class TestLexiconFromCSV (unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.config = {
            'dictionary': FIX_DIR + '/test_dict.csv',
            'legal_categories': ['Noun', 'Intransitive verb']
        }
        cls.lexicon = Lexicon(cls.config)

    def test_category_setup(self):
        # imports all listed legal categories in camelcase
        self.assertIn('Noun', self.lexicon.categories)
        self.assertIn('IntransitiveVerb', self.lexicon.categories)
        self.assertEqual(len(self.lexicon.categories), 2)

    def test_imports_entries(self):
        self.assertIn('g$at', self.lexicon.dict['Noun'])
        self.assertIn('b$ax_', self.lexicon.dict['IntransitiveVerb'])

    def test_doesnt_import_extra_category(self):
        self.assertNotEqual(len(self.lexicon.illegal_categories), 0)
        self.assertNotIn('preverb', self.lexicon.dict)
        self.assertIn('preverb', self.lexicon.illegal_categories)


# python -m unittest test
# python -m unittest discover # all test files in current dir
# python -m unittest discover -s tests # all test files in /tests
