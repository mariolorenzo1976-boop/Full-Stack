#clasifica todas las rutas en dura, media o suave
#formato: nombre: dura

rutas =[{"nombre": "Teide", "km":45, "desnivel": 1200},
        {"nombre": "Anaga", "km":30, "desnivel": 900},
        {"nombre": "Costa", "km":25, "desnivel": 200},
        {"nombre": "Norte", "km":50, "desnivel": 1500}
        ]

clase_ruta =     [f"{n['nombre']}: dura" if n['desnivel']>1000
            else f"{n['nombre']}: media" if n['desnivel']>=500
            else f"{n['nombre']}: suave"
            for n in rutas]

print(clase_ruta)