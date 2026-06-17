# ordena por precio descendente y nombre ascendente
productos = [("teclado",50), ("raton",20),("monitor",150),("altavoces",50)]

productos.sort (key=lambda x: -x[1])
productos.sort (key=lambda x: x[0])

print(productos)

