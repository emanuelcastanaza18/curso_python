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

#Otra forma de hacerlo
usuarios = [
    ["chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = [expresion for item in items]
nombres = [usuario[0] for usuario in usuarios]
print(nombres)