def suma(a, b):
    resultado = a+b
    return resultado


# para poder utilizar en otra apolicacion antes debemos de ponerle una variable al inicio despues el igual tal y como lo muestra el ejemplo
c = suma(1, 2)
d = suma(c, 2)

print(d)
# al momento de imprimir nos muestra que relizo la primera parte 1+2= 3 y en la segunda lo que hizo fue tomar el 3 de la primera y sumar el segundo valor que ya se tenia
