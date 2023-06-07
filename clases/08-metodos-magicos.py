# class Perro:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def __str__(self):
#         return f"Perro: {self.nombre}"

#     def habla(self):
#         print(f"{self.nombre} dice: Guau!")


# perro = Perro("Firulais", 5)
# print(perro)
# texto = str(perro)
# print(texto)


#magic methods python-> https://rszalski.github.io/magicmethods/



#Metodo Destructor
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chao Perro :( {self.nombre} ha sido eliminado")

    def __str__(self):
        return f"Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Firulais", 5)
del perro