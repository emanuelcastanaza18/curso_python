# def pagar_impuestos():
#     print("Pagando impuestos")

# Para guardar el usuario de cuando ingreso
# Import relativos
# from ..gestion.crud import guardar


# def pagar_impuestos():
#     print("Pagando impuestos")
#     guardar()


#
# Paquetes con nombres dinámicos

# from ..gestion.crud import guardar

# print(__name__)


# def pagar_impuestos():
#     print("Pagando impuestos")
#     guardar()


# Otra forma de importar
# if __name__ != '__main__':
#     from ..gestion.crud import guardar

#     print(__name__)

#     def pagar_impuestos():
#         print("Pagando impuestos")
#         guardar()

# if __name__ == '__main__':
#     print("Tarea en mantenimiento")

# Tenemos 2 opciones para importar un paquete dentro de otros paquetes
if __name__ != '__main__':
    # Imports absolutos
    from usuarios.gestion.crud import guardar

    print(__name__)

    def pagar_impuestos():
        print("Pagando impuestos")
        guardar()

if __name__ == '__main__':
    print("Tarea en mantenimiento")
