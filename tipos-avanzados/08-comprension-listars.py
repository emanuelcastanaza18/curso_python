# Transformacion, de una lista de usuarios a una lista de nombres
# Es decir que quitaremos el valor numerico y dejaremos los nombres

# Uso con FOR
# usuarios = [
#     ["chanchito", 4],
#     ["Felipe", 1],
#     ["Pulga", 5]
# ]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# Para modificar los elementos de una lista
# usuarios = [
#     ["chanchito", 4],
#     ["Felipe", 1],
#     ["Pulga", 5]
# ]


#map
# # nombres = [expresion for item in items]
# nombres = [usuario[0] for usuario in usuarios]
# print(nombres)

# Para filtrarlo
# usuarios = [
#     ["chanchito", 4],
#     ["Felipe", 1],
#     ["Pulga", 5]
# ]

#Filter
# # nombres = [expresion for item in items if lista [id] ]
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombres)

#Map
# usuarios = [
    # ["chanchito", 4],
    # ["Felipe", 1],
    # ["Pulga", 5]
# ]
# 
# #nombres = list(map(lambda usuario item: Valor que deseamos retornar[Elemento], Que queremos iterar))
# nombres = list(map(lambda usuario: usuario[0], usuarios))
# print(nombres)

#Filter
usuarios = [
    ["chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# menosusuarios = list(map(lambda usuario item: Valor que deseamos retornar[Elemento], Que queremos iterar))
menosusuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosusuarios)