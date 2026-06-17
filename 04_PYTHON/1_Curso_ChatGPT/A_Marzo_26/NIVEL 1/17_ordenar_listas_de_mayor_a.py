

# ordenar productos de mayor a menor

productos=[("bici",1200),("casco",80),("ruedas",300),]
productos_ordenados=sorted(productos, key=lambda x: x[1], reverse=True)

print(productos_ordenados)
