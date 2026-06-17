ruta =[{"nombre": "Teide", "km": 45, "desnivel":1200},
       {"nombre": "Anaga", "km": 30, "desnivel":900},
       {"nombre": "Costa", "km": 25, "desnivel":200},
       {"nombre": "Norte", "km": 50, "desnivel":1500},
       {"nombre": "Sur", "km": 20, "desnivel":300},]

#rutas con más de 25 km usando un bucle normal

mayor_25 = []  #creamos una lista nueva donde meteremos los datos

for n in ruta: #recorremos la lista ruta para buscar la información solicitada
    if n['km'] >25:  #si n que es el apuntador dentro de ruta vale 0 porque apunta al primer registro y donde km vale x, es mayor a 25 entonces guarda la información en le nueva lista 
        mayor_25.append(f"{n['nombre']} - {n['km']}km") # guarda el diccionario al que esta apuntando con la variable n en la nueva lista

print(mayor_25)




#rutas con mas de 25 km usando list compreshion automaticamente

mayor_25_lista = [f"{n['nombre']} - {n['km']} km" for n in ruta if n['km']>25]

print(mayor_25_lista)