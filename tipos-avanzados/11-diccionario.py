#Son una conexion de datos 

# Diccionarios
# punto = {"x": 2, "y": 3}
# print(punto)   
# print(punto["x"]) 
# print(punto["y"]) 


# punto["z"] = 45
# print(punto)

#para acceder a un valor cuya llave no existe
# punto = {"x": 2, "y": 3}
# print(punto)   
# print(punto["x"]) 
# print(punto["y"]) 


# punto["z"] = 45
# # print(punto, punto["lalala"])

# if "lalala" in punto:
#     print("Encontre lo que buscas Puto",punto["lalala"])


#para acceder a un valor del diccionario sin que explote 
# punto = {"x": 2, "y": 3}
# print(punto)   
# print(punto["x"]) 
# print(punto["y"]) 


# punto["z"] = 45

# if "lalala" in punto:
#     print("Encontre lo que buscas Puto",punto["lalala"])

# print(punto.get("x"))
# print(punto.get("lala", 97))

#para alguna llave o su valor 
# punto = {"x": 2, "y": 3}
# print(punto)   
# print(punto["x"]) 
# print(punto["y"]) 


# punto["z"] = 45

# if "lalala" in punto:
#     print("Encontre lo que buscas Puto",punto["lalala"])

# print(punto.get("x"))
# print(punto.get("lala", 97))
# del punto["x"]
# del (punto["y"])
# print(punto)


#para iterar el valor 
# punto = {"x": 2, "y": 3}
# print(punto)   
# print(punto["x"]) 
# print(punto["y"]) 


# punto["z"] = 45

# if "lalala" in punto:
#     print("Encontre lo que buscas Puto",punto["lalala"])

# print(punto.get("x"))
# print(punto.get("lala", 97))
# del punto["x"]
# del (punto["y"])
# print(punto)
# punto["X"] = 25

# for valor in punto:
#     print(valor, punto[valor])

# for valor in punto.items():
#     print(valor)

# for llave,valor in punto.items():
#     print(llave,valor)



#para un listado de usuarios
punto = {"x": 2, "y": 3}
print(punto)   
print(punto["x"]) 
print(punto["y"]) 


punto["z"] = 45

if "lalala" in punto:
    print("Encontre lo que buscas Puto",punto["lalala"])

print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del (punto["y"])
print(punto)
punto["X"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave,valor in punto.items():
    print(llave,valor)

usuarios = [
     #{} <--- identificador unico 
     {"id":1, "nombre":"Chanchito"},
     {"id":2, "nombre":"Feliz"},
     {"id":3, "nombre":"Emanuel"},
     {"id":4, "nombre":"Castaniaza"},
]

for usuario in usuarios:
    print(usuario["nombre"])