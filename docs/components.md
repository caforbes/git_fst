# Components

## Dictionary

The lexical items recognized by this analyzer are primarily drawn from Hindle & Rigsby (1975) and personal fieldwork with Gitxsan elders, with annotation by myself. See `config/dict.csv`.

## lexc

The lexc files (`config/lexc`) include information about additional morphology: preverb/modifier compounding, inflectional suffixes, and clitics. The lexc text that lists lexical items from the dictionary is generated upon load. The lexc header is also generated on load, with the exception of the flag inventory (`git_flags.txt`).

## Rules

This analyzer relies heavily on allomorphic rules to generate local allomorphic alternations and productive dialect variation. See `config/git_rules.txt`.

## Config files

Four configuration files are included in this compilation and accessible via their file path or as constants:

* `BASIC_E` = `config/basic_east.json`
* `BASIC_EW` = `config/basic_dialectal.json`
* `FULL_E` = `config/full_east.json`
* `FULL_EW` = `config/full_dialectal.json`

The "basic" configurations exclude functional items like pronouns or aspect markers from compilation, working instead only with open-class lexical items drawn from the dictionary. The "east" configurations exclude all dialect variation rules from compilation, using only the forms that are explicitly listed in the dictionary (which is based on the Git-an'maaxs dialect; Eastern).