productos = [{"nombre": "bici", "precio": 1200, "stock":0},
             {"nombre": "casco", "precio": 80, "stock":20},
             {"nombre": "ruedas", "precio": 300, "stock":0},
             {"nombre": "guantes", "precio": 80, "stock":50},]

productos_filtrados = []
for p in productos:
    if p["stock"]>0:
        productos_filtrados.append(p)

productos=productos_filtrados
print(productos_filtrados)
