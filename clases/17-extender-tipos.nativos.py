# lista = list([1, 2, 3])

# lista.append(4)

# # metodo intiuivo
# lista.insert(0, 0)


# print(lista)

# Otra forma de hacerlo
class Lista(list):
    # prepend agrega los elementos al inicio de la lista
    def prepend(self, item):
        self.insert(0, item)


lista = Lista([1, 2, 3])
lista.append(4)
lista.prepend(0)

print(lista)
