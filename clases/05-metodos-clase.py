# class Perro:
# patas = 4
#
# def __init__(self, nombre, edad):
# self.nombre = nombre
# self.edad = edad
#
# @classmethod
# def habla(cls):
# print("Guau!")
#
# Perro.habla()
# Perro1 = Perro("Firulais", 5)
# Perro2 = Perro("Felipe", 3)


# Crear una instancia (factory method)
class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Firulais", 5)


Perro.habla()
Perro1 = Perro("Firulais", 5)
Perro2 = Perro("Felipe", 3)
Perro3 = Perro.factory()
print(Perro3.nombre, Perro3.edad)
