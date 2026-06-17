# filtramos la siguiente lista por edad y luego por list compreshion

#metodo bucle normal
# edades = [12, 18, 25, 15, 40]

# mayor_igual_18 = []

# for n in edades:
#     if n >= 18:
#         mayor_igual_18.append(n)

# print(mayor_igual_18)

#metodo listh compreshion

edades = [12, 18, 25, 15, 40]

mayor_igual_18 = [n for n in edades if n>=18]

print(mayor_igual_18)
