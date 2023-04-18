# saludo = "Hola Global"  # <- Esto es mala Practica.


# def saludar():
#     saludo = "Hola Mundo"


# def saludaChancito():
#     saludo = "Hola Chanchito"
#     print(saludo)


# saludar()
# print(saludo)

# # El usar variable globales estamos haciendo una mala pratica.


# Como usar las variables globales (De PREFERENCIA NO USAR)
saludo = "Hola Global"  # <-Esta es la variable


def saludar():
    global saludo  # <- Aqui llamamos a la variable que se definio en la parte de arriba
    saludo = "Hola Mundo"


def saludaChancito():
    saludo = "Hola Chanchito"
    print(saludo)


print(saludo)
saludar()
print(saludo)

# El usar variable globales estamos haciendo una mala pratica.
