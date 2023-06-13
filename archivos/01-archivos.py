from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")
archivo.exists()
# archivo.rename("archivos/archivo-renombre.txt")
# archivo.unlink()

# print(archivo.stat())
print("Aceceso", ctime(archivo.stat().st_atime))  # Fecha de acceso
print("Creacion", ctime(archivo.stat().st_ctime))  # Fecha de creacion
print("Modificacion", ctime(archivo.stat().st_mtime))  # Fecha de modificacion


