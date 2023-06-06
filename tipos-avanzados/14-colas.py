pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

# Para eliminar una fila
ultimoelemento = pila.pop()
print(ultimoelemento)
print(pila)


# para acceder al ultimo elemento de la pila
print(pila[-1])

# Para una lista que esta complematamente vacia
pila.pop()
pila.pop()
if not pila:
    print("La lista esta vacia")
