def division(n=0):
    if n == 0:
        # Como saber que excepcion lanzar, nos basamos a la documentacion de python que esta en python error and exceptions y en el link de https://docs.python.org/3/library/exceptions.html
        raise ZeroDivisionError("No se puede dividir por cero", f"{n}")
    return 5 / n


try:
    division()
except ZeroDivisionError as e:
    print(e)

# Nota no se deberi de enviar excepciones muy segudias ya que son costosas en el rendimiento de la aplicacion
# Sin embargo queremos que nuestros errores sean explicitos  lanzar un par de excepciones es bueno para que el usuario sepa que esta pasando
# Las excepciones se pueden crear customizadas
