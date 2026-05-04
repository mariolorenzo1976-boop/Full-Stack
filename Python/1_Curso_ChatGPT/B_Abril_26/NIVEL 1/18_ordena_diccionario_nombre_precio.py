# ordena sin usar reverse=True, por Nombre descendente y Precio ascendente
productos = [{"nombre": "teclado", "precio": 50, "stock": 10},
             {"nombre": "raton", "precio": 20, "stock": 50},
             {"nombre": "monitor", "precio": 150, "stock": 5},
             {"nombre": "altaboces", "precio": 60, "stock": 30}]

ordena=sorted(productos,key=lambda x: (x["nombre"], -x["precio"]))
print(ordena)
