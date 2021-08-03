import unittest
from test import TestFSTOutput

"""
This suite checks that Gitksan stems appear in the correct form
when inflectional suffixes are attached to them. Alternates based on
final consonant and some other specific properties.
These tests use the actual FST (v1) as a dependency.
"""

CONFIG = 'config/basic_east.json'

class TestPlainStops(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "s$ip",
                "g_$oot",
                "kw'$ats", # TEST, find a real N
                "t'$ak", # TEST, find a real N
                "l$akw",
                "'$eek_",
                "j$ok_",
                "ay$ook_",
            ]
        }
        super().setUpClass(CONFIG, test_stems)

    def test_plainP(self):
        stem = 's$ip+N'
        expected_map = [
            ('-1SG',    ["sibi'y"]),
            ('-1PL',    ["sibi'm"]),
            ('-2SG',    ["sibin"]),
            ('-2PL',    ["sipsi'm"]),
            ('-3',      ["sipt"]),
            ('-3PL',    ["sipdiit"]),
            ('-3=CN',   ["siphl"]),
            ('-3=PN',   ["sips"]),
            ('-SX',     ["sibit"]),
            ('-ATTR',   ["sibim", "siba"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_plainT(self):
        stem = 'g_$oot+N'
        expected_map = [
            ('-1SG',    ["g̲oodi'y"]),
            ('-1PL',    ["g̲oodi'm"]),
            ('-2SG',    ["g̲oodin"]),
            ('-2PL',    ["g̲ootsi'm"]),
            ('-3',      ["g̲oott"]),
            ('-3PL',    ["g̲ootdiit"]),
            ('-3=CN',   ["g̲oothl"]),
            ('-3=PN',   ["g̲oots"]),
            ('-SX',     ["g̲oodit"]),
            ('-ATTR',   ["g̲oodim", "g̲ooda"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_plainTS(self):
        stem = "kw'$ats+N"
        expected_map = [
            ('-1SG',    ["kw'aji'y"]),
            ('-1PL',    ["kw'aji'm"]),
            ('-2SG',    ["kw'ajin"]),
            ('-2PL',    ["kw'ajisi'm"]),
            ('-3',      ["kw'atst"]),
            ('-3PL',    ["kw'atsdiit"]),
            ('-3=CN',   ["kw'atshl"]),
            ('-3=PN',   ["kw'ats"]),
            ('-SX',     ["kw'ajit"]),
            ('-ATTR',   ["kw'ajim", "kw'aja"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_plainK(self):
        stem = "t'$ak+N"
        expected_map = [
            ('-1SG',    ["t'agi'y"]),
            ('-1PL',    ["t'agi'm"]),
            ('-2SG',    ["t'agin"]),
            ('-2PL',    ["t'aksi'm"]),
            ('-3',      ["t'akt"]),
            ('-3PL',    ["t'akdiit"]),
            ('-3=CN',   ["t'akhl"]),
            ('-3=PN',   ["t'aks"]),
            ('-SX',     ["t'agit"]),
            ('-ATTR',   ["t'agim", "t'aga"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_plainKW(self):
        stem = 'l$akw+N'
        expected_map = [
            ('-1SG',    ["lagwi'y"]),
            ('-1PL',    ["lagwi'm", "lagu'm"]),
            ('-2SG',    ["lagwin"]),
            ('-2PL',    ["lakwsi'm"]),
            ('-3',      ["lakwt"]),
            ('-3PL',    ["lakwdiit"]),
            ('-3=CN',   ["lakwhl"]),
            ('-3=PN',   ["lakws"]),
            ('-SX',     ["lagwit"]),
            ('-ATTR',   ["lagwim", "lagum", "lagwa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_plainK_(self):
        stem = "'$eek_+N"
        expected_map = [
            ('-1SG',    ["eeg̲a'y"]),
            ('-1PL',    ["eeg̲a'm"]),
            ('-2SG',    ["eeg̲an"]),
            ('-2PL',    ["eek̲si'm"]),
            ('-3',      ["eek̲t"]),
            ('-3PL',    ["eek̲diit"]),
            ('-3=CN',   ["eek̲hl"]),
            ('-3=PN',   ["eek̲s"]),
            ('-SX',     ["eeg̲at"]),
            ('-ATTR',   ["eeg̲am", "eeg̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_plainOK_(self):
        stem = "j$ok_+N"
        expected_map = [
            ('-1SG',    ["jog̲a'y", "jog̲o'y"]),
            ('-1PL',    ["jog̲a'm", "jog̲o'm"]),
            ('-2SG',    ["jog̲an", "jog̲on"]),
            ('-2PL',    ["jok̲si'm"]),
            ('-3',      ["jok̲t"]),
            ('-3PL',    ["jok̲diit"]),
            ('-3=CN',   ["jok̲hl"]),
            ('-3=PN',   ["jok̲s"]),
            ('-SX',     ["jog̲at", "jog̲ot"]),
            ('-ATTR',   ["jog̲am", "jog̲om", "jog̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_plainOOK_(self):
        stem = "'ay$ook_+N"
        expected_map = [
            ('-1SG',    ["ayoog̲a'y"]),
            ('-1PL',    ["ayoog̲a'm"]),
            ('-2SG',    ["ayoog̲an"]),
            ('-2PL',    ["ayook̲si'm"]),
            ('-3',      ["ayook̲t"]),
            ('-3PL',    ["ayook̲diit"]),
            ('-3=CN',   ["ayook̲hl"]),
            ('-3=PN',   ["ayook̲s"]),
            ('-SX',     ["ayoog̲at"]),
            ('-ATTR',   ["ayoog̲am", "ayoog̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

class TestGlottalStops(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "s$ip'",     # find a real glottal P
                "hl$it'",
                "n$aasik'",
                "ts'$uuts'",
                "giky'$otl'",
                "t'$ikw'",
                "han$ak_'",
                "ts'$ok_'",
            ]
        }
        super().setUpClass(CONFIG, test_stems)

    def test_glottP(self):
        stem = "s$ip'+N"
        expected_map = [
            ('-1SG',    ["sip'i'y"]),
            ('-1PL',    ["sip'i'm"]),
            ('-2SG',    ["sip'in"]),
            ('-2PL',    ["sip'si'm"]),
            ('-3',      ["sip't"]),
            ('-3PL',    ["sip'diit"]),
            ('-3=CN',   ["sip'hl"]),
            ('-3=PN',   ["sip's"]),
            ('-SX',     ["sip'it"]),
            ('-ATTR',   ["sip'im", "sip'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_glottT(self):
        stem = "hl$it'+N"
        expected_map = [
            ('-1SG',    ["hlit'i'y"]),
            ('-1PL',    ["hlit'i'm"]),
            ('-2SG',    ["hlit'in"]),
            ('-2PL',    ["hlit'si'm"]),
            ('-3',      ["hlit't"]),
            ('-3PL',    ["hlit'diit"]),
            ('-3=CN',   ["hlit'hl"]),
            ('-3=PN',   ["hlit's"]),
            ('-SX',     ["hlit'it"]),
            ('-ATTR',   ["hlit'im", "hlit'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_glottTS(self):
        stem = "ts'$uuts'+N"
        expected_map = [
            ('-1SG',    ["ts'uuts'i'y"]),
            ('-1PL',    ["ts'uuts'i'm"]),
            ('-2SG',    ["ts'uuts'in"]),
            ('-2PL',    ["ts'uuts'isi'm"]), # ts'uuts'si'm?
            ('-3',      ["ts'uuts't"]),
            ('-3PL',    ["ts'uuts'diit"]),
            ('-3=CN',   ["ts'uuts'hl"]),
            ('-3=PN',   ["ts'uuts'"]),      # ts'uuts's?
            ('-SX',     ["ts'uuts'it"]),
            ('-ATTR',   ["ts'uuts'im", "ts'uuts'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_glottTL(self):
        stem = "giky'$otl'+N"
        expected_map = [
            ('-1SG',    ["giky'otl'i'y"]),
            ('-1PL',    ["giky'otl'i'm"]),
            ('-2SG',    ["giky'otl'in"]),
            ('-2PL',    ["giky'otl'si'm"]),
            ('-3',      ["giky'otl't"]),
            ('-3PL',    ["giky'otl'diit"]),
            ('-3=CN',   ["giky'otl'hl"]),
            ('-3=PN',   ["giky'otl's"]),
            ('-SX',     ["giky'otl'it"]),
            ('-ATTR',   ["giky'otl'im", "giky'otl'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_glottalK(self):
        stem = "n$aasik'+N"
        expected_map = [
            ('-1SG',    ["naasik'i'y"]),
            ('-1PL',    ["naasik'i'm"]),
            ('-2SG',    ["naasik'in"]),
            ('-2PL',    ["naasik'si'm"]),
            ('-3',      ["naasik't"]),
            ('-3PL',    ["naasik'diit"]),
            ('-3=CN',   ["naasik'hl"]),
            ('-3=PN',   ["naasik's"]),
            ('-SX',     ["naasik'it"]),
            ('-ATTR',   ["naasik'im", "naasik'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_glottKW(self):
        stem = "t'$ikw'+N"
        expected_map = [
            ('-1SG',    ["t'ikw'i'y"]),
            ('-1PL',    ["t'ikw'i'm", "t'ik'u'm"]),
            ('-2SG',    ["t'ikw'in"]),
            ('-2PL',    ["t'ikw'si'm"]),
            ('-3',      ["t'ikw't"]),
            ('-3PL',    ["t'ikw'diit"]),
            ('-3=CN',   ["t'ikw'hl"]),
            ('-3=PN',   ["t'ikw's"]),
            ('-SX',     ["t'ikw'it"]),
            ('-ATTR',   ["t'ikw'im", "t'ik'um", "t'ikw'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_glottK_(self):
        stem = "han$ak_'+N"
        expected_map = [
            ('-1SG',    ["hanak̲'a'y"]),
            ('-1PL',    ["hanak̲'a'm"]),
            ('-2SG',    ["hanak̲'an"]),
            ('-2PL',    ["hanak̲'si'm"]),
            ('-3',      ["hanak̲'t"]),
            ('-3PL',    ["hanak̲'diit"]),
            ('-3=CN',   ["hanak̲'hl"]),
            ('-3=PN',   ["hanak̲'s"]),
            ('-SX',     ["hanak̲'at"]),
            ('-ATTR',   ["hanak̲'am", "hanak̲'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_glottOK_(self):
        stem = "ts'$ok_'+N"
        expected_map = [
            ('-1SG',    ["ts'ok̲'a'y", "ts'ok̲'o'y"]),
            ('-1PL',    ["ts'ok̲'a'm", "ts'ok̲'o'm"]),
            ('-2SG',    ["ts'ok̲'on", "ts'ok̲'an"]),
            ('-2PL',    ["ts'ok̲'si'm"]),
            ('-3',      ["ts'ok̲'t"]),
            ('-3PL',    ["ts'ok̲'diit"]),
            ('-3=CN',   ["ts'ok̲'hl"]),
            ('-3=PN',   ["ts'ok̲'s"]),
            ('-SX',     ["ts'ok̲'at", "ts'ok̲'ot"]),
            ('-ATTR',   ["ts'ok̲'am", "ts'ok̲'om", "ts'ok̲'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

class TestFricatives(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "m$aas",
                "k'$uuhl",
                "l$ax",
                "l$aaxw",
                "'n$ax_",
                "n$ox_",
            ]
        }
        super().setUpClass(CONFIG, test_stems)

    def test_fricS(self):
        stem = "m$aas+N"
        expected_map = [
            ('-1SG',    ["maasi'y"]),
            ('-1PL',    ["maasi'm"]),
            ('-2SG',    ["maasin"]),
            ('-2PL',    ["maasisi'm"]),
            ('-3',      ["maast"]),
            ('-3PL',    ["maasdiit"]),
            ('-3=CN',   ["maashl"]),
            ('-3=PN',   ["maas"]),
            ('-SX',     ["maasit"]),
            ('-ATTR',   ["maasim", "maasa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_fricHL(self):
        stem = "k'$uuhl+N"
        expected_map = [
            ('-1SG',    ["k'uuhli'y"]),
            ('-1PL',    ["k'uuhli'm"]),
            ('-2SG',    ["k'uuhlin"]),
            ('-2PL',    ["k'uuhlsi'm"]),
            ('-3',      ["k'uuhlt"]),
            ('-3PL',    ["k'uuhldiit"]),
            ('-3=CN',   ["k'uuhl"]),
            ('-3=PN',   ["k'uuhls"]),
            ('-SX',     ["k'uuhlit"]),
            ('-ATTR',   ["k'uuhlim", "k'uuhla"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_fricX(self):
        stem = "l$ax+N"  # not sure if these should also be optionally glided
        expected_map = [
            ('-1SG',    ["layi'y"]),
            ('-1PL',    ["layi'm"]),
            ('-2SG',    ["layin"]),
            ('-2PL',    ["laxsi'm"]),
            ('-3',      ["laxt"]),
            ('-3PL',    ["laxdiit"]),
            ('-3=CN',   ["laxhl"]),
            ('-3=PN',   ["laxs"]),
            ('-SX',     ["layit"]),
            ('-ATTR',   ["layim", "laya"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_fricXW(self):
        stem = "l$aaxw+N"
        expected_map = [
            ('-1SG',    ["laawi'y", "laaxwi'y"]),
            ('-1PL',    ["laawi'm", "laawu'm", "laaxwi'm", "laaxu'm"]),
            ('-2SG',    ["laawin", "laaxwin"]),
            ('-2PL',    ["laaxwsi'm"]),
            ('-3',      ["laaxwt"]),
            ('-3PL',    ["laaxwdiit"]),
            ('-3=CN',   ["laaxwhl"]),
            ('-3=PN',   ["laaxws"]),
            ('-SX',     ["laawit", "laaxwit"]),
            ('-ATTR',   ["laawim", "laawum", "laawa", "laaxwim", "laaxum", "laaxwa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_fricX_(self):
        stem = "'n$ax_+N"
        expected_map = [
            ('-1SG',    ["'naha'y", "'nax̲a'y"]),
            ('-1PL',    ["'naha'm", "'nax̲a'm"]),
            ('-2SG',    ["'nahan", "'nax̲an"]),
            ('-2PL',    ["'nax̲si'm"]),
            ('-3',      ["'nax̲t"]),
            ('-3PL',    ["'nax̲diit"]),
            ('-3=CN',   ["'nax̲hl"]),
            ('-3=PN',   ["'nax̲s"]),
            ('-SX',     ["'nahat", "'nax̲at"]),
            ('-ATTR',   ["'naham", "'naha", "'nax̲am", "'nax̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_fricOX_(self):
        stem = "n$ox_+N"
        expected_map = [
            ('-1SG',    ["noha'y", "noho'y", "nox̲a'y", "nox̲o'y"]),
            ('-1PL',    ["noha'm", "noho'm", "nox̲a'm", "nox̲o'm"]),
            ('-2SG',    ["nohan", "nohon", "nox̲an", "nox̲on"]),
            ('-2PL',    ["nox̲si'm"]),
            ('-3',      ["nox̲t"]),
            ('-3PL',    ["nox̲diit"]),
            ('-3=CN',   ["nox̲hl"]),
            ('-3=PN',   ["nox̲s"]),
            ('-SX',     ["nohat", "nohot", "nox̲at", "nox̲ot"]),
            ('-ATTR',   ["noham", "nohom", "noha", "nox̲am", "nox̲om", "nox̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

class TestPlainSonorants(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "g$um",
                "b$an",
                "haw$il",
                "g_awk_'$aw",
                # "y",
            ]
        }
        super().setUpClass(CONFIG, test_stems)

    def test_plainM(self):
        stem = 'g$um+N'
        expected_map = [
            ('-1SG',    ["gumi'y"]),
            ('-1PL',    ["gumi'm", "gumu'm"]),
            ('-2SG',    ["gumin"]),
            ('-2PL',    ["gumsi'm"]),
            ('-3',      ["gumt"]),
            ('-3PL',    ["gumdiit"]),
            ('-3=CN',   ["gumhl"]),
            ('-3=PN',   ["gums"]),
            ('-SX',     ["gumit", "gumt"]),
            ('-ATTR',   ["gumim", "gumum", "guma"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_plainN(self):
        stem = 'b$an+N'
        expected_map = [
            ('-1SG',    ["bani'y"]),
            ('-1PL',    ["bani'm"]),
            ('-2SG',    ["banin"]),
            ('-2PL',    ["bansi'm"]),
            ('-3',      ["bant"]),
            ('-3PL',    ["bandiit"]),
            ('-3=CN',   ["banhl"]),
            ('-3=PN',   ["bans"]),
            ('-SX',     ["banit", "bant"]),
            ('-ATTR',   ["banim", "bana"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_plainL(self):
        stem = "haw$il+N"
        expected_map = [
            ('-1SG',    ["hawili'y"]),
            ('-1PL',    ["hawili'm"]),
            ('-2SG',    ["hawilin"]),
            ('-2PL',    ["hawilsi'm"]),
            ('-3',      ["hawilt"]),
            ('-3PL',    ["hawildiit"]),
            ('-3=CN',   ["hawilhl"]),
            ('-3=PN',   ["hawils"]),
            ('-SX',     ["hawilit", "hawilt"]), # hawilt? hawilit?
            ('-ATTR',   ["hawilim", "hawila"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_plainW(self):
        stem = "g_awk_'$aw+N"
        expected_map = [
            ('-1SG',    ["g̲awk̲'awi'y"]),
            ('-1PL',    ["g̲awk̲'awi'm", "g̲awk̲'awu'm"]),
            ('-2SG',    ["g̲awk̲'awin"]),
            ('-2PL',    ["g̲awk̲'awsi'm"]),
            ('-3',      ["g̲awk̲'awt"]),
            ('-3PL',    ["g̲awk̲'awdiit"]),
            ('-3=CN',   ["g̲awk̲'awhl"]),
            ('-3=PN',   ["g̲awk̲'aws"]),
            ('-SX',     ["g̲awk̲'awit", "g̲awk̲'awt"]),
            ('-ATTR',   ["g̲awk̲'awim", "g̲awk̲'awum", "g̲awk̲'awa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

class TestGlottalSonorants(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "hl$aa'm",
                "lig$i'l",
                "mask_'ay$aa'y",
                "x_b$aa'w",
                "n$oo'o",
                # "ba'n",
            ]
        }
        super().setUpClass(CONFIG, test_stems)

    def test_glottalM(self):
        stem = "hl$aa'm+N"
        expected_map = [
            ('-1SG',    ["hlaa'mi'y"]),
            # ('-1PL',    ["hlaa'mi'm", "hlaa'mm"]), # ??
            ('-2SG',    ["hlaa'min"]),
            ('-2PL',    ["hlaa'msi'm"]),
            ('-3',      ["hlaa'mt"]),
            ('-3PL',    ["hlaa'mdiit"]),
            ('-3=CN',   ["hlaa'mhl"]),
            ('-3=PN',   ["hlaa'ms"]),
            ('-SX',     ["hlaa'mit"]), # ??
            ('-ATTR',   ["hlaa'mim", "hlaa'ma"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

#     def test_glottalN(self):
#         stem = "b$an+N"
#         expected_map = [
#             ('-1SG',    ["bani'y"]),
#             ('-1PL',    ["bani'm"]),
#             ('-2SG',    ["banin"]),
#             ('-2PL',    ["bansi'm"]),
#             ('-3',      ["bant"]),
#             ('-3PL',    ["bandiit"]),
#             ('-3=CN',   ["banhl"]),
#             ('-3=PN',   ["bans"]),
#             ('-SX',     ["bant"]),
#             ('-ATTR',   ["banim", "bana"]),
#         ]
#         for gloss, expected_forms in expected_map:
#             result_list = self.fst.generate(stem+gloss)
#             for form in expected_forms:
#                 with self.subTest(form=stem+gloss):
#                     self.assertIn(form, result_list)
#             self.assertEqual(len(result_list), len(expected_forms),
#                 "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_glottalL(self):
        stem = "lig$i'l+N"
        expected_map = [
            ('-1SG',    ["ligi'li'y"]),
            ('-1PL',    ["ligi'li'm"]),
            ('-2SG',    ["ligi'lin"]),
            ('-2PL',    ["ligi'lsi'm"]),
            ('-3',      ["ligi'lt"]),
            ('-3PL',    ["ligi'ldiit"]),
            ('-3=CN',   ["ligi'lhl"]),
            ('-3=PN',   ["ligi'ls"]),
            ('-SX',     ["ligi'lit"]),
            ('-ATTR',   ["ligi'lim", "ligi'la"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_glottalY(self):
        stem = "mask_'ay$aa'y+N"
        expected_map = [
            ('-1SG',    ["mask̲'ayaa'y"]), # ??
            ('-1PL',    ["mask̲'ayaa'yi'm"]),
            ('-2SG',    ["mask̲'ayaa'yin"]),
            ('-2PL',    ["mask̲'ayaa'ysi'm"]),
            ('-3',      ["mask̲'ayaa'yt"]),
            ('-3PL',    ["mask̲'ayaa'ydiit"]),
            ('-3=CN',   ["mask̲'ayaa'yhl"]),
            ('-3=PN',   ["mask̲'ayaa'ys"]),
            ('-SX',     ["mask̲'ayaa'yit"]),
            ('-ATTR',   ["mask̲'ayaa'yim", "mask̲'ayaa'ya"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_glottalW(self):
        stem = "x_b$aa'w+N"
        expected_map = [
            ('-1SG',    ["x̲baa'wi'y"]),
            ('-1PL',    ["x̲baa'wi'm", "x̲baa'u'm"]),
            ('-2SG',    ["x̲baa'win"]),
            ('-2PL',    ["x̲baa'wsi'm"]),
            ('-3',      ["x̲baa'wt"]),
            ('-3PL',    ["x̲baa'wdiit"]),
            ('-3=CN',   ["x̲baa'whl"]),
            ('-3=PN',   ["x̲baa'ws"]),
            # ('-SX',     ["x̲baa'wit", "x̲baa'ut"]),  # haven't applied this yet, keep in mind
            ('-ATTR',   ["x̲baa'wim", "x̲baa'um", "x̲baa'wa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_glottalStop(self):
        stem = "n$oo'o+N"
        expected_map = [
            ('-1SG',    ["noo'o'y"]),
            ('-1PL',    ["noo'o'm"]),
            ('-2SG',    ["noo'on"]),
            ('-2PL',    ["noo'osi'm"]),
            ('-3',      ["noo'ot"]),
            ('-3PL',    ["noo'odiit"]),
            ('-3=CN',   ["noo'ohl"]),
            ('-3=PN',   ["noo'os"]),
            ('-SX',     ["noo'ot"]),
            ('-ATTR',   ["noo'om", "noo'a"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

class TestVowels(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "w$a",
                "ha'niig$ilbilsa",
                "gy$uu",
                "majag_al$ee",
                "k_'$esii",
            ],
            'IntransitiveVerb': ['y$ee']
        }
        super().setUpClass(CONFIG, test_stems)

    def test_shortA(self):
        stem = "w$a+N"
        expected_map = [
            ('-1SG',    ["wa'y"]),
            ('-1PL',    ["wa'm"]),
            ('-2SG',    ["wan"]),
            ('-2PL',    ["wasi'm"]),
            ('-3',      ["wat"]),
            ('-3PL',    ["wadiit"]),
            ('-3=CN',   ["wahl"]),
            ('-3=PN',   ["was"]),
            ('-SX',     ["wat"]),
            ('-ATTR',   ["wam", "waha"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_shortAlonger(self):
        stem = "ha'niig$ilbilsa+N"
        expected_map = [
            ('-1SG',    ["ha'niigilbilsa'y"]),
            ('-1PL',    ["ha'niigilbilsa'm"]),
            ('-2SG',    ["ha'niigilbilsan"]),
            ('-2PL',    ["ha'niigilbilsasi'm"]),
            ('-3',      ["ha'niigilbilsat"]),
            ('-3PL',    ["ha'niigilbilsadiit"]),
            ('-3=CN',   ["ha'niigilbilsahl"]),
            ('-3=PN',   ["ha'niigilbilsas"]),
            ('-SX',     ["ha'niigilbilsat"]),
            ('-ATTR',   ["ha'niigilbilsam", "ha'niigilbilsaha"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_longU(self):
        stem = "gy$uu+N"
        expected_map = [
            ('-1SG',    ["gyuu'y"]),
            ('-1PL',    ["gyuu'm"]),
            ('-2SG',    ["gyuun"]),
            ('-2PL',    ["gyuusi'm"]),
            ('-3',      ["gyuut"]),
            ('-3PL',    ["gyuudiit"]),
            ('-3=CN',   ["gyuuhl"]),
            ('-3=PN',   ["gyuus"]),
            ('-SX',     ["gyuut"]),
            ('-ATTR',   ["gyuum", "gyuuha"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_longE(self):
        stem = "y$ee+VI"
        expected_map = [
            ('-1SG',    ["yee'y"]),
            ('-1PL',    ["yee'm"]),
            # ('-2SG',    ["yeen", "yin"]), # requires maximal parser :\
            ('-2PL',    ["yeesi'm"]),
            ('-3',      ["yeet"]),
            ('-3=CN',   ["yeehl"]),
            ('-3=PN',   ["yees"]),
            ('-SX',     ["yeet"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_longElonger(self):
        stem = "majag_al$ee+N"
        expected_map = [
            ('-1SG',    ["majag̲alee'y"]),
            ('-1PL',    ["majag̲alee'm"]),
            ('-2SG',    ["majag̲aleen"]),
            ('-2PL',    ["majag̲aleesi'm"]),
            ('-3',      ["majag̲aleet"]),
            ('-3PL',    ["majag̲aleediit"]),
            ('-3=CN',   ["majag̲aleehl"]),
            ('-3=PN',   ["majag̲alees"]),
            ('-SX',     ["majag̲aleet"]),
            ('-ATTR',   ["majag̲aleem", "majag̲aleeha"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_longI(self):
        stem = "k_'$esii+N"
        expected_map = [
            ('-1SG',    ["k̲'esii'y"]),
            ('-1PL',    ["k̲'esii'm"]),
            ('-2SG',    ["k̲'esiin"]),
            ('-2PL',    ["k̲'esiisi'm"]),
            ('-3',      ["k̲'esiit"]),
            ('-3PL',    ["k̲'esiidiit"]),
            ('-3=CN',   ["k̲'esiihl"]),
            ('-3=PN',   ["k̲'esiis"]),
            ('-SX',     ["k̲'esiit"]),
            ('-ATTR',   ["k̲'esiim", "k̲'esiiha"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

class TestClusters(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "x_b$iist", # non-T
                "hal$ayt",
                "w$ilp",
                "s$ilkw",
                "ts'$amtx",
                "'$ax_xw",
                "biy$oosxw",
                "h$upx_",
            ]
        }
        super().setUpClass(CONFIG, test_stems)

    def test_ST(self):
        stem = "x_b$iist+N"
        expected_map = [
            ('-1SG',    ["x̲biisdi'y"]),
            ('-1PL',    ["x̲biisdi'm"]),
            ('-2SG',    ["x̲biisdin"]),
            ('-2PL',    ["x̲biistsi'm"]),
            ('-3',      ["x̲biistt"]),
            ('-3PL',    ["x̲biistdiit"]),
            ('-3=CN',   ["x̲biisthl"]),
            ('-3=PN',   ["x̲biists"]),
            ('-SX',     ["x̲biisdit"]),
            ('-ATTR',   ["x̲biisdim", "x̲biisda"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_YT(self):
        stem = "hal$ayt+N"
        expected_map = [
            ('-1SG',    ["halaydi'y"]),
            ('-1PL',    ["halaydi'm"]),
            ('-2SG',    ["halaydin"]),
            ('-2PL',    ["halaytsi'm"]),
            ('-3',      ["halaytt"]),
            ('-3PL',    ["halaytdiit"]),
            ('-3=CN',   ["halaythl"]),
            ('-3=PN',   ["halayts"]),
            ('-SX',     ["halaydit"]),
            ('-ATTR',   ["halaydim", "halayda"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_LP(self):
        stem = "w$ilp+N"
        expected_map = [
            ('-1SG',    ["wilbi'y"]),
            ('-1PL',    ["wilbi'm"]),
            ('-2SG',    ["wilbin"]),
            ('-2PL',    ["wilpsi'm"]),
            ('-3',      ["wilpt"]),
            ('-3PL',    ["wilpdiit"]),
            ('-3=CN',   ["wilphl"]),
            ('-3=PN',   ["wilps"]),
            ('-SX',     ["wilbit"]),
            ('-ATTR',   ["wilbim", "wilba"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_LKW(self):
        stem = "s$ilkw+N"
        expected_map = [
            ('-1SG',    ["silgwi'y"]),
            ('-1PL',    ["silgwi'm", "silgu'm"]),
            ('-2SG',    ["silgwin"]),
            ('-2PL',    ["silkwsi'm"]),
            ('-3',      ["silkwt"]),
            ('-3PL',    ["silkwdiit"]),
            ('-3=CN',   ["silkwhl"]),
            ('-3=PN',   ["silkws"]),
            ('-SX',     ["silgwit"]),
            ('-ATTR',   ["silgwim", "silgum", "silgwa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_TX(self):
        stem = "ts'$amtx+N"
        expected_map = [
            ('-1SG',    ["ts'amtxi'y"]),
            ('-1PL',    ["ts'amtxi'm"]),
            ('-2SG',    ["ts'amtxin"]),
            ('-2PL',    ["ts'amtxsi'm"]),
            ('-3',      ["ts'amtxt"]),
            ('-3PL',    ["ts'amtxdiit"]),
            ('-3=CN',   ["ts'amtxhl"]),
            ('-3=PN',   ["ts'amtxs"]),
            ('-SX',     ["ts'amtxit"]),
            ('-ATTR',   ["ts'amtxim", "ts'amtxa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_SXW(self):
        stem = "biy$oosxw+N"
        expected_map = [
            ('-1SG',    ["biyoosxwi'y"]),
            ('-1PL',    ["biyoosxwi'm", "biyoosxu'm"]),
            ('-2SG',    ["biyoosxwin"]),
            ('-2PL',    ["biyoosxwsi'm"]),
            ('-3',      ["biyoosxwt"]),
            ('-3PL',    ["biyoosxwdiit"]),
            ('-3=CN',   ["biyoosxwhl"]),
            ('-3=PN',   ["biyoosxws"]),
            ('-SX',     ["biyoosxwit"]),
            ('-ATTR',   ["biyoosxwim", "biyoosxum", "biyoosxwa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_X_XW(self):
        stem = "'$ax_xw+N"
        expected_map = [
            ('-1SG',    ["ax̲xwi'y"]),
            ('-1PL',    ["ax̲xwi'm", "ax̲xu'm"]),
            ('-2SG',    ["ax̲xwin"]),
            ('-2PL',    ["ax̲xwsi'm"]),
            ('-3',      ["ax̲xwt"]),
            ('-3PL',    ["ax̲xwdiit"]),
            ('-3=CN',   ["ax̲xwhl"]),
            ('-3=PN',   ["ax̲xws"]),
            ('-SX',     ["ax̲xwit"]),
            ('-ATTR',   ["ax̲xwim", "ax̲xum", "ax̲xwa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_PX_(self):
        stem = "h$upx_+N"
        expected_map = [
            ('-1SG',    ["hupx̲a'y"]),
            ('-1PL',    ["hupx̲a'm"]),
            ('-2SG',    ["hupx̲an"]),
            ('-2PL',    ["hupx̲si'm"]),
            ('-3',      ["hupx̲t"]),
            ('-3PL',    ["hupx̲diit"]),
            ('-3=CN',   ["hupx̲hl"]),
            ('-3=PN',   ["hupx̲s"]),
            ('-SX',     ["hupx̲at"]),
            ('-ATTR',   ["hupx̲am", "hupx̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

class TestTrVowel(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'TransitiveVerb': [
                "g$up",
                "t'$is",
                "g$in",
                "g_$e'n",
                "g$a'a", # add ga'a test to transitive vowel
                "hl$andin",
                "'w$a",
            ]
        }
        super().setUpClass(CONFIG, test_stems)

    def test_indepObstruent(self):
        stem = "g$up+VT"
        expected_map = [
            ('-TR-2SG',    ["gubin"]),
            ('-TR-2PL',    ["gubisi'm"]),
            ('-TR-3',      ["gubit"]),
            ('-TR-3PL',    ["gupdiit"]),
            ('-3',      ["gupt"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_indepSibilant(self):
        stem = "t'$is+VT"
        expected_map = [
            ('-TR-2SG',    ["t'isin"]),
            ('-TR-2PL',    ["t'isisi'm"]),
            ('-TR-3',      ["t'isit"]),
            ('-TR-3PL',    ["t'isdiit"]),
            ('-3',      ["t'ist"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_indepPlainSonorant(self):
        stem = "g$in+VT"
        expected_map = [
            ('-TR-2SG',    ["ginin"]),
            ('-TR-2PL',    ["ginisi'm"]),
            ('-TR-3',      ["ginit"]),
            ('-TR-3PL',    ["gindiit"]),
            ('-3',      ["gint"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_indepGlotSonorant(self):
        stem = "g_$e'n+VT"
        expected_map = [
            ('-TR-2SG',    ["g̲e'nin"]),
            ('-TR-2PL',    ["g̲e'nisi'm"]),
            ('-TR-3',      ["g̲e'nit"]),
            ('-TR-3PL',    ["g̲e'ndiit"]),
            ('-3',      ["g̲e'nt"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_indepGlotStop(self):
        stem = "g$a'a+VT"
        expected_map = [
            ('-TR-2SG',    ["ga'an"]),
            ('-TR-2PL',    ["ga'asi'm"]),
            ('-TR-3',      ["ga'at"]),
            ('-TR-3PL',    ["ga'adiit"]),
            ('-3',      ["ga'at"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                             "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_indepUnstressedSonorant(self):
        stem = "hl$andin+VT"
        expected_map = [
            ('-TR-2SG',    ["hlandinin"]),
            ('-TR-2PL',    ["hlandinsi'm"]),
            ('-TR-3',      ["hlandint"]),
            ('-TR-3PL',    ["hlandindiit"]),
            ('-3',      ["hlandint"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list, "expected for "+gloss)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_indepVowel(self):
        stem = "'w$a+VT"
        expected_map = [
            ('-TR-2SG',    ["'wayin"]),
            ('-TR-2PL',    ["'wayisi'm"]),
            ('-TR-3',      ["'wayit"]),
            ('-TR-3PL',    ["'wadiit"]),
            ('-3',      ["'wat"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

class TestBigT(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'TransitiveVerb': [
                "m$ahl(t)",
                "h$ats'(t)",
                "siw$a(t)",
                "g$uu(t)",
                "w$an",
                # get a glottal son + T in here
                # do tests for non-lexical big T as affix?
            ],
            'Noun': ['w$a']
        }
        super().setUpClass(CONFIG, test_stems)

    def test_native_postC(self):
        stem = "m$ahlT+VT"
        expected_map = [
            ('-TR-2SG',   ["mahldin"]),
            ('-TR-3',     ["mahldit"]),
            ('-TR-3PL',   ["mahldiit"]),
            ('-2SG',      ["mahlin"]),
            ('-3',        ["mahlit"]),
            ('-3PL',      ["mahldiit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))
    
    def test_native_no_extraT(self):
        stem = "m$ahlT+VT"
        unexpected_map = [
            '-T-3',
            '-T-TR-3',
        ]
        for gloss in unexpected_map:
            with self.subTest(form=stem+gloss):
                result_list = self.fst.generate(stem+gloss)
                self.assertEqual(len(result_list), 0,
                "{} should not be a possible path".format(stem+gloss))

    def test_native_postglottal(self):
        stem = "h$ats'T+VT"
        expected_map = [
            ('-TR-2SG',   ["hats'din"]),
            ('-TR-3',     ["hats'dit"]),
            ('-TR-3PL',   ["hats'diit"]),
            ('-2SG',      ["hats'in"]),
            ('-3',        ["hats'it"]),
            ('-3PL',      ["hats'diit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_native_postV(self):
        stem = "siw$aT+VT"
        expected_map = [
            ('-TR-2SG',   ["siwatdin"]),
            ('-TR-3',     ["siwatdit"]),
            ('-TR-3PL',   ["siwatdiit"]),
            ('-2SG',      ["siwadin"]),
            ('-3',        ["siwadit"]),
            ('-3PL',      ["siwatdiit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_postR_constructed(self):
        stem = "w$an+VT"
        expected_map = [
            ('-T-TR-2SG',   ["wandin"]),
            ('-T-TR-3',     ["wandit"]),
            ('-T-TR-3PL',   ["wandiit"]),
            ('-T-2SG',      ["wandin"]),
            ('-T-3',        ["wandit"]),
            ('-T-3PL',      ["wandiit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                             "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_postV_constructed(self):
        stem = "w$a+N"
        expected_map = [
            ('-T-3',        ["wadit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                             "{} should have {} results".format(stem+gloss, len(expected_forms)))


class TestIrregulars(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'IntransitiveVerb': [
                "gip$aykw",
                "'$algax_",
                "l$imx",
                # "gitxs$animx_",
            ],
        }
        super().setUpClass(CONFIG, test_stems)

    def test_gipaykw_voicing(self):
        stem = "gip$aykw+VI"
        expected_map = [
            ('',   ["gipaykw"]),
            ('-3',   ["gipaykwt"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_hardeningX_(self):
        stem = "'$algax_+VI"
        expected_map = [
            ('-1SG',    ["algag̲a'y", "algax̲a'y"]),
            ('-2PL',    ["algax̲si'm"]),
            ('-3',      ["algax̲t"]),
            ('-SX',     ["algag̲at", "algax̲at"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_vocalizedX(self):
        stem = "l$imx+VI"
        expected_map = [
            ('-1SG',    ["limi'y"]),
            ('-2PL',    ["limxsi'm"]),
            ('-3',      ["limxt"]),
            ('-SX',     ["limit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, len(expected_forms)))


@unittest.skip("derivational morphemes no longer included")
class TestCausValAntip(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'IntransitiveVerb': [
                "y$ee",
                "s$ip",
                "y$ook_",
                "s$iip'",
                "w$an",
                "t$e'l",
                "gwil$a",
            ],
        }
        super().setUpClass(CONFIG, test_stems)

    def test_caus_sII(self):
        stem = "s$ip+VI-CAUS"
        expected_map = [
            ('-1SG',    ["sibini'y"]),
            ('-1PL',    ["sibini'm"]),
            ('-2SG',    ["sibinin"]),
            ('-2PL',    ["sibinsi'm"]),
            ('-3',      ["sibint"]),
            ('-3PL',      ["sibindiit"]),
            ('-TR-1SG',    ["sibini'y"]),
            ('-TR-1PL',    ["sibini'm"]),
            ('-TR-2SG',    ["sibinin"]),
            ('-TR-2PL',    ["sibinsi'm"]),
            ('-TR-3',      ["sibint"]),
            ('-TR-3PL',      ["sibindiit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                             "{} should have {} results".format(stem+gloss, len(expected_forms)))

    def test_caus_stem_types(self):
        expected_map = [
            ('y$ook_+VI-CAUS-3',    ["yoog̲ant"]),
            ('y$ee+VI-CAUS-3',      ["yeedint"]),
            ("s$iip'+VI-CAUS-3",    ["siip'int"]),
            ("w$an+VI-CAUS-3",      ["wandint"]),
            ("t$e'l+VI-CAUS-3",     ["te'ldint"]),  # t'e'lint?
            ("gwil$a+VI-CAUS-3",     ["gwiladint"]),  #
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(gloss)
            for form in expected_forms:
                with self.subTest(gloss=gloss):
                    self.assertIn(form, result_list)
            with self.subTest(gloss=gloss):
                self.assertEqual(len(result_list), len(expected_forms),
                                "{} should have {} results".format(result_list, len(expected_forms)))


if __name__ == '__main__':
    unittest.main()

# python -m unittest test
# python -m unittest discover # all test files in current dir
# python -m unittest discover -s tests # all test files in /tests
