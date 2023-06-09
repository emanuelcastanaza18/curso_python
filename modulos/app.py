# Es una pesima practica colocar el * al finalizar el import es decir from accion import * ya que se pueden sobreescribir funciones

# Esto unicamente nos mostrara el mensaje de "Guardando usuario" ya que el import * sobreescribe la funcion guardar
# from usuarios import *
#
# def guardar():
#     print("Guardando usuario")
# guardar()

# En este caso si lo colocamos en la parte de arriba nos mostrara el mensaje de usuario_impuestos
# from usuarios import *
#
# guardar()

# def guardar():
#     print("Guardando usuario")


# Para importar un archivo que contiene multiples palabras debemos de hacerlo de la siguiente manera colocando un _ entre cada palabra

# from usuarios_impuestos import guardar

# guardar()


# Paquetes
# from nombredelpaquete.nombredelmodulo import funcion

# from usuarios.acciones import guardar
#
# guardar()

# Otra forma de importar

# import usuarios.acciones

# usuarios.acciones.guardar()

# Ademas de poder importar fisicamente lo que nosotros queremos existe otra forma  dentro de un modulo que37 se encuentra dentro de un paquete
# para que nuestro codigo se encuentre mas ordenado

# from usuarios import acciones

# acciones.guardar()


# Subpaquetes

from usuarios.acciones import guardar
guardar()
