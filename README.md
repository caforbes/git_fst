# Gitksan FST

A morphological transducer for the Gitksan language (Tsimshianic, BC) implemented in `foma`. Lexical items are primarily drawn from Hindle & Rigsby (1975).

*The Gitksan language (Gitxsanimx̱, Gitsenimx̱, Gaanimx̱, etc) is part of the linguistic and cultural heritage of the Gitxsan people. This resource was created out of respect for that heritage, and by accessing this resource, you agree to treat that heritage and the Gitxsan people with respect.*

This resource is available under the Creative Commons Attribution No-Commercial 4.0 license (<https://creativecommons.org/licenses/by-nc/4.0/>). You are welcome to use this resource for educational purposes and contribute to its development. Commercial use of this resource is prohibited.

## Version

This is a workable but incomplete version (Sep 22, 2021). This analyzer is still imperfect and contains many open issues. A complete gamut of tests, particularly for functional items, cliticization, and dialectal variation rules, is still forthcoming.

## Setup

### Docker

You should have [Docker](https://docs.docker.com/engine/install/) installed. To setup the container and all dependencies, including Python and foma, run:

```sh
docker build -t git_fst .
```

To open a Python shell with this package loaded, run:

```sh
docker run -it git_fst
# Python 3.12.4 (main, Aug  2 2024, 14:41:31) [GCC 12.2.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
```

(To avoid creating multiple one-off containers each time you run, add the `--rm` flag: `docker run -it --rm git_fst`)

### Locally

You should have a working version of Python `3.12`. You must locally install `foma` ([guide here](https://fomafst.github.io/)).

Note that this project does not use the `foma.py` bindings as I could not get them to work. Instead, your independent installation of `foma` is accessed via a subprocess. You must be able to call the program on the command line with `foma`:

```sh
foma
# Foma, version 0.10.0
# ...
# Type "help" to list all commands available.
# Type "help <topic>" or help "<operator>" for further help.
# foma[0]:
```

If this does not work, it's recommended to try the Docker setup.

If this does work, you can then setup and test the package:

1. `python`: Open a python shell. (Or open a file and do this.)
2. `import src`: Load the package into the shell or your own file.

## Try it

### Load a parser

Load a parser by passing a path to a foma file or a configuration file. Inputting a configuration file is the expected usage, and it will cause the foma file to be constructed dynamically from the dictionary and lexc files included in this project. Foma files constructed from configuration files are saved to `/fst/foma` in your installation.

Load the default full parser:

```python
fst = src.Parser()  # default usage builds/loads the most complete FST, saved to fst/foma/git_full_EW.foma
```

Or choose a different configuration file to get a smaller parser, e.g. eastern dialect only. The available options are stored in `fst/`.

```python
fst = src.Parser(src.BASIC_E)
fst = src.Parser('path/to/your/config.json')
```

You can also completely ignore the provided dictionaries and morphological rules and load your own `.foma` file.

```python
fst = src.Parser('path/to/git.foma')
```

To test, try any command:

```python
fst.analyze("gat")
# ['g$at+VI', 'g$at+N']
```

### Command: `analyze`/`generate`

Use `analyze` to transduce lower forms to upper forms (producing the analysis/gloss) or `generate` transduce upper forms to lower forms (producing a surface wordform). If the input foma file writes to a binary file, the flookup utility is used for faster queries.

```python
fst.analyze("gat")
# ['g$at+VI', 'g$at+N']
fst.generate('g$at+VI-3.II')
# ['gatt', 'gett']
```

### Command: `lemmatize`

Use the `lemmatize` function to identify possible stem forms/categories for a given surface form.

```python
fst.lemmatize("gat")
# [[('gat', 'N')], [('gat', 'VI')]]
```

## Inspecting the parser

The FST behavior is defined by the files stored in `fst` (lexical dictionary and configuration files) and `fst/lexc` (morphological rules). Any of these files can be edited to change the behavior of the parser.

Each time the FST is initialized, a full copy of the parser is saved in the `fst/foma` directory. Once created, you can independently troubleshoot/modify those files and feed them to the `foma` process.

Note: if you are running with Docker, you will need to navigate into the container to inspect the files written there. Try `docker run -it git_fst /bin/bash` and `ls fst/foma`.

## etc

Unit tests are stored in `test*.py` files; FST output tests are stored in `test_output*.py` files.

To run tests: run `python -m unittest` in your virtual environment.

See `/docs` for further description.

## Acknowledgement

This project was created with the support of a Documenting Endangered Languages fellowship from the National Endowment for the Humanities and the National Science Foundation. Any views, findings, conclusions, or recommendation expressed in this (publication/program/website) do not necessarily reflect those of the NEH and the NSF.
