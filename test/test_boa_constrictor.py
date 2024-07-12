import unittest 
from models.boa_constrictor import Boa_Constrictor

class TestBoaContrictor(unittest.TestCase):

    def test_hacer_sonido(self):
        boa = Boa_Constrictor("Serpentina",6,1,"Peru",36.400)
        self.assertEqual(boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        boa = Boa_Constrictor("Serpentina",6,1,"Peru",36.400)
        self.assertEqual(boa.calcular_flete(), 218.4)
    
    def test_comer_raton(self):
        boa = Boa_Constrictor("Serpentina",6,1,"Peru",36.400)
        self.assertEqual(boa.comer_raton(),"Éxito")