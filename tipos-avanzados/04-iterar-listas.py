# los iterables son los string, el resultado de la funcion range <- se trabajan con FOR
mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]

# for mascota in mascotas:
#     print(mascota)

# # Para pasar a una funcion ultilizaremos enumerables para un iterable
# for mascota in enumerate(mascotas):
#     print(mascota)
# (0, 'Pelusa') <- a este resultado con parentecis se le conoce como TUPLA, se pueden acceder a los elementos igual que como un listado

# para llamar unicamente fuera de parentecis debemos de hacer lo siguiente
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
