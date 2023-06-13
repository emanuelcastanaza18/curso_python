# from pathlib import Path

# path = Path("directorio")
# path.exists()
# path.mkdir()  # Esto nos sirve para crear un directorio
# path.rmdir()  # Esto nos sirve para eliminar un directorio, pero con la condicion quie este vacio
# path.rename("chancito-feliz")  # Esto nos sirve para renombrar un directorio


# from pathlib import Path

# path = Path("rutas")
# print(path.iterdir()) #Nos devuelve un objeto generador (El resultado se puede iterar)

# Ahora para trabajar con un for

# from pathlib import Path
#
# path = Path("rutas")
#
# for p in path.iterdir():
# print(p)

# Compresion de listas objetc en una lista
# from pathlib import Path
#
# path = Path("rutas")
#
# archivos = [p for p in path.iterdir() if not p.is_dir()]
# print(archivos)

# Otras alternativas que se tienen

from pathlib import Path

path = Path("rutas")

archivos = [p for p in path.iterdir() if not p.is_dir()]
# Para seleccionar un archivo pero que contengan un patron
# archivos = [p for p in path.glob("*.patron")]
# archivos = [p for p in path.glob("*.py")]
# archivos = [p for p in path.glob("01-*.py")]
# Para incluir de manera recursiva
# archivos = [p for p in path.glob("**/*.py")]
#rglob es por recursivo
archivos = [p for p in path.rglob("*.py")]
print(archivos)
