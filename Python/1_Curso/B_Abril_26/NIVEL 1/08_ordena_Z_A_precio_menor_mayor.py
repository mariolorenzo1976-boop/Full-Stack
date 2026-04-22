# ordena los productos de Z_A y precio de menor a mayor
productos = [("bici", 1200),
             ("casco", 80),
             ("ruedas", 300),
             ("guantes", 80)]


productos.sort(key=lambda x: x[1])
productos.sort(key=lambda x: x[0], reverse=True)

print(productos)