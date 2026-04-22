# devuelve rutas con más de 20 km, ordenadas por km de menor a mayor
ruta =[{"nombre": "Teide", "km": 45, "desnivel":1200},
       {"nombre": "Anaga", "km": 30, "desnivel":900},
       {"nombre": "Costa", "km": 25, "desnivel":200},
       {"nombre": "Norte", "km": 50, "desnivel":1500},
       {"nombre": "Sur", "km": 20, "desnivel":300},]

# realizamos por bucle normarl
mayor_20 = []

for n in ruta:
    if n['km']>20:
        mayor_20.append(n)

ordenar = sorted(mayor_20,key=lambda x: x['km'])
transformar = [f"{n['nombre']} ({n['km']} km)" for n in ordenar]
print(transformar)


# realizamos por list compreshion

filtradas = [n for n in ruta if n["km"] > 20]
ordenadas = sorted(filtradas, key=lambda x: x["km"])
resultado = [f"{n['nombre']} ({n['km']}km)" for n in ordenadas]

print(resultado)



