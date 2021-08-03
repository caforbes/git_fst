import unittest

from test import FIX_DIR
from git_fst.foma_reader import FomaError, FomaReader

"""
This suite tests the behavior of the interface class that loads foma
and reads its output. Dependency is a sample foma/bin file.
"""

class TestBuilder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.path = FIX_DIR + '/test.foma'
        cls.binpath = FIX_DIR + '/test.fomabin'
        cls.reader = FomaReader(cls.path, cls.binpath)

    def test_loads(self):
        self.assertIsInstance(self.reader, FomaReader)
        self.assertEqual(self.reader.states, 4)
        self.assertEqual(self.reader.arcs, 3)
        self.assertEqual(self.reader.paths, 1)

    def test_no_foma(self):
        with self.assertRaises(FileNotFoundError):
            FomaReader('lalala.foma')

    def test_query(self):
        self.assertEqual(self.reader.query('upper-words'), 'cog')
        self.assertEqual(self.reader.query('lower-words'), 'dog')

    def test_lookup(self):
        result = self.reader.lookup('dog')
        self.assertEqual(result, ['cog'])

    def test_lookup_no_bin(self):
        reader = FomaReader(self.path)
        result = reader.lookup('dog')
        self.assertEqual(result, ['cog'])

    def test_inverse_lookup(self):
        result = self.reader.lookup('cog', inverse=True)
        self.assertEqual(result, ['dog'])

    def test_inverse_lookup_no_bin(self):
        reader = FomaReader(self.path)
        result = reader.lookup('cog', inverse=True)
        self.assertEqual(result, ['dog'])