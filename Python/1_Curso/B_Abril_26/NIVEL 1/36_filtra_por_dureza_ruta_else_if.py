# filtra rutas con los siguientes criterios:
# ."Teide: dura" si desnivel>1000
# ."Anaga: media" si entre 500 y 1000
# ."Costa: suave" si menos de 500


ruta = [{"nombre": "Teide", "km": 45, "desnivel": 1200},
        {"nombre": "Anaga", "km": 30, "desnivel": 900},
        {"nombre": "Costa", "km": 25, "desnivel": 200}
        ]


dureza = [f"{n['nombre']}: dura" #expresión 
          if n['desnivel']>1000 #expresión 
          else f"{n['nombre']}: media" if n['desnivel']>=500 #expresión 
          else f"{n['nombre']}: suave" #expresión  
          for n in ruta ] #recorrido lista


print(dureza)