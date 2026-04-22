# modo tradicional (menos usado)

# lista = [1, 2, 3, 4, 5, 6]
# pares = []
# for n in lista:
#     if n %2 == 0:
#         pares.append(n)

# print(pares)



# por medio de list compreshion (forma moderna)

lista =[1, 2, 3, 4, 5, 6]
pares = [ n for n in lista if n %2 == 0]

print(pares)
