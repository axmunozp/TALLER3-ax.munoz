from models.huron import Huron
import unittest

class TestHuron(unittest.TestCase):
    def test_hacer_sonido(self):
        huron = Huron("Pepito",15,3,"Ecuador",25.300)
        self.assertEquals(huron.hacer_sonido(), "¡Eek Eek!")


    def test_calcular_flete(self):
        boa = Huron("Pepito",15,3,"Ecuador",25.300)
        self.assertEqual(boa.calcular_flete(), 379.5)