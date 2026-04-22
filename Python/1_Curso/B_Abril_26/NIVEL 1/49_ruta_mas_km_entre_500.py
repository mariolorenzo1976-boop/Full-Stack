# filtra rutas con más de 25 km
# ordénalas por desnivel (mayor a menor)
# formato nombre (km - desnivel)
ruta =[{"nombre": "Teide", "km": 45, "desnivel":1200},
       {"nombre": "Anaga", "km": 30, "desnivel":900},
       {"nombre": "Costa", "km": 25, "desnivel":200},
       {"nombre": "Norte", "km": 50, "desnivel":1500},
       {"nombre": "Sur", "km": 20, "desnivel":300},]

# usamos un bucle normal
mayor_500 = []

for n in ruta:
    if n['desnivel'] > 500:
        mayor_500.append(n)

mas_km = max(mayor_500, key=lambda x: x['km'])
formato_mas_km = f"{mas_km['nombre']} ({mas_km['km']})"
print(formato_mas_km)


# usamos un listh compreshion

mayor_500_lista = [n for n in ruta if n['desnivel']>500]
mas_km_lista = max(mayor_500_lista, key=lambda x: x['km'])
formato_mas_km_lista = f"{mas_km_lista['nombre']} ({mas_km_lista['km']})"
print(formato_mas_km_lista)