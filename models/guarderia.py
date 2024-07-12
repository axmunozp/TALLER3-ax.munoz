from models.huron import Huron
from models.boa_constrictor import Boa_Constrictor

class Guarderia:
    def __init__(self):
        self.boas = [None, None] 
        self.hurones = [None, None]  

    def alimentar_boa(self, index):
        try:
            boa = self.boas[index]
            if boa is None:
                raise ValueError("Esta Boa no existe!")
            mensaje = boa.comer_raton()
            return mensaje
        except (IndexError, ValueError) as e:
            return str("Esta Boa no existe!")


