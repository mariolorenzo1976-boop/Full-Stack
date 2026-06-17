from analisis import *
from datos import *

datos_limpios = limpia_datos(datos)
print(f" la suma de todos los km : ", suma_km(datos_limpios))
print(f" la media global de km: " , media_global(datos_limpios))
print(f" el deporte con más km:", deporte_mas_km(datos_limpios))