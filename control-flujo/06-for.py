# for numero in range(5):
#     print(numero, numero * 'hola mundo')

# forelse
buscar = 10
for numero in range(5):  # range(5) es un iterable
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No encontre el numero buscado")

for char in "Ultimate Python":
    print(char)
