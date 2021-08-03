# Gitksan FST

A morphological transducer for the Gitksan language (Tsimshianic, BC) implemented in `foma`. Lexical items are primarily drawn from Hindle & Rigsby (1975).

*The Gitksan language (Gitxsanimx̲, Gitsenimx̲, Gaanimx̲, etc) is part of the linguistic and cultural heritage of the Gitxsan people. This resource was created out of respect for that heritage, and by accessing this resource, you agree to treat that heritage and the Gitxsan people with respect.*

This resource is available under the Creative Commons Attribution No-Commercial 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/). You are welcome to use this resource for educational purposes and contribute to its development. Commercial use of this resource is prohibited.

## Version

Version 1.0 (Aug 3, 2021). This analyzer is still imperfect and contains many open issues. A complete gamut of tests, particularly for functional items and cliticization, is still forthcoming.

## Basic use

Load a parser by passing a path to a foma file or a configuration file. Inputting a configuration file will cause the foma file to be constructed upon loading (from dictionary csv, lexc files, etc). Sample configuration files can be found in `/config`. Foma files constructed in this way are saved to `/config/foma` and read automatically.

```python
# the most complete FST is built + loaded by default
fst = git_fst.Parser()
# or choose another configuration, or list your own foma file
fst = git_fst.Parser('config/basic_east.json')
fst = git_fst.Parser('path/to/git.foma')
```

Use `analyze` and `generate` functions to translate upper-lower forms and vvsa. If the input foma file writes to a binary file, the flookup utility is used for faster queries.

```python
results = fst.analyze(word)
for analysis in results:
	print(analysis)
```

Use the `lemmatize` function to identify possible stem forms/categories for a given surface form.

```python
results = fst.lemmatize(word)
for analysis in results:
	print(analysis)
```

## Dependencies

You must install `foma`.

Note that this project does not use the `foma.py` bindings as I could not get them to work; your independent installation of `foma` is accessed via a subprocess.

## more

Unit/object tests are in `test*.py` files; FST output tests are `test_output*.py`.

See `/docs` for further description.