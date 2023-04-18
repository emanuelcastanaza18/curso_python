def suma(*numeros):  # el * vuelve a nuestros parametros como (iterables)
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)  # tener cuidado con la identacion porque si lo dejamos tal y como esta al momento de darle enter pueden aparecer varios resultados


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)
