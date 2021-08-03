import unittest
import os, shutil

from test import FIX_DIR
from git_fst.builder import FomaBuilder, BuilderError

"""
This suite tests the construction of new lexc and foma files based
on input. Files are cleaned up after test completion.
"""

class TestBuilder(unittest.TestCase):

    def setUp(self):
        self.config = {
            "test": True,

            "name": "test",
            "lexc_files": ["test_nouns.txt"],
            "rules_files": ["test_rules.txt"],
            "dialect_variation": False,
            
            "dictionary": {'Noun': ["test"]},
            "legal_categories": ["noun"]
        }
    
    def test_dirname(self):
        builder = FomaBuilder(self.config)

        actual = builder.config['dir']
        expected = os.path.abspath(FIX_DIR)
        self.assertEqual(actual, expected)

    def test_invalid_no_name(self):
        del self.config['name']
        with self.assertRaises(BuilderError):
            FomaBuilder(self.config)

    def test_build(self):
        path = os.path.abspath(os.path.join(FIX_DIR, 'foma'))
        try:
            builder = FomaBuilder(self.config)
            builder.build()
            
            self.assertTrue(os.path.exists(builder.lexc_filepath()))
            self.assertTrue(os.path.exists(builder.foma_filepath()))
        finally:
            shutil.rmtree(path)
    
    def test_lexc_path(self):
        actual = FomaBuilder(self.config).lexc_filepath()
        expected = os.path.abspath(os.path.join(FIX_DIR, 'foma/test.txt'))
        self.assertEqual(actual, expected)
    
    def test_foma_path(self):
        actual = FomaBuilder(self.config).foma_filepath()
        expected = os.path.abspath(os.path.join(FIX_DIR, 'foma/test.foma'))
        self.assertEqual(actual, expected)
        
    # tests for lexc/morphological description builder