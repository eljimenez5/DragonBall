class Persona:
    def __init__(self, nombre, apellidos, edad):
        self.nombre= nombre
        self.apellidos= apellidos
        self.edad= edad

    def Nombre(self):
        print(self.nombre + " Este es mi nombre")

p1 = Persona("Francis", "Jiménez", 20)

p1.Nombre()
print(p1.nombre)
print(p1.edad)