# Gitksan FST

A morphological transducer for the Gitksan language (Tsimshianic, BC) implemented in `foma`. Lexical items are primarily drawn from Hindle & Rigsby (1975).

*The Gitksan language (Gitxsanimx̲, Gitsenimx̲, Gaanimx̲, etc) is part of the linguistic and cultural heritage of the Gitxsan people. This resource was created out of respect for that heritage, and by accessing this resource, you agree to treat that heritage and the Gitxsan people with respect.*

This resource is available under the Creative Commons Attribution No-Commercial 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/). You are welcome to use this resource for educational purposes and contribute to its development. Commercial use of this resource is prohibited.

## Version

This is the first workable version (1.0, Aug 5, 2021). This analyzer is still imperfect and contains many open issues. A complete gamut of tests, particularly for functional items and cliticization, is still forthcoming.

## Dependencies

You must locally install `foma`.

Note that this project does not use the `foma.py` bindings as I could not get them to work; your independent installation of `foma` is accessed via a subprocess.

## Basic use of Parser objects

Load a parser by passing a path to a foma file or a configuration file. Inputting a configuration file is the expected usage, and it will cause the foma file to be constructed dynamically from the dictionary and lexc files included in this project. Available configuration files are located in `/fst`. Foma files constructed from configuration files are saved to `/fst/foma` in your installation.

```python
# default usage builds/loads the most complete FST, saved to fst/foma/git_full_EW.foma
fst = src.Parser()
# or choose another configuration file
fst = src.Parser('fst/basic_east.json')
# or list your own foma file
fst = src.Parser('path/to/git.foma')
```

Use `analyze` to output upper forms (segmented morpheme glosses) and `generate` to output lower forms (surface words). If the input foma file writes to a binary file, the `flookup` utility is used for faster queries.

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

## etc

Unit tests and object tests are in `test*.py` files. Tests of the FST output are in `test_output*.py` files.

See `/docs` for further description.
