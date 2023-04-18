animal = " chanCHito feliz "
print(animal.upper())
print(animal.lower())
# Con el strip borraremos los espacios
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())
# Con este sacamos solo el indice
print(animal.find("cH"))
# En el metodo replace("", "")) en el primero colocaremos las letras de las cuelaes queremos cambiar y en el segundo se coloca la letra de la cual se reemplaza
print(animal.replace("nCH", "j"))
# Con esta funcion nos devuelve un booleano
print("nCH" in animal)
print("nCH" not in animal)
