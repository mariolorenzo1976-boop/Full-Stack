from core import *
from datos import *
# from datos import *

def informe(datos):
    datos_limpios = limpia_datos(datos)
    
    informe_datos = {"total km": suma_km(datos_limpios), "media": media_global(datos_limpios), "top_deporte": deporte_mas_km(datos_limpios)}
    
    return informe_datos