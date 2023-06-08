# Importar un modulo
# abstractmethod: sirve para las propiedaddes o metodos
# abs = Abstract Class y ABC es la clase ala cual se hereda
# from abc import ABC, abstractmethod


# class Model(ABC):
#     # Esto es el constructor
#     def __init__(self):
#         if not self.tabla:
#             print("Error tienes que definir una tabla")

#     @property
#     @abstractmethod
#     def tabla(self):
#         pass

#     # Esto es un metodo
#     def guardar(self):
#         print(f"Guardando {self.tabla} eb BBDD")

#     # metodo para ir a buscar elementos a la bbdd
#     @classmethod
#     def buscar_por_id(self, _id):
#         print(f"Buscando en la tabla {self.tabla} el id {_id}")


# class Usuario(Model):
#     tabla = "Usuario"


# # Instancia
# usuario = Usuario()
# Usuario.buscar_por_id(123)

# Al funcionar lo anterior podemos eliminar nuestro constructor
# from abc import ABC, abstractmethod


# class Model(ABC):
#     @property
#     @abstractmethod
#     def tabla(self):
#         pass

#     # Esto es un metodo
#     def guardar(self):
#         print(f"Guardando {self.tabla} eb BBDD")

#     # metodo para ir a buscar elementos a la bbdd
#     @classmethod
#     def buscar_por_id(self, _id):
#         print(f"Buscando en la tabla {self.tabla} el id {_id}")


# class Usuario(Model):
#     tabla = "Usuario"


# # Instancia
# usuario = Usuario()
# Usuario.buscar_por_id(123)

# Si quisieramos que otro metodo fuera abstracto pero no una propiedad sino un metodo
from abc import ABC, abstractmethod


class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    # metodo para ir a buscar elementos a la bbdd
    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando en la tabla {self.tabla} el id {_id}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print(f"Guardando {self.tabla} eb BBDD")


# Instancia
usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)
