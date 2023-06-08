# class Ave:
#     def vuela(self):  # <--Clase padre
#         print("Vuela ave")


# class Pato(Ave):      # <--subclase
#     def vuela(self):
#         # super() #<---- Nos entrega acceso inmediato a la clase padre
#         print("Vuela pato")
#         super().vuela()


# pato = Pato()
# pato.vuela()

# Para agregarlo en el contructor
class Ave:
    def __init__(self):
        self.volador = "volador"

    def vuela(self):
        print("Vuela ave")


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = "nadador"

    def vuela(self):
        print("Vuela pato")


pato = Pato()
pato.vuela()
print(pato.nada, pato.volador)
