# filtra rutas con los siguientes criterios:
# .tengan más de 30 km
# .y más de 800 m desnivel
# formato salida: "nombre(km km/desnivel m)"

ruta = [{"nombre": "Teide", "km": 45, "desnivel": 1200},
        {"nombre": "Anaga", "km": 30, "desnivel": 900},
        {"nombre": "Costa", "km": 25, "desnivel": 200}
        ]

ruta_km_desnivel = [f"{n['nombre']} ( {n['km']}km / {n['desnivel']}m )"     
                    for n in ruta      
                    if n["km"]>30 and n["desnivel"]>800]

print(ruta_km_desnivel)