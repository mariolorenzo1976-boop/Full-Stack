# filtra rutas con más de 25 km
# ordénalas por desnivel (mayor a menor)
# formato nombre (km - desnivel)
ruta =[{"nombre": "Teide", "km": 45, "desnivel":1200},
       {"nombre": "Anaga", "km": 30, "desnivel":900},
       {"nombre": "Costa", "km": 25, "desnivel":200},
       {"nombre": "Norte", "km": 50, "desnivel":1500},
       {"nombre": "Sur", "km": 20, "desnivel":300},]


# utilizamos un bucle normal
mayor_25 = []
for n in ruta:
    if n['km'] >25:
        mayor_25.append(n)

ordenar_mayor_25 = sorted(mayor_25, key=lambda x: -x['desnivel'])

formato_mayor = [f"{n['nombre']} ({n['km']} - {n['desnivel']})" for n in ordenar_mayor_25]

print(formato_mayor)



# utilizamos list compreshion

mayor_25_ordenada = sorted(ruta, key=lambda x: -x['desnivel'])
mayor_25_lista = [f"{n['nombre']} ({n['km']} - {n['desnivel']})" for n in mayor_25_ordenada if n['km']>25]
print(mayor_25_lista)
