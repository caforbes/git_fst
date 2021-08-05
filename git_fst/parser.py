import re
import json
import os

from . import helpers
from .builder import FomaBuilder
from .foma_reader import FomaReader


class ParserError(Exception):
    pass


proj_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

BASIC_E = os.path.join(proj_root, 'fst/basic_east.json')
BASIC_EW = os.path.join(proj_root, 'fst/basic_dialectal.json')
FULL_E = os.path.join(proj_root, 'fst/full_east.json')
FULL_EW = os.path.join(proj_root, 'fst/full_dialectal.json')

class Parser():
    """
    Skeleton class for FST in foma. Compiles lexc and foma files and captures
    output. By default, constructs and loads the fullest FST version
    (includes east/west variation, functional items)

    load_input = path to a foma file or json configuration file
                default: 'fst/full_dialect
    """

    def __init__(self, load_input: str or dict = FULL_EW) -> None:
        self.reload(load_input)
    
    def reload(self, load_input: str or dict) -> None:

        if type(load_input) is dict:
            foma_location, bin_location = self._build(load_input)
        elif type(load_input) is str and load_input[-5:] == '.foma':
            foma_location, bin_location = load_input, None
        elif type(load_input) is str and load_input[-5:] == '.json':
            with open(load_input) as f:
                load_input = json.load(f)
            foma_location, bin_location = self._build(load_input)
        else:
            raise ParserError('Unknown file type provided for foma file')
        
        # also need to validate to make sure foma location exists and is a file

        self._reader = FomaReader(foma_location, bin_location)
        self.analyzer_dict = {}
        self.generator_dict = {}

    def analyze(self, query: str) -> list:
        '''
        Input a surface wordform; returns list of possible analyses.
        Saves wordforms to internal dictionary if not already present.
        '''
        query = helpers.convert_to_underscore(query)
        if query not in self.analyzer_dict:
            self.analyzer_dict[query] = self._reader.lookup(query)
        return self.analyzer_dict[query]

    def generate(self, query: str) -> list:
        '''
        Input a foma analysis; returns list of possible surface wordforms.
        Saves analyses to internal dictionary if not already present.
        '''
        if query not in self.generator_dict:
            result_list = self._reader.lookup(query, inverse=True)
            result_list = [helpers.convert_to_lowline(item) for item in result_list]
            self.generator_dict[query] = result_list
        return self.generator_dict[query]

    def lemmatize(self, form: str) -> list:
        """ Input a word, returns a list of lists of tuples. Each sublist is
            a possible breakdown of the word; each tuple references an identified
            lemma in the word and its category.
            Returns None if no breakdowns/lemmas can be identified.
            Compound forms have multiple tuples [("form", "A"), ("form", "B")]
            Forms where variants can be generated are split with slashes ("form/Form", "X")
        """
        parses = self.analyze(form)
        if not parses: return None

        # for each possible parse, find all stem+category strings
        pat = r"(?:<[A-Z]+>)?[\w'\$]+\+[A-Z]+"
            # non-capturing group for <dialect alternation> (not sure if fst needs this)
            # combo of letters, apostr, stress marker
            # +ABRV tag for part of speech
        stem_options = [re.findall(pat, p) for p in parses]
        unique_options = helpers.unique(stem_options)
        
        # convert each stem string to a tuple of (surface forms, CAT)
        results = []
        for option in unique_options:
            option = [self._lemma_str_to_tuple(stem) for stem in option]
            if option and option not in results:
                results.append(option)

        if results:
            return sorted(results)

    def pairs(self) -> list:
        '''
        Reads the foma output of the pairs command and stores as a list of
        2-tuple word pairs (analysis, surfaceform).
        Returns a list of up to 100 tuple pairs.
        '''
        result = self._reader.query('pairs')
        return self._reader.format_foma_pairs(result)

    def random_pairs(self) -> list:
        '''
        Calls foma to run 'random-pairs', generating random pairs.
        Returns a list of up to 100 tuple pairs.
        '''
        result = self._reader.query('random-pairs')
        return self._reader.format_foma_pairs(result)

    def random_unique_pairs(self, limit: int = 50) -> list:
        ''' Calls foma to run 'random-pairs', and stores unique results
            up to the limit specified. May take a while since only 100 items
            can be queried at a time.
        '''
        if limit >= self._reader.paths:
            raise ParserError(
                '{} random pairs requested, but {} available'.format(
                    limit, self._reader.paths))

        sample_pairs = []
        result = []
        counter = 0
        while len(result) < limit:
            if not sample_pairs:
                counter += 1
                sample_pairs = self.random_pairs()
            item = sample_pairs.pop()
            if item not in result:
                result.append(item)
            
            if counter > (round(limit/3) + 1):
                raise ParserError('Timeout: {} unique random items could not be found.'.format(limit))
        
        return list(result)

    def _build(self, config: dict) -> tuple:
        ''' Constructs a new foma file from configuration dictionary.
            Returns a tuple of the new foma filepath and binary filepath.
        '''
        builder = FomaBuilder(config)
        builder.build()
        return (builder.foma_filepath(), builder.fomabin_filepath())

    def _lemma_str_to_tuple(self, analysis_str: str) -> tuple:
        """ When input a string that can be generated through the parser,
            returns a 2-tuple of the generated form (variants separated by slashes)
            and the category abbreviation for that form.
            e.g. 'cat+N' -> ('cat/Cat', 'N')
        """
        forms = self.generate(analysis_str)
        pat = r"\+([A-Z]+)"  # finds partofspeech abbreviation
        abbrev = re.search(pat, analysis_str).group(1)
        if forms and abbrev:
            surface_forms = "/".join(sorted(helpers.unique(forms)))
            return (surface_forms, abbrev)
