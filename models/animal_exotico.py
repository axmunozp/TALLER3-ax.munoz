from models.animal import Animal
from abc import ABC, abstractmethod

class Animal_Exotico(Animal, ABC):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos) -> None:
        super().__init__(nombre, peso, edad)
        self.__pais_origen = pais_origen
        self.__impuestos = impuestos
    
    def calcular_flete(self):
        return round(self.__impuestos * self._peso,2)
    
    @abstractmethod
    def hacer_sonido(self):
        pass

