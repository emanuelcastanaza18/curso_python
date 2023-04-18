# Que significa kwargs W es Key y la W de words args es de argumentos

def get_product(**datos):
    print(datos["id"], datos["name"])
    # para llamar o mejor dicho para mostrar en pantalla los datos debemos de ingresarlos con [] y comillas dobles ""


# al momento de usar el kwargs debemos de tomar en cuenta que se debe colocar una variable para que nos deje trabajar ya que le pusimos el ** doble
# el resultado que entrega es {'id': 'id'} que tiene por nombre diccionario
get_product(id="23",
            name="iPhone",
            desc="Esto es un iPhone")  # Primero lo que nos refleja es el parametro y despues nos muestra el argumento es decir {'id': <-parametro 'id'<-argumento,
