
from core import *

def estadistica(datos):
 
    datos_limpios = limpieza(datos)
    km_totales = total_kms(datos_limpios)
    # media_km = km_totales / len(datos_limpios)
    media_km = media_total(km_totales, datos_limpios)
    deporte_con_mas_km = deporte_mas_km(datos_limpios)

    salida = {"total_km": km_totales, "media_km": media_km, "deporte_top": deporte_con_mas_km}
    
    return salida