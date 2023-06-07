# Ejercicio 1 Eliminar los espacions en blanco de un string y devolver una lista con los caracteres restantes
# string = "Hola Mundo"


# def eliminar_espacios(texto):
#         return [char for char in texto if char != " "]


# sin_espacions=quit_espacios=eliminar_espacios(string)
# print(sin_espacions)

# Ejecicio 2 contar en un diccionario cuanto se repiten los caracteres de un string
# from pprint import pprint
# string = "Hola Mundo"


# def eliminar_espacios(texto):
#     return [char for char in texto if char != " "]


# def cuenta_caracteres(lista):
#     diccionario = {}
#     for char in lista:
#         if char in diccionario:
#             diccionario[char] += 1
#         else:
#             diccionario[char] = 1
#     return diccionario


# sin_espacions = quit_espacios = eliminar_espacios(string)
# contadoa = cuenta_caracteres(sin_espacions)
# pprint(contadoa, width=1)

# Ejercicio 3 ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas
# [("a",3),("b",2),("c",4), ("d",1)]

# from pprint import pprint
# string = "Hola Mundo"
#
#
# def eliminar_espacios(texto):
# return [char for char in texto if char != " "]
#
#
# def cuenta_caracteres(lista):
# diccionario = {}
# for char in lista:
# if char in diccionario:
# diccionario[char] += 1
# else:
# diccionario[char] = 1
# return diccionario
#
#
# def ordenar(diccionario):
# return sorted(
# diccionario.items(),
# key=lambda key: key[1])
#
#
# sin_espacions = quit_espacios = eliminar_espacios(string)
# contadoa = cuenta_caracteres(sin_espacions)
# ordenados = ordenar(contadoa)
# print(ordenados)
# para ordenar de manera ascendente
# from pprint import pprint
# string = "Hola Mundo"


# def eliminar_espacios(texto):
#     return [char for char in texto if char != " "]


# def cuenta_caracteres(lista):
#     diccionario = {}
#     for char in lista:
#         if char in diccionario:
#             diccionario[char] += 1
#         else:
#             diccionario[char] = 1
#     return diccionario


# def ordenar(diccionario):
#     return sorted(
#         diccionario.items(),
#         key=lambda key: key[1],
#         reverse=True)


# sin_espacions = quit_espacios = eliminar_espacios(string)
# contadoa = cuenta_caracteres(sin_espacions)
# ordenados = ordenar(contadoa)
# print(ordenados)

# Ejercicio 4 de un listado de tuplas, devolver las tuplas que tengan el mayor valor
# from pprint import pprint
# string = "Hola Mundo hoy es navidad"


# def eliminar_espacios(texto):
#     return [char for char in texto if char != " "]


# def cuenta_caracteres(lista):
#     diccionario = {}
#     for char in lista:
#         if char in diccionario:
#             diccionario[char] += 1
#         else:
#             diccionario[char] = 1
#     return diccionario


# def ordenar(diccionario):
#     return sorted(
#         diccionario.items(),
#         key=lambda key: key[1])


# def mayores_tuplas(lista):
#     maximo = lista[0][1]
#     respuesta = {}
#     for orden in lista:
#         if maximo > orden[1]:
#             break
#         respuesta[orden[0]] = orden[1]
#     return respuesta


# sin_espacions = quit_espacios = eliminar_espacios(string)
# contados = cuenta_caracteres(sin_espacions)
# ordenados = ordenar(contados)
# mayores = mayores_tuplas(ordenados)
# print(mayores)


# ejercicio 5  Crear un mensaje que diga  los caracteres que mas se repiten
from pprint import pprint
string = "Hola Mundo hoy es navidad"


def eliminar_espacios(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    diccionario = {}
    for char in lista:
        if char in diccionario:
            diccionario[char] += 1
        else:
            diccionario[char] = 1
    return diccionario


def ordenar(diccionario):
    return sorted(
        diccionario.items(),
        key=lambda key: key[1])


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(diccionario):
    # \n para generar una nueva linea
    mensaje = "Los caracteres que mas se repiten son: \n "
    for key, valor in diccionario.items():
        mensaje += f" -{key} con {valor} repeticiones \n"
    return mensaje


sin_espacions = quit_espacios = eliminar_espacios(string)
contados = cuenta_caracteres(sin_espacions)
ordenados = ordenar(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
print(mensaje)
