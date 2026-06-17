estructura = [{"a":1}, {"b":2}, {"c":3}]

# acceso a los valores de la lista
for n in estructura:
    for valor in n.values():
        print(valor)

# creamos una lista de valores
lista = []
for n in estructura:
    for valor in n.values():
        lista.append(valor)

print(lista)
