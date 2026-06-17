from datos import *

def limpieza_datos(datos):

    datos_limpios=[]
    
    if not datos:
        return []
    else:

        for n in datos:
            if isinstance(n, tuple) and len(n)==2 and isinstance(n[0], (str)) and isinstance(n[1], (int,float)):
                datos_limpios.append(n)

        return datos_limpios
    
    

def filtra_deporte(datos, deporte):

    deporte_filtrado = []
    
    for clave, valor in datos:
        if clave == deporte:
           deporte_filtrado.append((clave, valor))

    return deporte_filtrado 


def suma_deporte_filtrado(datos):

    suma_km = 0
    for clave, valor in datos:
        suma_km += valor

    return suma_km


def media_deporte_filtrado(datos, km):

    if len(datos)>0:
        return round(km / len(datos),2)
    
    return 0