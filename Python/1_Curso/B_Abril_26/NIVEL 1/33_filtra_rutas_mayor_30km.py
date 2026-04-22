# filtra rutas con más de 30km con formato : "Teide - 45km"

ruta = [{"nombre": "Teide", "km": 45, "desnivel": 1200},
        {"nombre": "Anaga", "km": 30, "desnivel": 900},
        {"nombre": "Costa", "km": 25, "desnivel": 200}
        ]

                   #cadena de texto.           recorro lista        condicional
         #------------------------------      --------------      ----------------
mas_30 = [f"{n['nombre']} - {n['km']}km"      for n in ruta       if n['km'] > 30]
print(mas_30)

