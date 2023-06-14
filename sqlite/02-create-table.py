import sqlite3

con = sqlite3.connect('sqlite/app.db')
# Para realizar consultas a nuestra base de datos, crearemos un objeto que se llama cursos
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios 
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)
con.commit() #Debemos de llamar al metodo de commit para que se guarden los cambios
con.close()
