# import time

# print(time.time())

# Formato de fecha mas legible
# import datetime
#
# fecha = datetime.datetime(2023, 1, 1)
# print(fecha)

# from datetime import datetime

# fecha = datetime(2023, 1, 1)
# print(fecha)

# formato de fecha

# from datetime import datetime

# fecha = datetime(2023, 1, 1)
# fecha2 = datetime(2023, 2, 1)
# ahora = datetime.now()
# print(fecha)
# print(ahora)


# Otro ejemplo
# from datetime import datetime

# fecha = datetime(2023, 1, 1)
# fecha2 = datetime(2023, 2, 1)
# fechaStr = datetime.strptime("2023/01/01", "%Y/%m/%d")
# # print(fechaStr)
# print(fechaStr.strftime("%Y/%m/%d"))
# print(fecha > fecha2)


# propiedades
from datetime import datetime

fecha = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)
fechaStr = datetime.strptime("2023/01/01", "%Y/%m/%d")
# print(fechaStr)
print(fechaStr.strftime("%Y/%m/%d"))
print(fecha > fecha2)

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute,
)
