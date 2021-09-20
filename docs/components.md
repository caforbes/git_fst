# Components

A `foma` morphological analyzer contains three main components:

- a dictionary
- a morphological description
- a set of transformational rules

This analyzer works from a single source for each of these components, but can be configured to load only certain sub-parts to produce a customized subset. Here I explain where each of the components is located within this project, a bit about their context, and about the configuration settings.

## Dictionary

The lexical items recognized by this analyzer are primarily drawn from Hindle & Rigsby (1975) and personal fieldwork with Gitxsan elders, with annotation by myself. The dictionary is located at `fst/dict.csv`, and contains a list of stems and their plural forms along with an annotation of their morphological category and some stress notes.

The dictionary file is formatted to be shared with the Mother Tongues Dictionary resource, an electronic talking dictionary resource for Gitksan, and contains substantial additional information relevant to a more robust dictionary project. This analyzer leverages the dictionary format originally set up for that resource.

## Morphological description

The morphological description for a foma analyzer are stored in text files using `lexc` markup, stored in `fst/lexc/*`. The folder contains several files that describe the morphological behavior of various categories.

Gitksan is somewhat morphologically complex although not synthetic; it is fusional and involves a substantial amount of compounding (cf. Germanic languages). There are also a number of clitics that can appear in a wide variety of positions. Concatenation operations included in this parser include:

- inflectional suffixation on nouns/verbs
- preverb/modifier compounding (/prefixation) on verbs
- ergative clitics on auxiliaries
- enclitics preceding nouns
- second position clitics

There is no dedicated lexc file for the lexical items included in the dictionary: these are generated upon load. The lexc header is also generated on load, with the exception of the flag inventory which is stored in `git_flags.txt`.

## Rules

This analyzer relies heavily on allomorphic rules to generate local allomorphic alternations and productive dialect variation. The rules are listed and self-documented in `fst/git_rules.txt`.

Local allomorphy accomplished via rule includes:

- pre-vocalic voicing (applies after suffixation)
- vowel insertion between sonorants
- deletion of morphemes before third-plural *-diit*.

Dialect variation rules are listed in a special section of the rules file (flagged as **stem variation**) and are removed from "_E"/"east" versions of the parser which reflect only the Eastern dialect. These include:

- short a/e alternations (*gat~get*)
- he/hi alternations (*hetxw~hitxw*)
- gwi/gu alternations (*agwi~agu*)

## Configuration

Four configuration files are included in this compilation and are accessible via their file path or as constants:

* `BASIC_E` = `fst/basic_east.json`
* `BASIC_EW` = `fst/basic_dialectal.json`
* `FULL_E` = `fst/full_east.json`
* `FULL_EW` = `fst/full_dialectal.json`

The "basic" configurations exclude functional items like pronouns or aspect markers from compilation, and do not include clitics. They produce only paradigm-like output, including only open-class lexical items and their various inflections. (Note that plurals are treated as derivational, not inflectional, and are listed in the dictionary rather than being generated.) The "full" configurations contain functional items and the full array of clitics.

The "E/east" configurations exclude all dialect variation rules from compilation, using only the forms that are explicitly listed in the dictionary (which is primarily but not exclusively based on the Git-an'maaxs dialect; Eastern). The "EW/dialectal" configurations include optional dialect rules to produce a variety of possible surface forms for a given lexical input.

Examples of configuration files are stored in `/fst/*.json`. The necessary components of a configuration file are as follows:

- **name:** Unique title for the custom analyzer. Related files will be stored with this as the filename.
- **dictionary:** Dictionary of stems formatted with categories as keys and lists of words as values; OR a link to a valid CSV file formatted similarly to `fst/dict.csv`.
- **legal_categories:** List of categories that the analyzer will read and import from the dictionary; case-insensitive. Words with categories not listed here will be ignored.
- **lexc_files:** List of valid paths to lexc files that the analyzer will read and import. Files not listed here will be ignored, allowing certain types of morphology to be excluded.
- **rules_files:** List of files containing morphological rules in foma format. These will be concatenated in order to produce the foma file.
- **dialect_variation:** boolean value representing whether stem-variation portions of the rules files will be included (true) or excluded (false).