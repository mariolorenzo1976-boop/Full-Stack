def limpia_datos(datos):

    
    nueva_lista = []
    nueva_lista_2 = []
    
    
    if not datos:
        return []
    else:
        for n in datos:
            if isinstance(n, (tuple)) and len(n) == 2:
               nueva_lista.append(n)
            
        for clave, valor in nueva_lista:
            if isinstance(valor, (int,float)):
               n = clave, valor
               nueva_lista_2.append(n)
    
        return nueva_lista_2



def suma_km(datos_limpios):
    
    suma_total_km = 0
    for clave, valor in datos_limpios:
        suma_total_km += valor
    
    return suma_total_km


def media_global(datos_limpios):

    if not datos_limpios:
        return 0
    else:
        media_gobal_km = suma_km(datos_limpios) / len(datos_limpios)
        return media_gobal_km

def deporte_mas_km(datos_limpios):

    deporte_km= {}
    km = 0
    deporte = ""

    for clave, valor in datos_limpios:
       if clave not in deporte_km:
           deporte_km[clave] = 0
       deporte_km[clave] += valor

    for n in deporte_km:
        if deporte_km[n] > km:
            km = deporte_km[n]
            deporte = n

    return deporte



            

