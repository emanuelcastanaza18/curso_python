from pathlib import Path

# path nos sirve para diferenciar entre una ruta dentro de nuestras maquinas
# y no necesariamente tiene que existir

# #para windows debemos de hacerlo de la sigueinte manera
# # Path(r"") #La R significa que es una raw string y esto lo usaremos para que no nos tome backslash como un caracter de escape
# Path(r"C:\Archivos del Programa\Minecraft")

# #Rutas en linux
# Path("/usr/local/bin")

# #Ruta dependiendo de donde nos encontremos
# Path() #Este nos servira cuando tengamos User/home/Mi-app
# Path.home() #Este nos servira cuando tengamos Uuna carpeta Home del usuario en donde se encuentre ejecutando el script
# Path("one/__init__.py") #Este nos sirve para generar rutas a Archivos.


# Para trabajar con rutas podemos hacer lo siguiente


path = Path("hola-mundo/mi-archivo.py")
# Estos son metodos utiles
path.is_file()  # Esto para saber si es un archivo
path.is_dir()  # Esto para saber si es un directorio
path.exists()  # Esto para saber si existe


print(
    path.name,  # Esto nos regresa el nombre del archivo incluyendo la extension
    path.stem,  # Esto nos regresa el nombre del archivo sin la extension
    path.suffix,  # Esto nos regresa la extension del archivo
    path.parent,  # Esto nos regresa el directorio padre donde nosotros estamos generando esta ruta de poth
    path.absolute()  # Esto nos regresa la ruta absoluta de donde se encuentra el archivo
)

# p = path.with_name("archivo.txt") #Esto nos sirve para cambiar el nombre del archivo, incluyendo la extension
# p = path.with_name("canchito.py")
# print(p)

# p = path.with_suffix(".txt")  # Esto nos sirve para cambiar la extension del archivo
# p = path.with_suffix(".bat")
# print(p)

# p = path.with_stem("archivo")  # Esto nos sirve para cambiar el nombre del archivo sin la extension
p = path.with_stem("feliz")
print(p)
