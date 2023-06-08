# try:
#     n1 = int(input("Ingrese un numero: "))

# except Exception as e:
#     print("Ocurrió un error!")
# else: #<-- Se ejecuta si no hay error
#     print("Todo salio bien")

# El bloque finally se ejecuta siempre, haya o no error
#Se utilizara siempre sin importar que tenga exito o no

# try:
    # n1 = int(input("Ingrese un numero: "))
# 
# except Exception as e:
    # print("Ocurrió un error!")
# finally:
    # print("Se ejecuta siempre")

#Para encadenar todos los bloques
try:
    n1 = int(input("Ingrese un numero: "))

except Exception as e:
    print("Ocurrió un error!")
else:
    print("Todo salio bien")
finally:
    print("Se ejecuta siempre")   
