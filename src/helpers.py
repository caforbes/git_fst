import re

def unique(orig: list) -> list:
    new = []
    for x in orig:
        if x not in new:
            new.append(x)
    return new

# Git text conversion functions

UNDERSCORE = '_'
# MACRON = 'macron'
LOW_LINE = "̲"
UNDERLINE_OPTIONS = UNDERSCORE + LOW_LINE

def join_words(string: str) -> str:
    '''
    Given a multi-word input string containing spaces, returns that string as a single
    word with spaces removed and hyphens/apostrophes inserted according to Gitksan orthographic rules.
    Useful if comparing multi-word dict entries with text tokenized on spaces.
    '''
    string = string.strip()
    # hyphen after plain stops
    string = re.sub(r'([ptk]|ts|kw|k_) ([aeiou])', r"\1-\2", string)
    string = re.sub(
        "(k[" + UNDERLINE_OPTIONS + "]) ([aeiou])", r"\1-\2", string)
    # apostrophe before vowel-initial
    string = re.sub(r"([^']) ([aeiou])", r"\1'\2", string)
    return re.sub(' ', '', string)

def convert_to_underscore(string: str) -> str:
    '''
    Replaces unicode combining lowline/macron with underscore
    '''
    return standardize_back(string, underline=UNDERSCORE)

def convert_to_lowline(string: str) -> str:
    '''
    Replaces underscore with unicode combining lowline
    '''
    return standardize_back(string, underline=LOW_LINE)

def standardize_back(string: str, underline: str=UNDERSCORE) -> str:
    # find all instances of any kind of underline
    # replace with provided underline type
    pat = "[" + UNDERLINE_OPTIONS + "]"
    return re.sub(pat, underline, string)

def standardize_palatal(string: str, use_kya: bool=False) -> str:
    """ 
    Choose whether g(y)a and k(y)'a sequences will include the y character.
    Removes y character from g(y)e and g(y)i sequences altogether.
    """
    if re.search("[gk]y?'?[iea]", string):
        # remove y from palatals before front vowels
        string = re.sub("gy([ie])", r"g\1", string)
        string = re.sub("ky'([ie])", r"k'\1", string)
        # standardize ky or k before low vowel a
        if use_kya:
            string = re.sub("ga", "gya", string)
            string = re.sub("k'a", "ky'a", string)
        else:
            string = re.sub("gya", "ga", string)
            string = re.sub("ky'a", "k'a", string)
    return string


# Lexicon helpers

def csv_to_neutral(string: str) -> str:
    '''
    Removes the initial period that may be in a csv dictionary stem.
    Converts the dictionary 'gya' convention to the neutral 'ga' convention.
    '''

    string = string.lstrip('.')  # removes initial apostrophe in dict/excel
    string = standardize_back(string, UNDERSCORE)
    string = standardize_palatal(string, use_kya=False)
    return string

def neutral_to_corpus(string: str) -> str:
    '''
    Git corpus uses low-line combining underline, and "ga" spelling convention.
    Standardizes a string to use those variants.
    '''
    string = standardize_back(string, LOW_LINE)
    string = standardize_palatal(string, use_kya=False)
    return string

def neutral_to_lexc(string: str) -> str:
    '''
    Adds an initial apostrophe to vowel-initial words.
    Converts big t (t) to T and adds initial flag.
    '''
    string = join_words(string)
    if re.search('^[\$aeiou]', string):  # add apostrophe to initial vowel
        string = "'" + string
    if re.search(r'\(t\)', string):  # add big t flag and replace (t)->T
        string = '@P.VAL.BIGT@' + re.sub(r'\(t\)', 'T', string)
    return string

def assign_stress(word_list: list, stress_string: str) -> list:
    '''
    Takes list of words and string of stressed syllables.
    Converts words to have a stress symbol $ just before the vowel
    of the stressed syllable. Returns new list.
    '''
    try:
        stress_list = parse_stress_string(stress_string)
        if not stress_list:
            return word_list

        result = []
        for index, word in enumerate(word_list):
            
            # splits at beginning of V cluster if there is a VVC chunk
            vowel_chunks = re.split(r'([aeiou]+[^aeiou]*)', word)
            # splits at beginning of V cluster if only open (C)VV
            if len(vowel_chunks) == 1:
                vowel_chunks = re.split(r'([aeiou]+)', word)
            # removes all empty strings except initial empty onset
            vowel_chunks = [vowel_chunks[0]] + [x for x in vowel_chunks[1:] if x]
            
            try:
                stresses = stress_list[index]
            except IndexError:
                stresses = stress_list[0]
            for stress_idx in stresses:
                    vowel_chunks[stress_idx] = '$' + vowel_chunks[stress_idx]
            result.append(''.join(vowel_chunks))

    except Exception as e:
        raise type(e)("Failed to import word: {}".format(word))
    return result

def parse_stress_string(string: str) -> list: # list of list of stress indices
    '''
    Parses a string of numbers indicating stress placement into a list of lists of integers.
    Inner lists = single wordforms, may have multiple stress in one word.
    Outer list = list of wordforms, there may be multiple words in an entry, each
    with different stress.
    '''
    if '?' in string: # unknown
        return None
    elif not string: # default monosyllable stress
        return [[1]]
    
    # split into different wordforms
    list_of_stresses = string.split('; ')
    # split into multiple stresses per word, convert to int
    return [[int(num) for num in substring.split(',')]
            for substring in list_of_stresses]

def camelcase(string: str) -> str:
    '''
    Converts multiword string to single word in camel case.
    '''
    return ''.join(wd.capitalize() for wd in string.split())
