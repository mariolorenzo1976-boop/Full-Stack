
rutas =[{"nombre": "Teide", "km":45, "desnivel": 1200},
        {"nombre": "Anaga", "km":30, "desnivel": 900},
        {"nombre": "Costa", "km":25, "desnivel": 200},
        {"nombre": "Norte", "km":50, "desnivel": 1500}
        ]

#filtra rutas con más de 25 km
mas_25 = [n for n in rutas if n['km']>25]

#ordenalas por desnivel (mayor a menor)
mayor_menor_desnivel=sorted(mas_25, key=lambda x: -x['desnivel'])

#Devuelve: formato nombre : desnivel
formato = [f"{n['nombre']}: {n['desnivel']}" for n in mayor_menor_desnivel]

print(formato)