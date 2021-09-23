# Dictionary categories

Every lexical item in the dictionary (`/fst/dict.csv`) requires a *category* to be successfully imported into the FST. Then its category determines its morphological behavior. This document explains the categories used in the dictionary and how they are interpreted in the context of the analyzer.

## Pressures of the endangered-language context

Gitksan is an endangered language that is undergoing active documentation. This resource serves as the initial attempt at a detailed description of syntactic and morphological categories (Tarpent's 1987 grammar of Nisg̲a'a is a valuable related resource and has been heavily referenced in development of these categories). The dictionary file used in this project is also shared with a publically-accessible talking dictionary website in use by members of the speech community, including language learners and teachers. This places some constraints on the the structure of the dictionary and nature of category labels.

For the purposes of the analyzer, categories are only required to distinguish the specific *morphological* behavior of groups of stems. This relates strictly to their ability to combine with inflectional morphemes and clitics. Additional syntactic or semantic properties are irrelevant. The analyzer only reflects what is morphologically possible for a word, versus what is morphologically impossible (for example, whether a Series I ergative clitic can attach to a preverbal particle; there are words which can take all clitics, only third person clitics, or may not have any clitic, which all have similar syntactic behavior).

A streamlined analyzer would include only the most necessary morphological categories in its lexical description. However, the endangered-language context requires the development of multipurpose resources. The lexical categories used in this dictionary -- the only dictionary which yet includes any lexical category information -- will be referenced in later language-learning efforts, including the development of curricula and pedagogical grammars. This means that the categories used should reflect additional important distinctions that are critical to understanding the holistic behavior of groups of words. This would include their major syntactic properties (for example, the ability to subordinate a clause, triggering dependent-style inflection).  A large number of categories may be required to effectively convey the necessary morphological and syntactic distinctions in the language to produce a descriptively adequate resource. In addition, semantic categorization can be useful to support vocabulary acquisition.

However, since the dictionary is public-facing, there is also a global pressure to use intuitive, less-technical terminology which learners and teachers may be able to understand without much explanation. Since there are only so many common or intuitive grammatical terms, this means there is a pressure to make fewer category distinctions.

These opposing pressures (specific descriptive adequacy, broad descriptive adequacy, and public understandability) make the development of this set of lexical categories something of a balancing act. Such is the nature of multipurpose-resource development common in endangered language documentation. This resource remains a work in progress.

## Categories

### Address form

A family/kinship term used in a vocative way, as a means of direct address. Not expected to take any inflection at all.

### Adverb

These are elements which either appear after the verb's arguments or in fronted position. They differ from nouns in that they are not typically used as arguments themselves, as evidenced by their lack of verbal agreement or argument-like extraction marking when fronted. In addition, as non-arguments they are not preceded by a preposition or oblique marker, whereas nouns would require such a licenser.

### Auxiliary

A preverbal element which modifies the main clause/verb, and can host both Series I ergative clitics and second-position clitics. Usually derived from an intransitive verb, and contributing tense, aspect, or mood-related information.

Examples: *nee* (NEG), *yukw* (PROG), *sgi* (should)

### Clause modifier

These are elements which precede the main verb or predicate of a clause. They differ from preverbs in that they can often be separated from the verb by subordinators or other markers, and they can typically host the third-person Series I ergative clitic. They differ from (regular) modifiers in that they typically only modify verbal predicates with some clausal structure, not nouns/arguments.

Elements in this category may or may not be syntactic subordinators (or "dependent markers"); they do not form a syntactic natural class. Rather, they are a morphological natural class in that they may host only the third-person ergative clitics (in contrast to subordinators).

Examples: *k̲'ay* ??

### Command

These are lexical items which stand alone as commands. They do not morphologically inflect as verbs do, though they may have both singular and plural-directed variations.

### Intransitive verb

These are verbs which take a single argument: an absolutive subject. They can take Series II suffixal inflection for that argument, and can also host attributives, the intransitive subject extraction suffix, and the third-plural semipronoun *-da*. They can host second-position clitics and nominal connective enclitics.

Example: *bax̲*, *yook̲xw*

### Modal

These elements appear in clauses to situate the event with respect to possibility and future orientation. There are only two known and they have different syntactic behavior in terms of subordination, but similar morphological behavior in that they may host any of the Series I ergative clitics.

Examples: *dim*, *ji*

### Modifier

These are category-neutral elements which may precede nouns, verbs, and sometimes adverbs. They do not inflect or host any clitics, but may form a compound with a following noun or verb. In the verbal domain, they may be separated from the main verb by other preverbal material such as subordinators or auxiliaries.

Examples: *sim*, *'wii*, *wag̲ayt*

### Noun

These are nouns. They can be used as verbal predicates, though they tend only to do so in traditionally copular contexts; otherwise they are typically used as arguments, and unlike verbs may do so without any morphological marking of relativization. They can take Series II suffixal inflection to mark a possessor, and can also host attributives, the intransitive subject extraction marker (for a possessor), second-position clitics, nominal connectives for a following noun.

Currently these are also able to appear in special possessive constructions where *xw* or the T-morpheme appears after the noun and before the Series II possessor inflection.

Examples: *gat*, *xbiist*, *lax̲'u*

### Number

These are a subclass of quantifiers which refer to cardinal numbers used in counting. Numbers are also part classifier, with different numeral series being used based on what is being counted (humans, animals, etc).

### Particle

These are free elements which do not inflect in any way.

Examples: *ee'e*

### Plural (?)

### Prenoun

These are elements which appear exclusively before nouns, modifying them. Some may trigger the noun's conversion to some other category. That is, some of these may be verbalizers which attach to a noun to form a verb.

Examples: *ts'im*, *sii*, *sin*

### Preposition

These are a closed class of elements which introduce nouns that are not arguments of a verb, such as instruments or locations. Prepositions are, morphologically, a heterogeneous set: most take Series II inflection when introducing a pronoun and a nominal connective when introducing a noun, but some do not inflect, and those which take connectives may differ (even between speakers) in whether that connective is *t* or *s* for a determinate noun.

Prepositions are handled on a case-by-case basis in the parser; some are labeled as "agreeing preposition" (inflects) or "conjunction" (does not inflect) in the dictionary resource to designate their distinct morphological properties.

### Preverb

This is an element which appear exclusively before verbs, modifying them. They can sometimes concatenate with the verb. They never serve as a host to any kind of inflection or clitic, and cannot be split from the verb by a subordinator or auxiliary (in contrast to modifiers).

### Relational noun (?)

Under construction: These are nouns which are typically possessed, inflecting with Series II inflection or a nominal marker, to designate some property of, part of, or spatial relation to the possessor -- AND/OR these elements have a T-morpheme (or similar) immediately preceding their inflection.

Examples: *sgan*, *sdo'o*, *g̲adaax*?

### Psychological verb (?)

An subtype of intransitive verb which exclusively takes a possessed noun *g̲oot-X* (X's heart) as its argument, yielding a mental or emotional predicate that holds of the possessor. Morphologically, these verbs combine with *g̲oot* using intransitive agreement and a connective (*=hl*), attributive morphology (*-m*), or through bare juxtaposition.

The argument *g̲oot* cannot be extracted but its possessor can be. Upon extraction of the possessor, extraction morphology (*-it*) is obligatory on *g̲oot*, but need not appear on the psych verb.

Examples: *luu'am* (happy), *wantxw* (worry), *g̲etxw* (sad, disappointed)

### Quantifier

These are quantificational elements. They can be used to modify (quantify) nominal arguments, and in this use are concatenated with an attributive, nominal connective, or subject extraction marker (?) plus nominal connective. They can be used to quantify over pronouns as well, and in this case will take Series II inflection to indicate the pronoun. They can also be used as predicates, but in this usage do not take obligatory Series II inflection as intransitive verbs do.

### Subordinator

These are preverbal elements which, in addition to syntactically subordinating the associated clause and main verb, can serve as a host to the Series I ergative clitics. They cannot host any other kind of clitic.

### Transitive verb

These are verbs which take two arguments: an ergative subject and an absolutive object. They can take Series II suffixal inflection for the object, or they can take a transitive vowel *plus* Series II suffixal inflection for the ergative subject. They can host second-position clitics and nominal connective enclitics only after Series II inflection.

Some may inherently be T-class transitive verbs; those verbs which are not can additionally have the T-morpheme attached to them in combination with some preverbal trigger.

Example: *gup*, *yoog̲an*

### (Verb)

A verb with unknown subcategory. (Not imported to FST)