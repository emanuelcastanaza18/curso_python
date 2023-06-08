class Animal:
    def comer(self):
        print("El animal está comiendo")


class Perro(Animal):

    def comer(self):
        print("El perro está comiendo")


class Chanchito(Animal):

    def programar(self):
        print("Chanchito programando")


chanchito = Chanchito()
chanchito.comer()
print("Chanchito programando")
