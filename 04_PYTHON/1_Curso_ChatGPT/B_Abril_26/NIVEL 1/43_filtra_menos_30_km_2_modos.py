#devuelve los nombres de rutas con menos de 30 km

ruta =[{"nombre": "Teide", "km": 45, "desnivel":1200},
       {"nombre": "Anaga", "km": 30, "desnivel":900},
       {"nombre": "Costa", "km": 25, "desnivel":200},
       {"nombre": "Norte", "km": 50, "desnivel":1500},
       {"nombre": "Sur", "km": 20, "desnivel":300},]

#usamos list compreshion
menos_30 = [n['nombre'] for n in ruta if n['km']<30]

print(menos_30)

#usamos bucle normal

menor_25=[]
for n in ruta:
    if n['km'] < 30:
        menor_25.append(n['nombre'])

print(menor_25)





