# Ejercicio 1 Eliminar los espacions en blanco de un string y devolver una lista con los caracteres restantes
# string = "Hola Mundo"


# def eliminar_espacios(texto):
#         return [char for char in texto if char != " "]


# sin_espacions=quit_espacios=eliminar_espacios(string)
# print(sin_espacions)

# Ejecicio 2 contar en un diccionario cuanto se repiten los caracteres de un string
string = "Hola Mundo"


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


sin_espacions = quit_espacios = eliminar_espacios(string)
contadoa = cuenta_caracteres(sin_espacions)
print(contadoa)
