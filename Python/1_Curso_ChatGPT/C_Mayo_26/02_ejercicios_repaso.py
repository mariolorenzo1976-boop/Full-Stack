# 1 extrae solo los tiempos de bici
datos = [{"deporte": "bici", "tiempo": 120},
         {"deporte": "run", "tiempo": 45},
         {"deporte": "swim", "tiempo": 60},
         {"deporte": "bici", "tiempo": 90},]

tiempos_bic = [x['tiempo'] for x in datos if x['deporte']== "bici"]

print(tiempos_bic)


# 2 suma ambas listas y suma 10 a cada valor
bici = [100, 120, 90]
run = [30, 45]

resultado = [x + 10  for x in run] + [x + 10 for x in bici]
print(resultado)

# 3 Ordena por tiempo según valor
datos= [("bici", 120), ("run", 45), ("swim", 60), ("bici", 90)]

resultado = sorted(datos, key=lambda x: x[1])
print(resultado)

# 4 Encuentra el deporte con mayor tiempo
datos= [("bici", 120), ("run", 45), ("swim", 60), ("bici", 90)]

nombre = ""
mayor = 0
for x in datos:
    if x[1] > mayor:
        mayor = x[1]
        nombre = x[0]

print(nombre, mayor)

# # 5 Suma tiempos por deporte
# datos= [("bici", 120), ("run", 45), ("swim", 60), ("bici", 90)]

# lista = {}
# for x in datos:
#     if x not in lista:
#        lista [] = x[0]
#     if x in lista:
#         lista[1] += x[1]

# print(lista)        

    

# 6 quédate con los >50 y ordenalos de mayor a menor

datos = [120, 45, 60, 90, 30]

resultado = [x for x in datos if x > 50]

ordenado = sorted(resultado, key=lambda x: -x)

print(ordenado)


# saca listas de tiempos >50
datos = [{"nombre": "Mario", "deporte": "bici", "tiempo": 120},
         {"nombre": "Mario", "deporte": "run", "tiempo": 40},
         {"nombre": "Mario", "deporte": "swim", "tiempo": 60}]

resultado = [x['tiempo'] for x in datos if x['tiempo']>50]
print(resultado)