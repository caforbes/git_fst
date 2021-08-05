from git_fst import Parser, BASIC_E, BASIC_EW, FULL_E, FULL_EW
import shutil
import json
import unittest
import os


FIX_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'fixtures'))


def create_fst_config(json_path: str, dictionary: dict) -> dict:
    with open(json_path) as f:
        config = json.load(f)
    config['test'] = True
    if dictionary:
        config['dictionary'] = dictionary
    config['name'] = 'testy'
    return config


def import_fst_files(config) -> list:
    # identify required files
    files = [f for f in config['rules_files']]
    if type(config['dictionary']) is str:
        if not config['dictionary'][:4] == 'test':
            files.append(config['dictionary'])
    # copy those files to fixtures directory
    new_files = []
    for file in files:
        orig = os.path.join(os.path.dirname(__file__), '../fst', file)
        dest = os.path.join(os.path.dirname(__file__), 'fixtures', file)
        shutil.copy(orig, dest)
        new_files.append(dest)
    # copy lexc files to directory in fixtures
    orig_lexc = orig = os.path.join(
        os.path.dirname(__file__), '../fst/lexc')
    dest_lexc = orig = os.path.join(
        os.path.dirname(__file__), 'fixtures/lexc')
    shutil.copytree(orig_lexc, dest_lexc)

    return new_files


def cleanup_fst_files(fixture_files) -> None:
    # remove rules files
    for file in fixture_files:
        os.remove(file)
    # remove lexc directory
    lexc = os.path.join(
        os.path.dirname(__file__), 'fixtures/lexc')
    shutil.rmtree(lexc)
    # remove foma directory
    foma = os.path.join(
        os.path.dirname(__file__), 'fixtures/foma')
    shutil.rmtree(foma)


class TestFSTOutput(unittest.TestCase):

    @classmethod
    def setUpClass(cls, json_config, dictionary) -> None:
        cls.config = create_fst_config(json_config, dictionary)
        cls.added_files = import_fst_files(cls.config)
        cls.fst = Parser(cls.config)

    @classmethod
    def tearDownClass(cls) -> None:
        cleanup_fst_files(cls.added_files)
