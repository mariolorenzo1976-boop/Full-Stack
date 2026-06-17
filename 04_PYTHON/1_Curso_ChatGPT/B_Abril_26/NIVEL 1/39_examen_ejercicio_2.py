#saca una lista con los nombres de rutas con más de 25 km
#formato: nombre (km)

rutas =[{"nombre": "Teide", "km":45, "desnivel": 1200},
        {"nombre": "Anaga", "km":30, "desnivel": 900},
        {"nombre": "Costa", "km":25, "desnivel": 200},
        {"nombre": "Norte", "km":50, "desnivel": 1500}
        ]

mas_25 = [f"{n['nombre']} ({n['km']}km)" for n in rutas if n['km']>25]
print(mas_25)