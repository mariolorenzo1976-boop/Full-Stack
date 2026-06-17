
# Ejercicio 27 - saca un informe con: el total de km, total de registros, media global y el deporte con más km.

def informe_general(datos):

    resultado_informe = {}
    total_km = 0
    deporte_mas_km = {}
    total_registros = len(datos)
    

    for clave, valor in datos:
        if clave not in deporte_mas_km:
            deporte_mas_km[clave] = 0
        deporte_mas_km[clave] += valor
        total_km += valor

    variable = 0
    deporte =""
    for n in deporte_mas_km:
        if deporte_mas_km[n] > variable:
            variable = deporte_mas_km[n]
            deporte = n
    
    media_global = total_km / total_registros
    resultado_informe = {"total_km": total_km, 
                         "total_registros": total_registros, 
                         "media_global": media_global, 
                         "deporte_mas_km": deporte}
    return resultado_informe



datos = [("bici", 100),
         ("run", 30),
         ("bici", 50),
         ("swim", 70),
         ("run", 20)]


print(informe_general(datos))