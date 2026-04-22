personas = [{"nombre": "Mario", "edad": 49},
            {"nombre": "Ana", "edad": 32},
            {"nombre": "Luis", "edad": 41},
            ]

def persona_mayor_menor(personas):

    edad_mayor = -1
    edad_menor = float('inf')
    nombre_mayor = ""
    nombre_menor = ""
    
    for n in personas:
        if n['edad'] > edad_mayor:
            edad_mayor = n['edad']
            nombre_mayor = n['nombre']
        
        if n['edad']< edad_menor:
            edad_menor = n['edad']
            nombre_menor = n['nombre']
        
    return nombre_menor, edad_menor , nombre_mayor, edad_mayor
     

nombre_menor, edad_menor, nombre_mayor, edad_mayor = persona_mayor_menor(personas)

print(f"Persona mayor: {nombre_mayor} con edad {edad_mayor}")
print(f"Persona menor: {nombre_menor} con edad {edad_menor}")

