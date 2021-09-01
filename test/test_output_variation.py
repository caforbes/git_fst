import unittest
from test import TestFSTOutput, BASIC_EW

"""
This suite checks the correct application of E-W dialectal rules on
actual gitksan words.
These tests use a version of the FST (v1 with dialect rules) as a dependency.
"""

class TestGwiGu(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "'agw$i",
                "'$aagwi",
                "kw'$ihl",
                "gw$iila",
            ]
        }
        super().setUpClass(BASIC_EW, test_stems)

    def test_agwi_agu(self):
        self.assertEqual(len(self.fst.analyze("agwi")), 1)
        self.assertEqual(len(self.fst.analyze("agu")), 1)
        self.assertNotEqual(len(self.fst.analyze("agwihl")), 0)
        self.assertNotEqual(len(self.fst.analyze("aguhl")), 0)

    def test_aagwi_no_change(self):
        self.assertNotEqual(len(self.fst.analyze("aagwi")), 0)
        self.assertEqual(len(self.fst.analyze("aagu")), 0)

    def test_kwihl_kuhl(self):
        self.assertNotEqual(len(self.fst.analyze("kw'ihl")), 0)
        self.assertNotEqual(len(self.fst.analyze("k'uhl")), 0)

    def test_kuhl_tag(self):
        self.assertIn("kw'$ihl+N", self.fst.analyze("k'uhl"))  # <GWIGU>

    def test_gwii_no_change(self):
        self.assertNotEqual(len(self.fst.analyze("gwiila")), 0)
        self.assertEqual(len(self.fst.analyze("guila")), 0)
        self.assertEqual(len(self.fst.analyze("guula")), 0)

class TestAE(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "w$a",
                "l$an",
                "ts'$ap",
                "g_$an",
                "'$aks",
                "and$aba'a",
            ],
            'Prenoun': [
                "l$ax_",
            ]
        }
        super().setUpClass(BASIC_EW, test_stems)

    def test_wa_we(self):
        self.assertNotEqual(len(self.fst.analyze("wa")), 0)
        self.assertNotEqual(len(self.fst.analyze("we")), 0)

    def test_we_tag(self):
        self.assertIn("w$a+N", self.fst.analyze("we"))  # <AE>

    def test_lan_len(self):
        self.assertNotEqual(len(self.fst.analyze("lan")), 0)
        self.assertNotEqual(len(self.fst.analyze("len")), 0)

    def test_tsap_tsep(self):
        self.assertNotEqual(len(self.fst.analyze("ts'ap")), 0)
        self.assertNotEqual(len(self.fst.analyze("ts'ep")), 0)

    def test_aks_no_change(self):
        self.assertNotEqual(len(self.fst.analyze("aks")), 0)
        self.assertEqual(len(self.fst.analyze("eks")), 0)

    def test_lax_no_change(self):
        self.assertNotEqual(len(self.fst.analyze("lax̲")), 0)
        self.assertEqual(len(self.fst.analyze("lex̲")), 0)

    def test_gan_no_change(self):
        self.assertNotEqual(len(self.fst.analyze("g̲an")), 0)
        self.assertEqual(len(self.fst.analyze("g̲en")), 0)


class TestEI(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'IntransitiveVerb': [
                "h$etxw",
                "h$edin",
                "h$e",
            ],
        }
        super().setUpClass(BASIC_EW, test_stems)

    def test_hetxw_hitxw(self):
        self.assertNotEqual(len(self.fst.analyze("hetxw")), 0)
        self.assertNotEqual(len(self.fst.analyze("hitxw")), 0)

    def test_hitxw_tag(self):
        self.assertIn("h$etxw+VI", self.fst.analyze("hitxw"))  # <HEHI>

    def test_hedin_hidin(self):
        self.assertNotEqual(len(self.fst.analyze("hedin")), 0)
        self.assertNotEqual(len(self.fst.analyze("hidin")), 0)

    def test_he_no_change(self):
        self.assertNotEqual(len(self.fst.analyze("he")), 0)
        self.assertEqual(len(self.fst.analyze("hi")), 0)
        self.assertNotEqual(len(self.fst.analyze("hehl")), 0)
        self.assertEqual(len(self.fst.analyze("hihl")), 0)

class TestXsFortition(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "xs$an",
                "'amxsiw$aa",
            ],
            'Preverb': [
                "g_$alxsi",
                "g$uxws",
            ],
            'IntransitiveVerb': [
                "xwsd$ins",
                "h$ooxs",
                "l$iluxws",
                "g$itxs",
            ]
        }
        super().setUpClass(BASIC_EW, test_stems)


    def test_xsan_ksan(self):
        self.assertNotEqual(len(self.fst.analyze("xsan")), 0)
        self.assertNotEqual(len(self.fst.analyze("ksan")), 0)

    def test_ksan_ksen_tag(self):
        self.assertIn("xs$an+N", self.fst.analyze("ksan"))  # <XSKS>
    
    def test_multiple_application(self):
        self.assertNotEqual(len(self.fst.analyze("ksen")), 0)
        self.assertIn("xs$an+N", self.fst.analyze("ksen"))  # <XSKS><AE>

    def test_galxsi_galksi(self):
        self.assertNotEqual(len(self.fst.analyze("g̲alxsi")), 0)
        self.assertNotEqual(len(self.fst.analyze("g̲alksi")), 0)

    def test_galksi_tag(self):
        self.assertIn("g_$alxsi+PVB", self.fst.analyze("g̲alksi"))  # <XSKS>

    def test_hooxs_hooks(self):
        self.assertNotEqual(len(self.fst.analyze("hooxs")), 0)
        self.assertNotEqual(len(self.fst.analyze("hooks")), 0)

    def test_amxsiwaa_amksiwaa(self):
        self.assertNotEqual(len(self.fst.analyze("amxsiwaa")), 0)
        self.assertNotEqual(len(self.fst.analyze("amksiwaa")), 0)

    def test_xwsdins_kwsdins(self):
        self.assertNotEqual(len(self.fst.analyze("xwsdins")), 0)
        self.assertNotEqual(len(self.fst.analyze("kwsdins")), 0)

    @unittest.skip('would like it to work, but not needed based on dict')
    def test_guxws_gukws(self):
        self.assertNotEqual(len(self.fst.analyze("guxws")), 0)
        self.assertNotEqual(len(self.fst.analyze("gukws")), 0)

    def test_liluxws_no_change(self):
        self.assertNotEqual(len(self.fst.analyze("liluxws")), 0)
        self.assertEqual(len(self.fst.analyze("lilukws")), 0)

    def test_gitxs_no_change(self):
        self.assertNotEqual(len(self.fst.analyze("gitxs")), 0)
        self.assertEqual(len(self.fst.analyze("gitks")), 0)

class TestKsLenition(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                # "xs$an",
                "'$aks",
                "'amksiw$aa",
            ],
            'Preverb': [
                "g_$alksi",
                "ksi",
                "g$ukws",
            ],
            'IntransitiveVerb': [
                "kwsd$ins",
                "'$aat'iks",
            ]
        }
        super().setUpClass(BASIC_EW, test_stems)

    def test_xsi_ksi(self):
        self.assertNotEqual(len(self.fst.analyze("ksi")), 0)
        self.assertNotEqual(len(self.fst.analyze("xsi")), 0)

    def test_ksi_tag(self):
        self.assertIn("ksi+PVB", self.fst.analyze("xsi"))  # <XSKS>

    def test_galxsi_galksi(self):
        self.assertNotEqual(len(self.fst.analyze("g̲alksi")), 0)
        self.assertNotEqual(len(self.fst.analyze("g̲alxsi")), 0)

    def test_amxsiwaa_amksiwaa(self):
        self.assertNotEqual(len(self.fst.analyze("amksiwaa")), 0)
        self.assertNotEqual(len(self.fst.analyze("amxsiwaa")), 0)

    def test_aks_no_change(self):
        self.assertNotEqual(len(self.fst.analyze("aks")), 0)
        self.assertEqual(len(self.fst.analyze("axs")), 0)

    def test_xwsdins_kwsdins(self):
        self.assertNotEqual(len(self.fst.analyze("kwsdins")), 0)
        self.assertNotEqual(len(self.fst.analyze("xwsdins")), 0)

    def test_guxws_gukws(self):
        self.assertNotEqual(len(self.fst.analyze("gukws")), 0)
        self.assertNotEqual(len(self.fst.analyze("guxws")), 0)

    def test_aatixs_aatiks(self):
        self.assertNotEqual(len(self.fst.analyze("aat'iks")), 0)
        self.assertNotEqual(len(self.fst.analyze("aat'ixs")), 0)


class TestExcrescentRX(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            'Noun': [
                "l$imx",
                "gitxs$animx_",
                "b$alx",
                "b$ahlx",
            ],
        }
        super().setUpClass(BASIC_EW, test_stems)

    def test_limx_limix(self):
        self.assertNotEqual(len(self.fst.analyze("limx")), 0)
        self.assertNotEqual(len(self.fst.analyze("limix")), 0)

    def test_limix_tag(self):
        self.assertIn("l$imx+N", self.fst.analyze("limix"))  # <IMIX>

    def test_imx_imax(self):
        self.assertNotEqual(len(self.fst.analyze("gitxsanimx̲")), 0)
        self.assertNotEqual(len(self.fst.analyze("gitxsanimax̲")), 0)

    def test_ilx_ilix(self):
        self.assertNotEqual(len(self.fst.analyze("balx")), 0)
        self.assertNotEqual(len(self.fst.analyze("balix")), 0)

    def test_ihlx_no_ihlix(self):
        self.assertNotEqual(len(self.fst.analyze("bahlx")), 0)
        self.assertEqual(len(self.fst.analyze("bahlix")), 0)


if __name__ == '__main__':
    unittest.main()
