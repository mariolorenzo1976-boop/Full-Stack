
from core import *


# Estadistica global

def estadistica_global_deportes(datos):
    
    datos_limpios = limpieza_datos(datos)   
    total_km = suma_deporte_filtrado(datos_limpios) 
    media_total =  media_deporte_filtrado(datos_limpios, total_km)
    return {"total_km": total_km, "media_km": media_total}


# Estadistica por deporte

def estadistica_por_deporte(datos,deporte):

    datos_limpios = limpieza_datos(datos)
    deporte_filtrado = filtra_deporte(datos_limpios, deporte)
    deporte_filtrado_suma = suma_deporte_filtrado(deporte_filtrado)
    deporte_filtrado_media = media_deporte_filtrado(deporte_filtrado, deporte_filtrado_suma)

    return {"deporte": deporte, "total_km": deporte_filtrado_suma, "media_km": deporte_filtrado_media}