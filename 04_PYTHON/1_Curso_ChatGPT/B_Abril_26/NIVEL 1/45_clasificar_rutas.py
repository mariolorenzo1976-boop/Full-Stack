# clasificación de ruta segun su dureza - formato nombre:tipo
ruta =[{"nombre": "Teide", "km": 45, "desnivel":1200},
       {"nombre": "Anaga", "km": 30, "desnivel":900},
       {"nombre": "Costa", "km": 25, "desnivel":200},
       {"nombre": "Norte", "km": 50, "desnivel":1500},
       {"nombre": "Sur", "km": 20, "desnivel":300},]


# lo hacemos con un bucle normal

resultado = []

for n in ruta:
    if n["desnivel"] > 1000:
        tipo = "Muy dura"
    elif n["desnivel"] > 500:
        tipo = "Media"
    else:
        tipo = "Baja"

    resultado.append(f"{n['nombre']}: {tipo}")

print(resultado)



# lo hacemos con list compreshion

clasificacion =[f"{n['nombre']}: Muy dura" if n['desnivel']>1000 else 
                 f"{n['nombre']}: media dureza" if n['desnivel']>500 else
                 f"{n['nombre']}: baja dureza" for n in ruta]
print(clasificacion)