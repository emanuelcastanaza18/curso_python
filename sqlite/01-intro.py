import sqlite3  # Este nos permitira conectarnos a la base de datos sqlite

# Esto intentara conectarse a nuestra base de datos, tomando en cuenta que se esta colocando dentro de las comillas el nombre de la carpeta y el nombre de la base de datos
# Nota importante siempre debemos de cerrar nuestra base de datos
con = sqlite3.connect('sqlite/app.db')
con.close()  # De esta manera cerramos nuestra base de datos
