# from abc import ABC, abstractmethod


# class Model(ABC):
#     @abstractmethod
#     def guardar(self):
#         pass


# class Usuario(Model):
#     def guardar(self):
#         print("Guardando usuario")

# # Las sesiones son las que le permite al servidor identificar cuando un usuario se esta conectando al igual que
# # aquien pertenece las peticiones que el usuario esta haciendo
# class Sesion(Model):
#     def guardar(self):
#         print("Guardando en archivo")


# def guardar(entidad):
#     entidad.guardar()


# usuario = Usuario()
# sesion = Sesion()

# guardar(sesion)

# Para recibir en vez de una entidad acepte una lista de entidades
# from abc import ABC, abstractmethod


# class Model(ABC):
#     @abstractmethod
#     def guardar(self):
#         pass


# class Usuario(Model):
#     def guardar(self):
#         print("Guardando usuario")


# class Sesion(Model):
#     def guardar(self):
#         print("Guardando en archivo")


# def guardar(entidades):
#     for entidad in entidades:
#         entidad.guardar()


# usuario = Usuario()
# sesion = Sesion()

# #([sesion, usuario]) A esto le llamamos polimorfismo
# guardar([sesion, usuario])


# Duck typing

class Usuario():
    def guardar(self):
        print("Guardando usuario")


class Sesion():
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])
