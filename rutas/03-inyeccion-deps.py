# Esto me permite poder volver a utilizar en otra parte del codigo
# class Perro:
#     def __init__(self, Correa):
#         self.correa = Correa()


# otro ejemplo con funciones
# import usuario

# #Ejemplo sin inyeccion de dependencias
# def guardar():
#     usuario.guardar()

# #Ejemplo con inyeccion de dependencias
# #Le pasamos la entidad que tenga el metodo de guardar
# #Ventajas: Nos permite reutilizar mas el codigo, Nos permite desacoplar el codigo para que sea mas facil de reutilizar, Cuando empecemos a utilziar el tests sera muy sencillo
# def guardar(entidad):
#     entidad.guardar()

# Ejemplo 3
# flask necesita que mi aplicacion tenga un metodo de init_app, configura rutas pero de un appirest , inicializar nuestra base de datos y nos permitira importas mas paquetes
# def init_app(bbdd, api):
# Inicializamos la base de datos


# Ejemplo 4

# from pathlib import Path

# path = Path("")
# paths = [p for p in path.iterdir() if p.is_dir()]

# def load(p):
#     paquete: __import__(str(p).replace("/", "."))
#     try:
#         paquete.init_app()
#     except:
#         print("El paquete no tiene funcion init")


# map(load, paths)


from pathlib import Path
import db
import graphql
import api

path = Path("")
paths = [p for p in path.iterdir() if p.is_dir()]

dependecia = {
    "db": db,
    "api": graphql,
    "graphql": api
}


def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependecia)
    except:
        print("El paquete no tiene funcion init")


list(map(load, paths))
