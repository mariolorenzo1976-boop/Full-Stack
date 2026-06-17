# ordena longitud del nombre más corto primero y si empatan precio menor a mayor
productos = [("bici", 1200),
             ("casco", 80),
             ("ruedas", 300),
             ("guantes", 80),
             ("zapatillas", 120)]

ordena = sorted(productos, key=lambda x: (len(x[0]), x[1]))

print(ordena) 