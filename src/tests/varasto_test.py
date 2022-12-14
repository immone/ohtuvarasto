import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(10, -1)
        self.varasto3 = Varasto(10, 11)
        self.varasto4 = Varasto(-1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
	
    def test_otetaan_liikaa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        
    def test_otetaan_neg(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0.0)
	
    def test_laitetaan_liikaa(self):
        self.varasto.ota_varastosta(5)
        self.varasto.lisaa_varastoon(6)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
     
    def test_saldo(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)
     
    def test_saldo2(self):
        self.assertAlmostEqual(self.varasto3.saldo, 10)
        
    def test_tilavuus(self):
        self.assertAlmostEqual(self.varasto4.tilavuus, 0.0)
      
    def test_lisaa_varastoon_metodi(self):
        self.assertEqual(self.varasto.lisaa_varastoon(-1), None)
    
    def test_ota_varastosta_neg(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0.0)
     
    def test_kokeile_str(self):
        self.assertEqual(self.varasto3.__str__(), "saldo = 10, vielä tilaa 0")
		
		
		
		