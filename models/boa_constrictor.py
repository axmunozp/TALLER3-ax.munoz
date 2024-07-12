from models.animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 0
    
    def hacer_sonido(self):
        return "¡Tsss!"

    def comer_raton(self):
        if self._ratones_comidos >= 20:
            raise ValueError("La Boa está llena!")
        self._ratones_comidos += 1
        return "Éxito"


    def contar_ratones_comidos(self) -> int:
        return self._ratones_comidos
