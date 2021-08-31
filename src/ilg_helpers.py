import re


def fst_to_story_gloss(fst_gloss: str, stem_pattern: str) -> str:
    """ 
    Input a gloss from the FST to convert it approximately to how it would look
    in the Gitksan interlinear gloss format used in stories. Instead of a definition
    for main stems, an empty '___' is used.
        - fst_gloss: string output from the parser
        - stem_pattern: regex corresponding to the shape of a stem in the fst output
    """
    new_gloss = fst_gloss
    # morpheme/tag replacements: fst style as key, story form as value
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
    # specific replacements where fst and story breakdowns differ
    new_gloss = re.sub(r"(\w+)\+OBL", r"OBL-\1.II", new_gloss)
    new_gloss = re.sub(r"(\w+)\+DEM", r"DEM.\1", new_gloss)
    if '+QUOT' in new_gloss:
        new_gloss = re.sub(r"(\d)SG\+QUOT", r"\1=QUOT", new_gloss)
        new_gloss = re.sub(r"3PL\+QUOT", r"3=QUOT.3PL", new_gloss)
        new_gloss = re.sub(r"(\d)PL\+QUOT", r"\1=QUOT.PL", new_gloss)
    # replace various stems with '___'
    new_gloss = re.sub(stem_pattern, '___', new_gloss)
    return new_gloss

def filter_matching_glosses(analyses: list, story_gloss: str) -> list:
    pass

def is_gloss_match(fst_gloss: str, story_gloss: str) -> bool:
    pass

def match_score():
    pass