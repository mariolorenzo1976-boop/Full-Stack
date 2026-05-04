personas = [{"nombre": "Mario", "edad": 49},
            {"nombre": "Ana", "edad": 32},
            {"nombre": "Luis", "edad": 41},
            {"nombre": "Marta", "edad": 28}
            ]

mayor_40 =[]


# utilizando un bucle
for n in personas:
    if n['edad']>40:
        mayor_40.append(n['nombre'])

print(mayor_40)

# utilizando list compreshion
mayor_40 =[f"{n['nombre']}" for n in personas if n['edad']>40]

print(mayor_40)



