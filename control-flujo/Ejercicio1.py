# Como yo lo realice pendiente de ver el salir
while True:

    num1 = int(input("Ingrese el primer número: "))

    while True:
        print("Seleccione un operador matemático:")
        print("+ Suma")
        print("- Resta")
        print("* Multiplicación")
        print("/ División")
        print("X Salir")
        operador = input()

        num2 = int(input("Ingrese el segundo número: "))

        # if operador.lower() == "salir":
        #     break
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            resultado = num1 / num2
        # elif operador == "X":
        #     resultado = "x"
        #     break

        print("El resultado es:", resultado)

# Como en el video lo realizo

# print("Bienvenido a la Calculadora")
# print("Para salir escribe salir")
# print("Las operaciones son suma,resta,multi,div")

# resultado = ""
# while True:
#     if not resultado:
#         resultado = input("Ingrese numero: ")
#         if resultado.lower() == "salir":
#             break
#         resultado = int(resultado)
#         op = input("Ingrese operacion: ")
#         if op.lower() == "salir":
#             break
#         n2 = input("ingresa el siguiente numero: ")
#         if n2.lower() == "salir":
#             break
#         n2 = int(n2)

#         if op.lower() == "Suma":
#             resultado += n2
#         elif op.lower() == "Resta":
#             resultado -= n2
#         elif op.lower() == "Multi":
#             resultado *= n2
#         elif op.lower() == "Div":
#             resultado /= n2
#         else:
#             print("Operacion no valida")
#             break

#         print(f"El resultado es {resultado}")
