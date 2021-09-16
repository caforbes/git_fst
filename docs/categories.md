# Dictionary categories

Every lexical item in the dictionary (`/fst/dict.csv`) requires a *category* to be successfully imported into the FST. Then, its category determines its morphological behavior. This document explains the categories used in the dictionary and FST found in this repository.

## Context and constraints

Gitksan is an endangered language that is undergoing active documentation. There has not yet been a detailed description of the full range of lexical categories in Gitksan, so this resource serves as an initial attempt (though Tarpent's grammar of Nisg̲a'a is a valuable related resource). 

The dictionary file used in this project is shared with a publically-accessible talking dictionary website in use by members of the speech community, including language learners and teachers. This places some constraints on the the structure of the dictionary and nature of category labels.

The lexical categories used in this dictionary will, in the future, form some of the basis for a broader language-learning curriculum, such as an accompanying pedagogical grammar. This means that the categories used should reflect important distinctions that are critical to understanding the holistic behavior of groups of words, including syntactic properties (for example, the ability to subordinate a clause, triggering dependent-style inflection).

For the purposes of the analyzer, however, categories are required to distinguish the specific *morphological* behavior of groups of stems. This relates strictly to their ability to combine with inflectional morphemes and clitics. Additional syntactic properties are irrelevant. It is important to create distinctions to reflect what is morphologically possible for a word, versus what is morphologically impossible (for example, whether a Series I ergative clitic can attach to a preverbal particle; there are words which can take all clitics, only third person clitics, or may not have any clitic, which all have similar syntactic behavior).

These two requirements conflict to some degree, indicating that a larger number of categories might be required to mark both the necessary morphological and syntactic distinctions at play. However, since the dictionary is public-facing, there is also a global pressure to use intuitive, less-technical terminology which learners and teachers may be able to understand without much explanation -- particularly given that no accompanying pedagogical resources exist yet. Since there are only so many common or intuitive grammatical terms, this means there is a pressure to make fewer category distinctions.

Developing the set of lexical categories for this resource is therefore a balancing act, and remains a work in progress.

## Dictionary structure

The primary obligatory columns in the dictionary file, for the purposes of its inclusion in the FST

## Categories

### Address form
### Adverb
### Auxiliary
### Clause modifier
### Command
### Intransitive verb
### Modal
### Modifier
### Noun
### Number
### Particle
### Plural
### Prenoun
### Preposition
- agreeing preposition
- conjunction
### Preverb
### Relational noun (?)
### Psychological verb
### Quantifier
### Subordinator
### Transitive verb
### (Verb)