class prueba:
    atrib_static = 0

    def __init__(self,atrib_dinamic):

        self.atrib_dinamic = atrib_dinamic


C1 = prueba(22)
C2 = prueba(45)

""" C1.atrib_static = 1 """
prueba.atrib_static = 22

print(f"Clase C1 atributo estático: {C1.atrib_static} y atributo dinámico {C1.atrib_dinamic}")
print(f"Clase C1 atributo estático: {C1.atrib_static} y atributo dinámico {C1.atrib_dinamic}")