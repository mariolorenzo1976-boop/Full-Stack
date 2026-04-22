lista=[1,2,-3,-5]

prov=0
for a in range(len(lista)):
    for i in range(len(lista)-1):
        if lista[i]>lista[i + 1]:
            prov=lista[i + 1]
            lista[i + 1]=lista[i]
            lista[i]=prov


print(lista)


# Nivel Pro

# lista = [1, 2, -3, -5]

# for a in range(len(lista)):
#     intercambio = False # si de la primera pasada ya esta ordenada se para el programa

#     for i in range(len(lista) - a - 1): # -a es para que no compare cosas que ya están bien.
#         if lista[i] > lista[i + 1]:
#             lista[i], lista[i + 1] = lista[i + 1], lista[i] # cambio las posiciones directamente si falta de variables como en C
#             intercambio = True

#     if not intercambio:
#         break

# print(lista)


