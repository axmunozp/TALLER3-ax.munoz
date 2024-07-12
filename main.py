from models.huron import Huron
from models.boa_constrictor import Boa_Constrictor
from models.guarderia import Guarderia

## Creación de objetos tipo Huron
huron1 = Huron("Pepito",15,3,"Ecuador",25.300)
##Creación de objetos tipo Boa
boa1= Boa_Constrictor("Serpentina",6,1,"Peru",36.400)
boa2= Boa_Constrictor("Luz",5,3,"Peru",36.400)


guarderia = Guarderia()
guarderia.boas[0] = boa1
guarderia.boas[1] = boa2

# Intentar alimentar una boa que existe
print(guarderia.alimentar_boa(2))  

for i in range(11):
    print(guarderia.alimentar_boa(0))
    i += 1
