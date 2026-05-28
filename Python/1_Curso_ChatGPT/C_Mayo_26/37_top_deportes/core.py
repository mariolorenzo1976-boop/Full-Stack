# limpiando datos
def limpia_datos(datos):
    
    lista_limpia = []
    if not datos:
        return[]
    
    
    for n in datos:
        if  isinstance(n, dict) and "user" in n and "sport" in n and "km" in n and len(n) == 3 and isinstance(n["user"], str) \
            and isinstance(n["sport"], str) and isinstance(n["km"], int):
            lista_limpia.append(n) 

    return lista_limpia      


# agrupando usuarios por kms
def km_por_usuario(datos):

    km_usuario_agrupado = {}
    km_usuario_agrupado2 =[]
   
    for n in datos:
        
        usuario = n ["user"]
        km = n["km"]
       
        if usuario not in km_usuario_agrupado:
            km_usuario_agrupado[usuario] = 0
        km_usuario_agrupado[usuario] += km
   
    for clave, valor in km_usuario_agrupado.items():
        km_usuario_agrupado2.append({"user": clave, "km": valor})
       
    return km_usuario_agrupado2      


# detectando que usuario tiene más km
def usuario_mas_km(datos):

    mas_km = 0
    usuario = ""

    for n in datos:
        if n["km"] > mas_km:
            mas_km = n["km"]
            usuario = {"user": n["user"], "km": n["km"]}

    return usuario


# agrupando kms por deporte
def km_por_deporte(datos):

    deporte_por_km_2 = {}
    deportes_por_km = []

    for n in datos:
       km = n["km"]
       deporte = n["sport"]
      
       if deporte not in deporte_por_km_2:
           deporte_por_km_2[deporte] = 0
       deporte_por_km_2[deporte] += km 

    for clave, valor in deporte_por_km_2.items():
        deportes_por_km.append({"sport":clave, "km": valor})

    return deportes_por_km

