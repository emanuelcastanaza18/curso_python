# class Perro:
#     def __init__(self, nombre, edad):
#         # self.__nombre le daremos a las teclas control + shif + p para busvar Rename Symbol para cambiar ambas partes
#         self.__nombre = nombre
#         self.edad = edad

#     def habla(self):
#         print(f"{self.__nombre} dice: Guau!")

#     @classmethod
#     def factory(cls):
#         return cls("Firulais", 5)


# perro1 = Perro.factory()
# perro1.habla()


# Para acceder al nombre del perro crearemos un metodo

# class Perro:
#     def __init__(self, nombre, edad):
#         # self.__nombre le daremos a las teclas control + shif + p para busvar Rename Symbol para cambiar ambas partes
#         self.__nombre = nombre
#         self.edad = edad

#     def get_nombre(self):
#         return self.__nombre

#     def habla(self):
#         print(f"{self.__nombre} dice: Guau!")

#     @classmethod
#     def factory(cls):
#         return cls("Firulais", 5)


# perro1 = Perro.factory()
# perro1.habla()
# print(perro1.get_nombre())

# para cambiar el nombre del perro pero debemnos de validar que el nombre

# class Perro:
#     def __init__(self, nombre, edad):
#         self.__nombre = nombre
#         self.edad = edad

#     def get_nombre(self):
#         return self.__nombre

#     def set_nombre(self, nombre):
#         self.__nombre = nombre

#     def habla(self):
#         print(f"{self.__nombre} dice: Guau!")

#     @classmethod
#     def factory(cls):
#         return cls("Firulais", 5)


# perro1 = Perro.factory()
# perro1.habla()
# print(perro1.get_nombre())


#Para poder acceder a las propidedades privadas de una clase se puede hacer de la siguiente manera OJo no es recomendable
class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Firulais", 5)


perro1 = Perro.factory()
perro1.habla()
print(perro1._Perro__nombre)