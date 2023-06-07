class Perro:
    # self es una palabra reservada que se utiliza para referirse alas instancias de las clases
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Chanchito", 1)
mi_perro.habla()
# print(mi_perro.nombre)
# print(mi_perro2.nombre)
