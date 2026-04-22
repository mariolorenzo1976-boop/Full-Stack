# ordena los productos por precio de mayor a menor, si empate de A_Z
productos = [("bici", 1200),
             ("casco", 80),
             ("ruedas", 300),
             ("guantes", 80)]

ordena = sorted(productos, key=lambda x: (-x[1], x[0]))
print(ordena)