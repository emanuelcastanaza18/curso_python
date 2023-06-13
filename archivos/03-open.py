# from io import open

# # Escritura
# texto = "Hola mundo"

# Para modo de escritura se utiliza "w"
# archivo = open("archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# lectura
# from io import open

# # Para modo de lectura se utiliza "r"
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista
# from io import open


# archivo = open("archivos/hola-mundo.txt", "r")
# # Leera todas las lineas
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# # Metodos magicos
# metodo de with
# from io import open

# # With se encargara de cerrar nuestros archivos de manera automatica sin que se lo indiquemos
# with open("archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     for linea in archivo:
#         print(linea)

# Con el metodo de seek podemos indicarle en que posicion queremos que se encuentre el puntero
# from io import open


# with open("archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# Solo agregar una caosa a un archivo

# agregar
# from io import open

# archivo = open("archivos/hola-mundo.txt", "a+")
# archivo.write(" Chao mundo :(")
# archivo.close()


# leer y escritura
from io import open

with open("archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito feliz la "
    archivo.writelines(texto)

