# Para obtener un elemento y forma en la cual arreglarlo
# numeros = [1, 2, 3]
# primero, *otros = numeros
# print(primero, otros)

# # Para obtener un segundo elemento
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# primero, segundo, *otros = numeros
# print(primero, segundo, otros)

# Para obtener el ultimo elemento
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, *otros, ultimo = numeros
print(primero, ultimo, otros)

# Para obtener el segundo y el penultimo elemento
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros, penu, ultimo = numeros
print(segundo, penu, otros)
