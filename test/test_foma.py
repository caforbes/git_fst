#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


# import unittest

# from test import FIX_DIR
# from src.foma import FST

# """
# Tests for the foma.py bindings. Currently I can't get these to load.
# # AttributeError: /lib/x86_64-linux-gnu/libfoma.so.0: undefined symbol: add_defined_function
# """

# def test_fst():
#     return FST.load(FIX_DIR + '/test.foma')

# @unittest.skip("original foma hooks don't load")
# class TestOrigFST(unittest.TestCase):
#     """
#     Test cases for Foma Python bindings.
#     """

#     def test_load_fst(self):
#         fst = test_fst()
#         self.assertIsInstance(fst, FST)

#     def test_apply_fst(eat_fst):
#         result, = test_fst().apply_up('ate')
#         assert result == 'eat+V+Past'

#     def test_apply_down(eat_fst):
#         result, = test_fst().apply_down('eat+V+3P+Sg')
#         assert result == 'eats'
