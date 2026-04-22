# ordena los productos por nombre A-Z
productos = [("bici", 1200),
             ("casco", 80),
             ("ruedas", 300),
             ("guantes", 80)]

ordena = sorted(productos, key=lambda x: x[0])
print(ordena)