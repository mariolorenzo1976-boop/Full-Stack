#saca una lista con los nombres de rutas con más de 30 km

rutas =[{"nombre": "Teide", "km":45, "desnivel": 1200},
        {"nombre": "Anaga", "km":30, "desnivel": 900},
        {"nombre": "Costa", "km":25, "desnivel": 200},
        {"nombre": "Norte", "km":50, "desnivel": 1500}
        ]

mas_30 = [f"{n['nombre']:}" for n in rutas if n["km"]>30]
print(mas_30)
