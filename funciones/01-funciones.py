# Para crear funciones
# def hola():
#     print("Hola Mundo!")
#     print("Ultimate Python")


# hola()

# # Para crear funciones con variables
# # El parametro es la variable que estamos llamando dentro de la funcion
# def hola(nombre, apellido):
#     print("Hola Mundo!")
#     print(f"Bienvenido {nombre} {apellido}")


# # Es el argumento que estamos llamando es decir hola("Emanuel")
# hola("Emanuel", "Cataniaza")
# hola("Chanchito", "Feliz")


# Funciones cuando eliminamos un argumento al momento que no se lo pasemos
def hola(nombre, apellido="Feliz"):
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Emanuel", "Cataniaza")
hola("Chanchito")


# Ejemplo si se quiere pasar de primero el apellido y despues el nombre
hola(apellido="Cataniaza", nombre="Diego")
