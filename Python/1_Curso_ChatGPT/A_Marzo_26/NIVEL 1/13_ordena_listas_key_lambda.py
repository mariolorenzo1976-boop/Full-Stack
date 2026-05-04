

# Ordena la lista productos por key con la funsión X donde 1 es el precio

productos=[("bici",1200),("casco",80),("ruedas",300),]

ordenado=sorted(productos, key=lambda x: x[1]) # Ordena la lista productos por key con la funsión X donde 1 es el precio
print(ordenado)
