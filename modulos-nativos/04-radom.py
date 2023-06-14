# import random

# lista = ([1, 2, 3, 4, 5, 6, 7, 8])
# lista2 = ([1, 2, 3, 4, 5, 6, 7, 8])
# random.shuffle(lista)
# print(
#     random.random(),
#     random.randint(1, 10),
#     lista,
#     random.choice(lista2),
#     random.choices(lista2, k=3),
#     random.choices("abcdefg", k=3),
#     "".join(random.choices("abcdefg", k=3))

# )

# Ejemplo de para unas contraseñas
import random
import string

lista = ([1, 2, 3, 4, 5, 6, 7, 8])
lista2 = ([1, 2, 3, 4, 5, 6, 7, 8])
random.shuffle(lista)
print(
    random.random(),  # Crear un numero aleatorio
    random.randint(1, 10),  # Podemos indicar de donde hasta donde
    lista,  # Podemos desordenar una lista
    # Podemos indicar que queremos un elemento  aleatorio de una lista
    random.choice(lista2),
    # Podemos indicar que queremos mas de un elemento de forma aleatoria
    random.choices(lista2, k=3),
    random.choices("abcdefg", k=3),  # Podemos aplicar a los string
    "".join(random.choices("abcdefg", k=3))

)

chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices(chars + digitos, k=16)
# print(seleccion)

contrasena = "".join(seleccion)
print(contrasena)
