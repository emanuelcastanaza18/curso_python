class Model:
    tabla = False

    # Esto es el constructor
    def __init__(self):
        if not self.tabla:
            print("Error tienes que definir una tabla")

    # Esto es un metodo
    def guardar(self):
        print(f"Guardando {self.tabla} eb BBDD")

    # metodo para ir a buscar elementos a la bbdd
    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando en la tabla {self.tabla} el id {_id}")


class Usuario(Model):
    tabla = "Usuario"


# Instancia
usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(123)
