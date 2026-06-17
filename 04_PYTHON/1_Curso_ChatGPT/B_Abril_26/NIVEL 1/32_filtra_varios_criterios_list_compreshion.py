# filtra los nombres de las rutas con desnivel mayor a 800

rutas = [{"nombre": "Teide", "km": 45, "desnivel": 1200},
         {"nombre": "Anaga", "km": 30, "desnivel": 900},
         {"nombre": "Costa", "km": 25, "desnivel": 200} 
          ]


mas_desnivel = [n["nombre"] for n in rutas if n["desnivel"]>800]

print(mas_desnivel)