import re
import json
import os
from types import new_class

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

    _stem_pat = r"[\w'\$]+\+[A-Z]+"
    # combo of letters, apostr, stress marker
    # +ABRV tag for part of speech

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
        stem_options = [re.findall(self._stem_pat, p) for p in parses]
        unique_options = helpers.unique(stem_options)
        
        # convert each stem string to a tuple of (surface forms, CAT)
        results = []
        for option in unique_options:
            option = [self._analysis_to_lemma_tuple(stem) for stem in option]
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

    def _analysis_to_lemma_tuple(self, analysis_str: str) -> tuple:
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
        elif abbrev == 'DEM':
            if 'PROX' in analysis_str:
                surface_forms = 'tun'
            else:
                surface_forms = 'tust'
            return (surface_forms, abbrev)

    @classmethod
    def story_gloss(cls, fst_gloss: str) -> str:
        new_gloss = fst_gloss
        # dictionary of replacements from glossing guide
        replacements = {
            "n$ee+AUX": 'NEG',
            "y$ukw+AUX": 'PROG',
            "d$im+MOD": 'PROSP',
            "j$i+MOD": 'IRR',
            "j$i+SUB": 'IRR',
            "w$il+SUB": 'COMP',
            "w$in+SUB": 'COMP',
            "'$ii+SUB": 'CCNJ',
            "w$ila+SUB": 'MANR',
            "hl$aa+SUB": 'INCEP',
            "hl$is+SUB": 'PERF',
            "k_'$ap+MDF": 'VER',
            "'$ap+MDF": 'VER',
            "g_$an+MDF": 'REAS',
            "g_$ay+MDF": 'CONTR',
            "'$alp'a+ADV": 'RESTR',
            "hind$a+ADV": 'WH',
            "nd$a+ADV": 'WH',
            "'$a+P": 'PREP',
            "g_$o'o+P": 'LOC',
            "g_$oo+P": 'LOC',
            "g_$a'a+P": 'LOC',
            "g_an+CNJ": 'PCNJ',
            "'$ii+CNJ": 'CCNJ',
            "'$oo+CNJ": 'or',
            "+PRO": '',
            "+OP": '',
        }
        for fst_ver, ilg_ver in replacements.items():
            new_gloss = new_gloss.replace(fst_ver, ilg_ver)
        # specific replacements for things not broken down in fst
        new_gloss = re.sub(r"(\w+)\+OBL", r"OBL-\1.II", new_gloss)
        new_gloss = re.sub(r"(\w+)\+DEM", r"DEM.\1", new_gloss)
        if '+QUOT' in new_gloss:
            new_gloss = re.sub(r"(\d)SG\+QUOT", r"\1=QUOT", new_gloss)
            new_gloss = re.sub(r"3PL\+QUOT", r"3=QUOT.3PL", new_gloss)
            new_gloss = re.sub(r"(\d)PL\+QUOT", r"\1=QUOT.PL", new_gloss)
        # replace stems with 'word+CAT' form with '___'
        new_gloss = re.sub(cls._stem_pat, '___', new_gloss)
        return new_gloss
