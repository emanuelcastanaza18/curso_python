# ordenenar nuestros numeros
# numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 45, 72, 75, 22]

# numeros.sort() #<- Ordena nuestro listado
# print(numeros)

# Ordenar de manera descendente
# numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 45, 72, 75, 22]

# numeros.sort(reverse=True)
# print(numeros)


# # Ordenar de otra manera
# numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 45, 72, 75, 22]

# numeros2 = sorted(numeros)  # <-Devuelve una nueva lista ordenada sin afectar nada
# print(numeros)
# print(numeros2)

# Ordenes los elementos
# numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 45, 72, 75, 22]

# numeros2 = sorted(numeros, reverse=True) # <-Devuelve una nueva lista ordenada alrevez con el metodo de sorted
# print(numeros)
# print(numeros2)

# # ordenar una lista con listas dentro Esto si lo puede ordenar
# usuarios = [
#     [4, "chanchito"],
#     [1, "Felipe"],
#     [5, "Pulga"]
# ]
# usuarios.sort()
# print(usuarios)

# Como ordenar con los valores numericos hasta de ultimo
# usuarios = [
#     ["chanchito", 4],
#     ["Felipe", 1],
#     ["Pulga", 5]
# ]


# def ordena(elemento):
#     return elemento[1]


# usuarios.sort(key=ordena)
# print(usuarios)

# Para ordenarlo alrevez con key y una funcion
# usuarios = [
#     ["chanchito", 4],
#     ["Felipe", 1],
#     ["Pulga", 5]
# ]


# def ordena(elemento):
#     return elemento[1]


# usuarios.sort(key=ordena, reverse=True)
# print(usuarios)

# Funcion lambda
usuarios = [
    ["chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# El usar la palabra lambda nos ahorramos en usar la palabra def un parametro y etc
usuarios.sort(key=lambda el: el[1])
print(usuarios)
