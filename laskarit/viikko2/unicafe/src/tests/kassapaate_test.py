import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_alussa_kassassa_rahaa_oikea_maara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_alussa_myytyjen_lounaisen_maara_oikein(self):
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)

    # käteis testit

    def test_kateinen_edullinen_lounas_raha_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(1000),760)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_kateinen_edullinen_lounas_raha_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100),100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)
    
    def test_kateinen_maukas_lounas_raha_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000),600)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_kateinen_maukas_lounas_raha_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(150),150)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,0)

    # kortti testit

    def test_kortti_edullinen_lounas_raha_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),True)
        self.assertEqual(self.kassapaate.edulliset,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.maksukortti.saldo,760)

    def test_kortti_edullinen_lounas_raha_ei_riittava(self):
        self.maksukortti.ota_rahaa(800) # kortin saldo 200
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),False)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.maksukortti.saldo,200)

    def test_kortti_maukas_lounas_raha_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),True)
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.maksukortti.saldo,600)

    def test_kortti_maukas_lounas_raha_ei_riittava(self):
        self.maksukortti.ota_rahaa(700) # kortin saldo 300
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),False)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.maksukortti.saldo,300)


    # kortin lataus

    def test_lataa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,100)
        self.assertEqual(self.maksukortti.saldo,1100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100100)

    def test_lataa_kortilla_negatiininen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-100)
        self.assertEqual(self.maksukortti.saldo,1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

