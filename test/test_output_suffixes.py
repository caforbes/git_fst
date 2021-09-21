import unittest
from test import TestFSTOutput, BASIC_E

"""
This suite checks that Gitksan stems appear in the correct form
when inflectional suffixes are attached to them. Alternates based on
final consonant and some other specific properties.
These tests use the actual FST (v1) as a dependency.
"""

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
        super().setUpClass(BASIC_E, test_stems)

    def test_plainP(self):
        stem = 's$ip+N'
        expected_map = [
            ('-1SG.II',    ["sibi'y"]),
            ('-1PL.II',    ["sibi'm"]),
            ('-2SG.II',    ["sibin"]),
            ('-2PL.II',    ["sipsi'm"]),
            ('-3.II',      ["sipt"]),
            ('-3PL.II',    ["sipdiit"]),
            ('[-3.II]=CN',   ["siphl"]),
            ('[-3.II]=PN',   ["sips"]),
            ('-SX',     ["sibit"]),
            ('-ATTR',   ["sibim", "siba"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

    def test_plainT(self):
        stem = 'g_$oot+N'
        expected_map = [
            ('-1SG.II',    ["g̲oodi'y"]),
            ('-1PL.II',    ["g̲oodi'm"]),
            ('-2SG.II',    ["g̲oodin"]),
            ('-2PL.II',    ["g̲ootsi'm"]),
            ('-3.II',      ["g̲oott"]),
            ('-3PL.II',    ["g̲ootdiit"]),
            ('[-3.II]=CN',   ["g̲oothl"]),
            ('[-3.II]=PN',   ["g̲oots"]),
            ('-SX',     ["g̲oodit"]),
            ('-ATTR',   ["g̲oodim", "g̲ooda"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

    def test_plainTS(self):
        stem = "kw'$ats+N"
        expected_map = [
            ('-1SG.II',    ["kw'aji'y"]),
            ('-1PL.II',    ["kw'aji'm"]),
            ('-2SG.II',    ["kw'ajin"]),
            ('-2PL.II',    ["kw'ajisi'm"]),
            ('-3.II',      ["kw'atst"]),
            ('-3PL.II',    ["kw'atsdiit"]),
            ('[-3.II]=CN',   ["kw'atshl"]),
            ('[-3.II]=PN',   ["kw'ats"]),
            ('-SX',     ["kw'ajit"]),
            ('-ATTR',   ["kw'ajim", "kw'aja"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

    def test_plainK(self):
        stem = "t'$ak+N"
        expected_map = [
            ('-1SG.II',    ["t'agi'y"]),
            ('-1PL.II',    ["t'agi'm"]),
            ('-2SG.II',    ["t'agin"]),
            ('-2PL.II',    ["t'aksi'm"]),
            ('-3.II',      ["t'akt"]),
            ('-3PL.II',    ["t'akdiit"]),
            ('[-3.II]=CN',   ["t'akhl"]),
            ('[-3.II]=PN',   ["t'aks"]),
            ('-SX',     ["t'agit"]),
            ('-ATTR',   ["t'agim", "t'aga"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

    def test_plainKW(self):
        stem = 'l$akw+N'
        expected_map = [
            ('-1SG.II',    ["lagwi'y"]),
            ('-1PL.II',    ["lagwi'm", "lagu'm"]),
            ('-2SG.II',    ["lagwin"]),
            ('-2PL.II',    ["lakwsi'm"]),
            ('-3.II',      ["lakwt"]),
            ('-3PL.II',    ["lakwdiit"]),
            ('[-3.II]=CN',   ["lakwhl"]),
            ('[-3.II]=PN',   ["lakws"]),
            ('-SX',     ["lagwit"]),
            ('-ATTR',   ["lagwim", "lagum", "lagwa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

    def test_plainK_(self):
        stem = "'$eek_+N"
        expected_map = [
            ('-1SG.II',    ["eeg̲a'y"]),
            ('-1PL.II',    ["eeg̲a'm"]),
            ('-2SG.II',    ["eeg̲an"]),
            ('-2PL.II',    ["eek̲si'm"]),
            ('-3.II',      ["eek̲t"]),
            ('-3PL.II',    ["eek̲diit"]),
            ('[-3.II]=CN',   ["eek̲hl"]),
            ('[-3.II]=PN',   ["eek̲s"]),
            ('-SX',     ["eeg̲at"]),
            ('-ATTR',   ["eeg̲am", "eeg̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

    def test_plainOK_(self):
        stem = "j$ok_+N"
        expected_map = [
            ('-1SG.II',    ["jog̲a'y", "jog̲o'y"]),
            ('-1PL.II',    ["jog̲a'm", "jog̲o'm"]),
            ('-2SG.II',    ["jog̲an", "jog̲on"]),
            ('-2PL.II',    ["jok̲si'm"]),
            ('-3.II',      ["jok̲t"]),
            ('-3PL.II',    ["jok̲diit"]),
            ('[-3.II]=CN',   ["jok̲hl"]),
            ('[-3.II]=PN',   ["jok̲s"]),
            ('-SX',     ["jog̲at", "jog̲ot"]),
            ('-ATTR',   ["jog̲am", "jog̲om", "jog̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

    def test_plainOOK_(self):
        stem = "'ay$ook_+N"
        expected_map = [
            ('-1SG.II',    ["ayoog̲a'y"]),
            ('-1PL.II',    ["ayoog̲a'm"]),
            ('-2SG.II',    ["ayoog̲an"]),
            ('-2PL.II',    ["ayook̲si'm"]),
            ('-3.II',      ["ayook̲t"]),
            ('-3PL.II',    ["ayook̲diit"]),
            ('[-3.II]=CN',   ["ayook̲hl"]),
            ('[-3.II]=PN',   ["ayook̲s"]),
            ('-SX',     ["ayoog̲at"]),
            ('-ATTR',   ["ayoog̲am", "ayoog̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

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
        super().setUpClass(BASIC_E, test_stems)

    def test_glottP(self):
        stem = "s$ip'+N"
        expected_map = [
            ('-1SG.II',    ["sip'i'y"]),
            ('-1PL.II',    ["sip'i'm"]),
            ('-2SG.II',    ["sip'in"]),
            ('-2PL.II',    ["sip'si'm"]),
            ('-3.II',      ["sip't"]),
            ('-3PL.II',    ["sip'diit"]),
            ('[-3.II]=CN',   ["sip'hl"]),
            ('[-3.II]=PN',   ["sip's"]),
            ('-SX',     ["sip'it"]),
            ('-ATTR',   ["sip'im", "sip'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

    def test_glottT(self):
        stem = "hl$it'+N"
        expected_map = [
            ('-1SG.II',    ["hlit'i'y"]),
            ('-1PL.II',    ["hlit'i'm"]),
            ('-2SG.II',    ["hlit'in"]),
            ('-2PL.II',    ["hlit'si'm"]),
            ('-3.II',      ["hlit't"]),
            ('-3PL.II',    ["hlit'diit"]),
            ('[-3.II]=CN',   ["hlit'hl"]),
            ('[-3.II]=PN',   ["hlit's"]),
            ('-SX',     ["hlit'it"]),
            ('-ATTR',   ["hlit'im", "hlit'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

    def test_glottTS(self):
        stem = "ts'$uuts'+N"
        expected_map = [
            ('-1SG.II',    ["ts'uuts'i'y"]),
            ('-1PL.II',    ["ts'uuts'i'm"]),
            ('-2SG.II',    ["ts'uuts'in"]),
            ('-2PL.II',    ["ts'uuts'isi'm"]), # ts'uuts'si'm?
            ('-3.II',      ["ts'uuts't"]),
            ('-3PL.II',    ["ts'uuts'diit"]),
            ('[-3.II]=CN',   ["ts'uuts'hl"]),
            ('[-3.II]=PN',   ["ts'uuts'"]),      # ts'uuts's?
            ('-SX',     ["ts'uuts'it"]),
            ('-ATTR',   ["ts'uuts'im", "ts'uuts'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

    def test_glottTL(self):
        stem = "giky'$otl'+N"
        expected_map = [
            ('-1SG.II',    ["giky'otl'i'y"]),
            ('-1PL.II',    ["giky'otl'i'm"]),
            ('-2SG.II',    ["giky'otl'in"]),
            ('-2PL.II',    ["giky'otl'si'm"]),
            ('-3.II',      ["giky'otl't"]),
            ('-3PL.II',    ["giky'otl'diit"]),
            ('[-3.II]=CN',   ["giky'otl'hl"]),
            ('[-3.II]=PN',   ["giky'otl's"]),
            ('-SX',     ["giky'otl'it"]),
            ('-ATTR',   ["giky'otl'im", "giky'otl'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss, 
                                            len(expected_forms)))

    def test_glottalK(self):
        stem = "n$aasik'+N"
        expected_map = [
            ('-1SG.II',    ["naasik'i'y"]),
            ('-1PL.II',    ["naasik'i'm"]),
            ('-2SG.II',    ["naasik'in"]),
            ('-2PL.II',    ["naasik'si'm"]),
            ('-3.II',      ["naasik't"]),
            ('-3PL.II',    ["naasik'diit"]),
            ('[-3.II]=CN',   ["naasik'hl"]),
            ('[-3.II]=PN',   ["naasik's"]),
            ('-SX',     ["naasik'it"]),
            ('-ATTR',   ["naasik'im", "naasik'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_glottKW(self):
        stem = "t'$ikw'+N"
        expected_map = [
            ('-1SG.II',    ["t'ikw'i'y"]),
            ('-1PL.II',    ["t'ikw'i'm", "t'ik'u'm"]),
            ('-2SG.II',    ["t'ikw'in"]),
            ('-2PL.II',    ["t'ikw'si'm"]),
            ('-3.II',      ["t'ikw't"]),
            ('-3PL.II',    ["t'ikw'diit"]),
            ('[-3.II]=CN',   ["t'ikw'hl"]),
            ('[-3.II]=PN',   ["t'ikw's"]),
            ('-SX',     ["t'ikw'it"]),
            ('-ATTR',   ["t'ikw'im", "t'ik'um", "t'ikw'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_glottK_(self):
        stem = "han$ak_'+N"
        expected_map = [
            ('-1SG.II',    ["hanak̲'a'y"]),
            ('-1PL.II',    ["hanak̲'a'm"]),
            ('-2SG.II',    ["hanak̲'an"]),
            ('-2PL.II',    ["hanak̲'si'm"]),
            ('-3.II',      ["hanak̲'t"]),
            ('-3PL.II',    ["hanak̲'diit"]),
            ('[-3.II]=CN',   ["hanak̲'hl"]),
            ('[-3.II]=PN',   ["hanak̲'s"]),
            ('-SX',     ["hanak̲'at"]),
            ('-ATTR',   ["hanak̲'am", "hanak̲'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_glottOK_(self):
        stem = "ts'$ok_'+N"
        expected_map = [
            ('-1SG.II',    ["ts'ok̲'a'y", "ts'ok̲'o'y"]),
            ('-1PL.II',    ["ts'ok̲'a'm", "ts'ok̲'o'm"]),
            ('-2SG.II',    ["ts'ok̲'on", "ts'ok̲'an"]),
            ('-2PL.II',    ["ts'ok̲'si'm"]),
            ('-3.II',      ["ts'ok̲'t"]),
            ('-3PL.II',    ["ts'ok̲'diit"]),
            ('[-3.II]=CN',   ["ts'ok̲'hl"]),
            ('[-3.II]=PN',   ["ts'ok̲'s"]),
            ('-SX',     ["ts'ok̲'at", "ts'ok̲'ot"]),
            ('-ATTR',   ["ts'ok̲'am", "ts'ok̲'om", "ts'ok̲'a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

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
        super().setUpClass(BASIC_E, test_stems)

    def test_fricS(self):
        stem = "m$aas+N"
        expected_map = [
            ('-1SG.II',    ["maasi'y"]),
            ('-1PL.II',    ["maasi'm"]),
            ('-2SG.II',    ["maasin"]),
            ('-2PL.II',    ["maasisi'm"]),
            ('-3.II',      ["maast"]),
            ('-3PL.II',    ["maasdiit"]),
            ('[-3.II]=CN',   ["maashl"]),
            ('[-3.II]=PN',   ["maas"]),
            ('-SX',     ["maasit"]),
            ('-ATTR',   ["maasim", "maasa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_fricHL(self):
        stem = "k'$uuhl+N"
        expected_map = [
            ('-1SG.II',    ["k'uuhli'y"]),
            ('-1PL.II',    ["k'uuhli'm"]),
            ('-2SG.II',    ["k'uuhlin"]),
            ('-2PL.II',    ["k'uuhlsi'm"]),
            ('-3.II',      ["k'uuhlt"]),
            ('-3PL.II',    ["k'uuhldiit"]),
            ('[-3.II]=CN',   ["k'uuhl"]),
            ('[-3.II]=PN',   ["k'uuhls"]),
            ('-SX',     ["k'uuhlit"]),
            ('-ATTR',   ["k'uuhlim", "k'uuhla"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_fricX(self):
        stem = "l$ax+N"  # not sure if these should also be optionally glided
        expected_map = [
            ('-1SG.II',    ["layi'y"]),
            ('-1PL.II',    ["layi'm"]),
            ('-2SG.II',    ["layin"]),
            ('-2PL.II',    ["laxsi'm"]),
            ('-3.II',      ["laxt"]),
            ('-3PL.II',    ["laxdiit"]),
            ('[-3.II]=CN',   ["laxhl"]),
            ('[-3.II]=PN',   ["laxs"]),
            ('-SX',     ["layit"]),
            ('-ATTR',   ["layim", "laya"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_fricXW(self):
        stem = "l$aaxw+N"
        expected_map = [
            ('-1SG.II',    ["laawi'y", "laaxwi'y"]),
            ('-1PL.II',    ["laawi'm", "laawu'm", "laaxwi'm", "laaxu'm"]),
            ('-2SG.II',    ["laawin", "laaxwin"]),
            ('-2PL.II',    ["laaxwsi'm"]),
            ('-3.II',      ["laaxwt"]),
            ('-3PL.II',    ["laaxwdiit"]),
            ('[-3.II]=CN',   ["laaxwhl"]),
            ('[-3.II]=PN',   ["laaxws"]),
            ('-SX',     ["laawit", "laaxwit"]),
            ('-ATTR',   ["laawim", "laawum", "laawa", "laaxwim", "laaxum", "laaxwa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_fricX_(self):
        stem = "'n$ax_+N"
        expected_map = [
            ('-1SG.II',    ["'naha'y", "'nax̲a'y"]),
            ('-1PL.II',    ["'naha'm", "'nax̲a'm"]),
            ('-2SG.II',    ["'nahan", "'nax̲an"]),
            ('-2PL.II',    ["'nax̲si'm"]),
            ('-3.II',      ["'nax̲t"]),
            ('-3PL.II',    ["'nax̲diit"]),
            ('[-3.II]=CN',   ["'nax̲hl"]),
            ('[-3.II]=PN',   ["'nax̲s"]),
            ('-SX',     ["'nahat", "'nax̲at"]),
            ('-ATTR',   ["'naham", "'naha", "'nax̲am", "'nax̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_fricOX_(self):
        stem = "n$ox_+N"
        expected_map = [
            ('-1SG.II',    ["noha'y", "noho'y", "nox̲a'y", "nox̲o'y"]),
            ('-1PL.II',    ["noha'm", "noho'm", "nox̲a'm", "nox̲o'm"]),
            ('-2SG.II',    ["nohan", "nohon", "nox̲an", "nox̲on"]),
            ('-2PL.II',    ["nox̲si'm"]),
            ('-3.II',      ["nox̲t"]),
            ('-3PL.II',    ["nox̲diit"]),
            ('[-3.II]=CN',   ["nox̲hl"]),
            ('[-3.II]=PN',   ["nox̲s"]),
            ('-SX',     ["nohat", "nohot", "nox̲at", "nox̲ot"]),
            ('-ATTR',   ["noham", "nohom", "noha", "nox̲am", "nox̲om", "nox̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

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
        super().setUpClass(BASIC_E, test_stems)

    def test_plainM(self):
        stem = 'g$um+N'
        expected_map = [
            ('-1SG.II',    ["gumi'y"]),
            ('-1PL.II',    ["gumi'm", "gumu'm"]),
            ('-2SG.II',    ["gumin"]),
            ('-2PL.II',    ["gumsi'm"]),
            ('-3.II',      ["gumt"]),
            ('-3PL.II',    ["gumdiit"]),
            ('[-3.II]=CN',   ["gumhl"]),
            ('[-3.II]=PN',   ["gums"]),
            ('-SX',     ["gumit", "gumt"]),
            ('-ATTR',   ["gumim", "gumum", "guma"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_plainN(self):
        stem = 'b$an+N'
        expected_map = [
            ('-1SG.II',    ["bani'y"]),
            ('-1PL.II',    ["bani'm"]),
            ('-2SG.II',    ["banin"]),
            ('-2PL.II',    ["bansi'm"]),
            ('-3.II',      ["bant"]),
            ('-3PL.II',    ["bandiit"]),
            ('[-3.II]=CN',   ["banhl"]),
            ('[-3.II]=PN',   ["bans"]),
            ('-SX',     ["banit", "bant"]),
            ('-ATTR',   ["banim", "bana"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_plainL(self):
        stem = "haw$il+N"
        expected_map = [
            ('-1SG.II',    ["hawili'y"]),
            ('-1PL.II',    ["hawili'm"]),
            ('-2SG.II',    ["hawilin"]),
            ('-2PL.II',    ["hawilsi'm"]),
            ('-3.II',      ["hawilt"]),
            ('-3PL.II',    ["hawildiit"]),
            ('[-3.II]=CN',   ["hawilhl"]),
            ('[-3.II]=PN',   ["hawils"]),
            ('-SX',     ["hawilit", "hawilt"]), # hawilt? hawilit?
            ('-ATTR',   ["hawilim", "hawila"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_plainW(self):
        stem = "g_awk_'$aw+N"
        expected_map = [
            ('-1SG.II',    ["g̲awk̲'awi'y"]),
            ('-1PL.II',    ["g̲awk̲'awi'm", "g̲awk̲'awu'm"]),
            ('-2SG.II',    ["g̲awk̲'awin"]),
            ('-2PL.II',    ["g̲awk̲'awsi'm"]),
            ('-3.II',      ["g̲awk̲'awt"]),
            ('-3PL.II',    ["g̲awk̲'awdiit"]),
            ('[-3.II]=CN',   ["g̲awk̲'awhl"]),
            ('[-3.II]=PN',   ["g̲awk̲'aws"]),
            ('-SX',     ["g̲awk̲'awit", "g̲awk̲'awt"]),
            ('-ATTR',   ["g̲awk̲'awim", "g̲awk̲'awum", "g̲awk̲'awa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

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
        super().setUpClass(BASIC_E, test_stems)

    def test_glottalM(self):
        stem = "hl$aa'm+N"
        expected_map = [
            ('-1SG.II',    ["hlaa'mi'y"]),
            # ('-1PL.II',    ["hlaa'mi'm", "hlaa'mm"]), # ??
            ('-2SG.II',    ["hlaa'min"]),
            ('-2PL.II',    ["hlaa'msi'm"]),
            ('-3.II',      ["hlaa'mt"]),
            ('-3PL.II',    ["hlaa'mdiit"]),
            ('[-3.II]=CN',   ["hlaa'mhl"]),
            ('[-3.II]=PN',   ["hlaa'ms"]),
            ('-SX',     ["hlaa'mit"]), # ??
            ('-ATTR',   ["hlaa'mim", "hlaa'ma"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

#     def test_glottalN(self):
#         stem = "b$an+N"
#         expected_map = [
#             ('-1SG.II',    ["bani'y"]),
#             ('-1PL.II',    ["bani'm"]),
#             ('-2SG.II',    ["banin"]),
#             ('-2PL.II',    ["bansi'm"]),
#             ('-3.II',      ["bant"]),
#             ('-3PL.II',    ["bandiit"]),
#             ('[-3.II]=CN',   ["banhl"]),
#             ('[-3.II]=PN',   ["bans"]),
#             ('-SX',     ["bant"]),
#             ('-ATTR',   ["banim", "bana"]),
#         ]
#         for gloss, expected_forms in expected_map:
#             result_list = self.fst.generate(stem+gloss)
#             for form in expected_forms:
#                 with self.subTest(form=stem+gloss):
#                     self.assertIn(form, result_list)
#             self.assertEqual(len(result_list), len(expected_forms),
#                 "{} should have {} results".format(stem+gloss,
                                            # len(expected_forms)))

    def test_glottalL(self):
        stem = "lig$i'l+N"
        expected_map = [
            ('-1SG.II',    ["ligi'li'y"]),
            ('-1PL.II',    ["ligi'li'm"]),
            ('-2SG.II',    ["ligi'lin"]),
            ('-2PL.II',    ["ligi'lsi'm"]),
            ('-3.II',      ["ligi'lt"]),
            ('-3PL.II',    ["ligi'ldiit"]),
            ('[-3.II]=CN',   ["ligi'lhl"]),
            ('[-3.II]=PN',   ["ligi'ls"]),
            ('-SX',     ["ligi'lit"]),
            ('-ATTR',   ["ligi'lim", "ligi'la"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_glottalY(self):
        stem = "mask_'ay$aa'y+N"
        expected_map = [
            ('-1SG.II',    ["mask̲'ayaa'y"]), # ??
            ('-1PL.II',    ["mask̲'ayaa'yi'm"]),
            ('-2SG.II',    ["mask̲'ayaa'yin"]),
            ('-2PL.II',    ["mask̲'ayaa'ysi'm"]),
            ('-3.II',      ["mask̲'ayaa'yt"]),
            ('-3PL.II',    ["mask̲'ayaa'ydiit"]),
            ('[-3.II]=CN',   ["mask̲'ayaa'yhl"]),
            ('[-3.II]=PN',   ["mask̲'ayaa'ys"]),
            ('-SX',     ["mask̲'ayaa'yit"]),
            ('-ATTR',   ["mask̲'ayaa'yim", "mask̲'ayaa'ya"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_glottalW(self):
        stem = "x_b$aa'w+N"
        expected_map = [
            ('-1SG.II',    ["x̲baa'wi'y"]),
            ('-1PL.II',    ["x̲baa'wi'm", "x̲baa'u'm"]),
            ('-2SG.II',    ["x̲baa'win"]),
            ('-2PL.II',    ["x̲baa'wsi'm"]),
            ('-3.II',      ["x̲baa'wt"]),
            ('-3PL.II',    ["x̲baa'wdiit"]),
            ('[-3.II]=CN',   ["x̲baa'whl"]),
            ('[-3.II]=PN',   ["x̲baa'ws"]),
            # ('-SX',     ["x̲baa'wit", "x̲baa'ut"]),  
                # haven't applied this yet, keep in mind
            ('-ATTR',   ["x̲baa'wim", "x̲baa'um", "x̲baa'wa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_glottalStop(self):
        stem = "n$oo'o+N"
        expected_map = [
            ('-1SG.II',    ["noo'o'y"]),
            ('-1PL.II',    ["noo'o'm"]),
            ('-2SG.II',    ["noo'on"]),
            ('-2PL.II',    ["noo'osi'm"]),
            ('-3.II',      ["noo'ot"]),
            ('-3PL.II',    ["noo'odiit"]),
            ('[-3.II]=CN',   ["noo'ohl"]),
            ('[-3.II]=PN',   ["noo'os"]),
            ('-SX',     ["noo'ot"]),
            ('-ATTR',   ["noo'om", "noo'a"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

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
        super().setUpClass(BASIC_E, test_stems)

    def test_shortA(self):
        stem = "w$a+N"
        expected_map = [
            ('-1SG.II',    ["wa'y"]),
            ('-1PL.II',    ["wa'm"]),
            ('-2SG.II',    ["wan"]),
            ('-2PL.II',    ["wasi'm"]),
            ('-3.II',      ["wat"]),
            ('-3PL.II',    ["wadiit"]),
            ('[-3.II]=CN',   ["wahl"]),
            ('[-3.II]=PN',   ["was"]),
            ('-SX',     ["wat"]),
            ('-ATTR',   ["wam", "waha"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_shortAlonger(self):
        stem = "ha'niig$ilbilsa+N"
        expected_map = [
            ('-1SG.II',    ["ha'niigilbilsa'y"]),
            ('-1PL.II',    ["ha'niigilbilsa'm"]),
            ('-2SG.II',    ["ha'niigilbilsan"]),
            ('-2PL.II',    ["ha'niigilbilsasi'm"]),
            ('-3.II',      ["ha'niigilbilsat"]),
            ('-3PL.II',    ["ha'niigilbilsadiit"]),
            ('[-3.II]=CN',   ["ha'niigilbilsahl"]),
            ('[-3.II]=PN',   ["ha'niigilbilsas"]),
            ('-SX',     ["ha'niigilbilsat"]),
            ('-ATTR',   ["ha'niigilbilsam", "ha'niigilbilsaha"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_longU(self):
        stem = "gy$uu+N"
        expected_map = [
            ('-1SG.II',    ["gyuu'y"]),
            ('-1PL.II',    ["gyuu'm"]),
            ('-2SG.II',    ["gyuun"]),
            ('-2PL.II',    ["gyuusi'm"]),
            ('-3.II',      ["gyuut"]),
            ('-3PL.II',    ["gyuudiit"]),
            ('[-3.II]=CN',   ["gyuuhl"]),
            ('[-3.II]=PN',   ["gyuus"]),
            ('-SX',     ["gyuut"]),
            ('-ATTR',   ["gyuum", "gyuuha"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_longE(self):
        stem = "y$ee+VI"
        expected_map = [
            ('-1SG.II',    ["yee'y"]),
            ('-1PL.II',    ["yee'm"]),
            # ('-2SG.II',    ["yeen", "yin"]), # requires maximal parser :\
            ('-2PL.II',    ["yeesi'm"]),
            ('-3.II',      ["yeet"]),
            ('[-3.II]=CN',   ["yeehl"]),
            ('[-3.II]=PN',   ["yees"]),
            ('-SX',     ["yeet"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_longElonger(self):
        stem = "majag_al$ee+N"
        expected_map = [
            ('-1SG.II',    ["majag̲alee'y"]),
            ('-1PL.II',    ["majag̲alee'm"]),
            ('-2SG.II',    ["majag̲aleen"]),
            ('-2PL.II',    ["majag̲aleesi'm"]),
            ('-3.II',      ["majag̲aleet"]),
            ('-3PL.II',    ["majag̲aleediit"]),
            ('[-3.II]=CN',   ["majag̲aleehl"]),
            ('[-3.II]=PN',   ["majag̲alees"]),
            ('-SX',     ["majag̲aleet"]),
            ('-ATTR',   ["majag̲aleem", "majag̲aleeha"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_longI(self):
        stem = "k_'$esii+N"
        expected_map = [
            ('-1SG.II',    ["k̲'esii'y"]),
            ('-1PL.II',    ["k̲'esii'm"]),
            ('-2SG.II',    ["k̲'esiin"]),
            ('-2PL.II',    ["k̲'esiisi'm"]),
            ('-3.II',      ["k̲'esiit"]),
            ('-3PL.II',    ["k̲'esiidiit"]),
            ('[-3.II]=CN',   ["k̲'esiihl"]),
            ('[-3.II]=PN',   ["k̲'esiis"]),
            ('-SX',     ["k̲'esiit"]),
            ('-ATTR',   ["k̲'esiim", "k̲'esiiha"]), # ??
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

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
        super().setUpClass(BASIC_E, test_stems)

    def test_ST(self):
        stem = "x_b$iist+N"
        expected_map = [
            ('-1SG.II',    ["x̲biisdi'y"]),
            ('-1PL.II',    ["x̲biisdi'm"]),
            ('-2SG.II',    ["x̲biisdin"]),
            ('-2PL.II',    ["x̲biistsi'm"]),
            ('-3.II',      ["x̲biistt"]),
            ('-3PL.II',    ["x̲biistdiit"]),
            ('[-3.II]=CN',   ["x̲biisthl"]),
            ('[-3.II]=PN',   ["x̲biists"]),
            ('-SX',     ["x̲biisdit"]),
            ('-ATTR',   ["x̲biisdim", "x̲biisda"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_YT(self):
        stem = "hal$ayt+N"
        expected_map = [
            ('-1SG.II',    ["halaydi'y"]),
            ('-1PL.II',    ["halaydi'm"]),
            ('-2SG.II',    ["halaydin"]),
            ('-2PL.II',    ["halaytsi'm"]),
            ('-3.II',      ["halaytt"]),
            ('-3PL.II',    ["halaytdiit"]),
            ('[-3.II]=CN',   ["halaythl"]),
            ('[-3.II]=PN',   ["halayts"]),
            ('-SX',     ["halaydit"]),
            ('-ATTR',   ["halaydim", "halayda"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_LP(self):
        stem = "w$ilp+N"
        expected_map = [
            ('-1SG.II',    ["wilbi'y"]),
            ('-1PL.II',    ["wilbi'm"]),
            ('-2SG.II',    ["wilbin"]),
            ('-2PL.II',    ["wilpsi'm"]),
            ('-3.II',      ["wilpt"]),
            ('-3PL.II',    ["wilpdiit"]),
            ('[-3.II]=CN',   ["wilphl"]),
            ('[-3.II]=PN',   ["wilps"]),
            ('-SX',     ["wilbit"]),
            ('-ATTR',   ["wilbim", "wilba"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_LKW(self):
        stem = "s$ilkw+N"
        expected_map = [
            ('-1SG.II',    ["silgwi'y"]),
            ('-1PL.II',    ["silgwi'm", "silgu'm"]),
            ('-2SG.II',    ["silgwin"]),
            ('-2PL.II',    ["silkwsi'm"]),
            ('-3.II',      ["silkwt"]),
            ('-3PL.II',    ["silkwdiit"]),
            ('[-3.II]=CN',   ["silkwhl"]),
            ('[-3.II]=PN',   ["silkws"]),
            ('-SX',     ["silgwit"]),
            ('-ATTR',   ["silgwim", "silgum", "silgwa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_TX(self):
        stem = "ts'$amtx+N"
        expected_map = [
            ('-1SG.II',    ["ts'amtxi'y"]),
            ('-1PL.II',    ["ts'amtxi'm"]),
            ('-2SG.II',    ["ts'amtxin"]),
            ('-2PL.II',    ["ts'amtxsi'm"]),
            ('-3.II',      ["ts'amtxt"]),
            ('-3PL.II',    ["ts'amtxdiit"]),
            ('[-3.II]=CN',   ["ts'amtxhl"]),
            ('[-3.II]=PN',   ["ts'amtxs"]),
            ('-SX',     ["ts'amtxit"]),
            ('-ATTR',   ["ts'amtxim", "ts'amtxa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_SXW(self):
        stem = "biy$oosxw+N"
        expected_map = [
            ('-1SG.II',    ["biyoosxwi'y"]),
            ('-1PL.II',    ["biyoosxwi'm", "biyoosxu'm"]),
            ('-2SG.II',    ["biyoosxwin"]),
            ('-2PL.II',    ["biyoosxwsi'm"]),
            ('-3.II',      ["biyoosxwt"]),
            ('-3PL.II',    ["biyoosxwdiit"]),
            ('[-3.II]=CN',   ["biyoosxwhl"]),
            ('[-3.II]=PN',   ["biyoosxws"]),
            ('-SX',     ["biyoosxwit"]),
            ('-ATTR',   ["biyoosxwim", "biyoosxum", "biyoosxwa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_X_XW(self):
        stem = "'$ax_xw+N"
        expected_map = [
            ('-1SG.II',    ["ax̲xwi'y"]),
            ('-1PL.II',    ["ax̲xwi'm", "ax̲xu'm"]),
            ('-2SG.II',    ["ax̲xwin"]),
            ('-2PL.II',    ["ax̲xwsi'm"]),
            ('-3.II',      ["ax̲xwt"]),
            ('-3PL.II',    ["ax̲xwdiit"]),
            ('[-3.II]=CN',   ["ax̲xwhl"]),
            ('[-3.II]=PN',   ["ax̲xws"]),
            ('-SX',     ["ax̲xwit"]),
            ('-ATTR',   ["ax̲xwim", "ax̲xum", "ax̲xwa"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_PX_(self):
        stem = "h$upx_+N"
        expected_map = [
            ('-1SG.II',    ["hupx̲a'y"]),
            ('-1PL.II',    ["hupx̲a'm"]),
            ('-2SG.II',    ["hupx̲an"]),
            ('-2PL.II',    ["hupx̲si'm"]),
            ('-3.II',      ["hupx̲t"]),
            ('-3PL.II',    ["hupx̲diit"]),
            ('[-3.II]=CN',   ["hupx̲hl"]),
            ('[-3.II]=PN',   ["hupx̲s"]),
            ('-SX',     ["hupx̲at"]),
            ('-ATTR',   ["hupx̲am", "hupx̲a"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

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
        super().setUpClass(BASIC_E, test_stems)

    def test_indepObstruent(self):
        stem = "g$up+VT"
        expected_map = [
            ('-TR-2SG.II',    ["gubin"]),
            ('-TR-2PL.II',    ["gubisi'm"]),
            ('-TR-3.II',      ["gubit"]),
            ('-TR-3PL.II',    ["gupdiit"]),
            ('-3.II',      ["gupt"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_indepSibilant(self):
        stem = "t'$is+VT"
        expected_map = [
            ('-TR-2SG.II',    ["t'isin"]),
            ('-TR-2PL.II',    ["t'isisi'm"]),
            ('-TR-3.II',      ["t'isit"]),
            ('-TR-3PL.II',    ["t'isdiit"]),
            ('-3.II',      ["t'ist"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_indepPlainSonorant(self):
        stem = "g$in+VT"
        expected_map = [
            ('-TR-2SG.II',    ["ginin"]),
            ('-TR-2PL.II',    ["ginisi'm"]),
            ('-TR-3.II',      ["ginit"]),
            ('-TR-3PL.II',    ["gindiit"]),
            ('-3.II',      ["gint"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_indepGlotSonorant(self):
        stem = "g_$e'n+VT"
        expected_map = [
            ('-TR-2SG.II',    ["g̲e'nin"]),
            ('-TR-2PL.II',    ["g̲e'nisi'm"]),
            ('-TR-3.II',      ["g̲e'nit"]),
            ('-TR-3PL.II',    ["g̲e'ndiit"]),
            ('-3.II',      ["g̲e'nt"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_indepGlotStop(self):
        stem = "g$a'a+VT"
        expected_map = [
            ('-TR-2SG.II',    ["ga'an"]),
            ('-TR-2PL.II',    ["ga'asi'm"]),
            ('-TR-3.II',      ["ga'at"]),
            ('-TR-3PL.II',    ["ga'adiit"]),
            ('-3.II',      ["ga'at"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                             "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_indepUnstressedSonorant(self):
        stem = "hl$andin+VT"
        expected_map = [
            ('-TR-2SG.II',    ["hlandinin"]),
            ('-TR-2PL.II',    ["hlandinsi'm"]),
            ('-TR-3.II',      ["hlandint"]),
            ('-TR-3PL.II',    ["hlandindiit"]),
            ('-3.II',      ["hlandint"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list, "expected for "+gloss)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_indepVowel(self):
        stem = "'w$a+VT"
        expected_map = [
            ('-TR-2SG.II',    ["'wayin"]),
            ('-TR-2PL.II',    ["'wayisi'm"]),
            ('-TR-3.II',      ["'wayit"]),
            ('-TR-3PL.II',    ["'wadiit"]),
            ('-3.II',      ["'wat"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

class TestBigT(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'TransitiveVerb': [
                "m$ahl(t)",
                "b$ats(t)",
                "h$ats'(t)",
                "siw$a(t)",
                "g$uu(t)",
                "w$an",
                # get a glottal son + T in here
                # do tests for non-lexical big T as affix?
            ],
            'Noun': ['w$a']
        }
        super().setUpClass(BASIC_E, test_stems)

    def test_native_postC(self):
        stem = "m$ahlT+VT"
        expected_map = [
            ('-TR-2SG.II',   ["mahldin"]),
            ('-TR-3.II',     ["mahldit"]),
            ('-TR-3PL.II',   ["mahldiit"]),
            ('-2SG.II',      ["mahlin"]),
            ('-3.II',        ["mahlit"]),
            ('-3PL.II',      ["mahldiit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))
    
    def test_native_no_extraT(self):
        stem = "m$ahlT+VT"
        unexpected_map = [
            '-T-3.II',
            '-T-TR-3.II',
        ]
        for gloss in unexpected_map:
            with self.subTest(form=stem+gloss):
                result_list = self.fst.generate(stem+gloss)
                self.assertEqual(len(result_list), 0,
                "{} should not be a possible path".format(stem+gloss))

    def test_native_postvoiceable(self):
        stem = "b$atsT+VT"
        expected_map = [
            ('-TR-2SG.II',   ["batsdin"]),
            ('-TR-3.II',     ["batsdit"]),
            ('-TR-3PL.II',   ["batsdiit"]),
            ('-2SG.II',      ["bajin"]),
            ('-3.II',        ["bajit"]),
            ('-3PL.II',      ["batsdiit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_native_postglottal(self):
        stem = "h$ats'T+VT"
        expected_map = [
            ('-TR-2SG.II',   ["hats'din"]),
            ('-TR-3.II',     ["hats'dit"]),
            ('-TR-3PL.II',   ["hats'diit"]),
            ('-2SG.II',      ["hats'in"]),
            ('-3.II',        ["hats'it"]),
            ('-3PL.II',      ["hats'diit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_native_postV(self):
        stem = "siw$aT+VT"
        expected_map = [
            ('-TR-2SG.II',   ["siwatdin"]),
            ('-TR-3.II',     ["siwatdit"]),
            ('-TR-3PL.II',   ["siwatdiit"]),
            ('-2SG.II',      ["siwadin"]),
            ('-3.II',        ["siwadit"]),
            ('-3PL.II',      ["siwatdiit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_postR_constructed(self):
        stem = "w$an+VT"
        expected_map = [
            ('-T-TR-2SG.II',   ["wandin"]),
            ('-T-TR-3.II',     ["wandit"]),
            ('-T-TR-3PL.II',   ["wandiit"]),
            ('-T-2SG.II',      ["wandin"]),
            ('-T-3.II',        ["wandit"]),
            ('-T-3PL.II',      ["wandiit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                             "{} should have {} results".format(stem+gloss,
                                                        len(expected_forms)))

    def test_postV_constructed(self):
        stem = "w$a+N"
        expected_map = [
            ('-T-3.II',        ["wadit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                             "{} should have {} results".format(stem+gloss,
                                                        len(expected_forms)))


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
        super().setUpClass(BASIC_E, test_stems)

    def test_gipaykw_voicing(self):
        stem = "gip$aykw+VI"
        expected_map = [
            ('',   ["gipaykw"]),
            ('-3.II',   ["gipaykwt"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_hardeningX_(self):
        stem = "'$algax_+VI"
        expected_map = [
            ('-1SG.II',    ["algag̲a'y", "algax̲a'y"]),
            ('-2PL.II',    ["algax̲si'm"]),
            ('-3.II',      ["algax̲t"]),
            ('-SX',     ["algag̲at", "algax̲at"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))

    def test_vocalizedX(self):
        stem = "l$imx+VI"
        expected_map = [
            ('-1SG.II',    ["limi'y"]),
            ('-2PL.II',    ["limxsi'm"]),
            ('-3.II',      ["limxt"]),
            ('-SX',     ["limit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                "{} should have {} results".format(stem+gloss,
                                            len(expected_forms)))


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
        super().setUpClass(BASIC_E, test_stems)

    def test_caus_sII(self):
        stem = "s$ip+VI-CAUS"
        expected_map = [
            ('-1SG.II',    ["sibini'y"]),
            ('-1PL.II',    ["sibini'm"]),
            ('-2SG.II',    ["sibinin"]),
            ('-2PL.II',    ["sibinsi'm"]),
            ('-3.II',      ["sibint"]),
            ('-3PL.II',      ["sibindiit"]),
            ('-TR-1SG.II',    ["sibini'y"]),
            ('-TR-1PL.II',    ["sibini'm"]),
            ('-TR-2SG.II',    ["sibinin"]),
            ('-TR-2PL.II',    ["sibinsi'm"]),
            ('-TR-3.II',      ["sibint"]),
            ('-TR-3PL.II',      ["sibindiit"]),
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(stem+gloss)
            for form in expected_forms:
                with self.subTest(form=stem+gloss):
                    self.assertIn(form, result_list)
            self.assertEqual(len(result_list), len(expected_forms),
                             "{} should have {} results".format(stem+gloss,
                                                        len(expected_forms)))

    def test_caus_stem_types(self):
        expected_map = [
            ('y$ook_+VI-CAUS-3.II',    ["yoog̲ant"]),
            ('y$ee+VI-CAUS-3.II',      ["yeedint"]),
            ("s$iip'+VI-CAUS-3.II",    ["siip'int"]),
            ("w$an+VI-CAUS-3.II",      ["wandint"]),
            ("t$e'l+VI-CAUS-3.II",     ["te'ldint"]),  # t'e'lint?
            ("gwil$a+VI-CAUS-3.II",     ["gwiladint"]),  #
        ]
        for gloss, expected_forms in expected_map:
            result_list = self.fst.generate(gloss)
            for form in expected_forms:
                with self.subTest(gloss=gloss):
                    self.assertIn(form, result_list)
            with self.subTest(gloss=gloss):
                self.assertEqual(len(result_list), len(expected_forms),
                                "{} should have {} results".format(result_list, 
                                                        len(expected_forms)))


if __name__ == '__main__':
    unittest.main()

# python -m unittest test
# python -m unittest discover # all test files in current dir
# python -m unittest discover -s tests # all test files in /tests
