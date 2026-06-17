# funcion limpieza

def limpieza (datos):

    datos_limpios = [] 
    datos_limpios_2 =[]
    tupla_limpia = ()
    
    if not datos:
        return []
    else:
        for n in datos:
            if isinstance(n, tuple) and len(n) == 2:
                datos_limpios.append(n)

        for clave, valor in datos_limpios:
            if isinstance(valor, (int,float)):
                tupla_limpia = clave, valor
                datos_limpios_2.append(tupla_limpia)
            
    return datos_limpios_2



def total_kms(datos):

    km_totales = 0
    
    for clave, valor in datos:
        km_totales += valor
    
    return km_totales


def deporte_mas_km(datos):

    mas_km = 0
    deporte = ""
    acumulador = {}
    
    for clave, valor in datos:
        if clave not in acumulador:
            acumulador[clave] = 0
        acumulador[clave] += valor
        
    for n in acumulador: 
        if acumulador[n] > mas_km:
            mas_km = acumulador[n]
            deporte = n
    
    
    
    
    if mas_km == 0:
        deporte = "None"
    
    return deporte


def media_total(kms,datos):

    media = 0
   
    if kms == 0:
       return 0
    else:
         media = kms / len(datos)
        

    return media

