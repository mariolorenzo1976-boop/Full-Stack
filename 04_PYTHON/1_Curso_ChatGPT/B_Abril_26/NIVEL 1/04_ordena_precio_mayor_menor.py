# ordena los productos por precio de mayor a menor
productos = [("bici", 1200),
             ("casco", 80),
             ("ruedas", 300)]

ordena = sorted(productos, key=lambda x: -x[1])
print(ordena)