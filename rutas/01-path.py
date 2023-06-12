from pathlib import Path

# path nos sirve para diferenciar entre una ruta dentro de nuestras maquinas
# y no necesariamente tiene que existir

#para windows debemos de hacerlo de la sigueinte manera 
# Path(r"") #La R significa que es una raw string y esto lo usaremos para que no nos tome backslash como un caracter de escape
Path(r"C:\Archivos del Programa\Minecraft")

#Rutas en linux
Path("/usr/local/bin")

#Ruta dependiendo de donde nos encontremos
Path() #Este nos servira cuando tengamos User/home/Mi-app
Path.home() #Este nos servira cuando tengamos Uuna carpeta Home del usuario en donde se encuentre ejecutando el script
Path("one/__init__.py") #Este nos sirve para generar rutas a Archivos 
