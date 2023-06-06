# lista1 = [1, 2, 3, 4]
# print(*lista)


# Combinar listas
# lista1 = [1, 2, 3, 4]
# lista2 = [5, 6]
#
# combinada = ["Hola",*lista1,"Mundo", *lista2,"Sebastian"]
# print(combinada)


# Para usar en los diccionarios
punto1 = {"x": 19, "y": "Pendejos"}
punto2 = {"y": 15}

nuevopunto = {**punto1, "lala": "Nicolas", ** punto2, "z": "mundo"}
print(nuevopunto)
