# Ejercicio 28 - saca un informe con: el total de km, total de registros, media global y el deporte con más km. en fusiones separadas

def total_km(datos):
    
    km_totales = 0
    for clave, valor in datos:
        km_totales += valor

    return km_totales 

def total_registros(datos):

    registros_total = len(datos)

    return registros_total

def media_global(datos):

    global_media = total_km(datos) / total_registros(datos)

    return global_media

def deporte_mas_km(datos):

    variable = 0
    deporte = ""
    deporte_mas_km = {}
    for clave, valor in datos:
        if clave not in deporte_mas_km:
            deporte_mas_km[clave] = 0
        deporte_mas_km[clave] += valor

    for n in deporte_mas_km:
        if deporte_mas_km[n] > variable:
            variable = deporte_mas_km[n]
            deporte = n    

    return deporte    






datos = [("bici", 100),
         ("run", 30),
         ("bici", 50),
         ("swim", 70),
         ("run", 20)]



print({"total_km" :total_km(datos), "total_registros": total_registros(datos), "media_global": media_global(datos), "deporte_mas_km": deporte_mas_km(datos)})











