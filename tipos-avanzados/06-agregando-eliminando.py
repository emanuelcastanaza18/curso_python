#para insertar un elemento dentro
# mascotas = [
#     "Wolfgang", 
#     "Pelusa", 
#     "Pulga",
#     "Felipe", 
#     "Pulga", 
#     "Chanchito feliz"
# ]
# mascotas.insert(1, "Melvin")
# print(mascotas)

#Para agregar elementos de ultimo
# mascotas = [
#     "Wolfgang", 
#     "Pelusa", 
#     "Pulga",
#     "Felipe", 
#     "Pulga", 
#     "Chanchito feliz"
# ]
# mascotas.append("Chanchito triste")
# print(mascotas)

# #Eliminar elementos dentro de un listado
# mascotas = [
#     "Wolfgang", 
#     "Pelusa", 
#     "Pulga",
#     "Felipe", 
#     "Pulga", 
#     "Chanchito feliz"
# ]
# mascotas.remove("Pulga") #<-Dentro de los parentecis no se debe de colocar el indice, sino debe de ser el ELEMENTO, Esto elimina el primer elemento
# print(mascotas)

#Eliminar el ultimo elemento de un arreglo
# mascotas = [
#     "Wolfgang", 
#     "Pelusa", 
#     "Pulga",
#     "Felipe", 
#     "Pulga", 
#     "Chanchito feliz"
# ] 
# mascotas.pop()
# print(mascotas)

#Eliminar con INDICE
# mascotas = [
#     "Wolfgang", 
#     "Pelusa", 
#     "Pulga",
#     "Felipe", 
#     "Pulga", 
#     "Chanchito feliz"
# ] 
# mascotas.insert(1, "Melvin")
# mascotas.pop(1)
# print(mascotas)

#Eliminar elementos dentro de un arregle
mascotas = [
    "Wolfgang", 
    "Pelusa", 
    "Pulga",
    "Felipe", 
    "Pulga", 
    "Chanchito feliz"
] 
mascotas.insert(1, "Melvin")
mascotas.pop(1)
del mascotas[0] #<- debemos de colocar la palabra DEL el nombre de la variable dentro de corchetes colocaremos el INDICE
print(mascotas)

#Para limpiar completamente el arregle
mascotas = [
    "Wolfgang", 
    "Pelusa", 
    "Pulga",
    "Felipe", 
    "Pulga", 
    "Chanchito feliz"
] 
mascotas.insert(1, "Melvin")
mascotas.pop(1)
del mascotas[0] 
mascotas.clear() #<- para elminar debemos de colocar la variable seguido de .clear() 
print(mascotas)
