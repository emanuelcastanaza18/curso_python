# class nombre de que queramos indicar
class Perro:  # Usar siempre Mayusculas Primero
    def habla(self):  # <---- Ya no se llamaran funciones, ahora se llaman metodos
        print("Guau")


mi_perro = Perro()
print(type(mi_perro))

#para llamar al metodo de habla
mi_perro.habla()

#Para verificar si el objeto creado pertenece o es instancia de la clase
# print(objeto(clase))
print(isinstance(mi_perro, Perro))
