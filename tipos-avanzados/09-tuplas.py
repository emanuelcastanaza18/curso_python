#las tuplas no se pueden modificar
numeros = (1,2,3,4,5,6,7,8,9,0) + (10,11,12,13,14,15,16,17,18,19,20)
print(numeros)


punto = tuple((1,2))
print(punto)
menosnumeros = numeros[:2]
print(menosnumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)


#No se puede modificar
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito Feliz"
print(listaNumeros)