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

# from usuarios.acciones.utilidades import guardar
# guardar()


# Referenciando  subpaquetes
# from usuarios.impuestos.utilidades import pagar_impuestos
#
# pagar_impuestos()


# Funcion dir
# from usuarios.impuestos.utilidades import pagar_impuestos
# import usuarios
#
# La funcion de dir me servira para listar todos los paquetes que se encuentran dentro de un pqquete en especifico
# Esto nos va a servir cuando
# estemos construllendo un framework podremos crear distintos paquetes los cuales haran referencia a distintas partes de la aplicacion
# print(dir(usuarios))

# metodos magicos que nos agrego Python con este cambio del dir
# from usuarios.impuestos.utilidades import pagar_impuestos
# import usuarios

# print(usuarios.__name__)  # Este nos muestra el nombre del paquete
# print(usuarios.__package__)  # Este nos muestra el nombre del paquete perser
# # Este nosmuestra dentro de un listado el lugar o la ruta en especifico donde se encuentra el paquete
# print(usuarios.__path__)
# # Este nos muestra el nombre del archivo a cual esta hacidendo referencia
# print(usuarios.__file__)

# A demas de agregar el nombre de los subpaquetes
#
# from usuarios.impuestos.utilidades import pagar_impuestos
# import usuarios

# print(usuarios.gestion.__name__)
# print(usuarios.impuestos.__package__)
# print(usuarios.gestion.__path__)
# print(usuarios.impuestos.__file__)


# Paquetes con nombres dinámicos
# from usuarios.impuestos.utilidades import pagar_impuestos
# pagar_impuestos()
# print(__name__)


# Otra forma
from usuarios.impuestos.utilidades import pagar_impuestos
pagar_impuestos()
