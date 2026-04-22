
def analiza_datos(personas):

    suma_edades = 0
    media_edad = 0
    mayor = {"nombre":"", "edad":-1}
    menor = {"nombre":"", "edad":float('inf')}
    for n in personas:
        suma_edades += n['edad']
    
        if n['edad'] > mayor['edad']:
            mayor = n

        if n['edad'] < menor['edad']:
            menor = n

    media_edad = suma_edades / len(personas)    
    
    return({
             "media_edad": media_edad, 
             "mayor":mayor, 
             "menor":menor
            })
    


def imprime_datos(datos):

    print("Media de la edad:", datos['media_edad'])
    print("La persona mayor es:", datos['mayor']['nombre'], datos['mayor']['edad'])
    print("la persona menor es:", datos['menor']['nombre'], datos['menor']['edad'])



def main():
    personas = [{"nombre": "Mario", "edad": 49},
            {"nombre": "Ana", "edad": 32},
            {"nombre": "Luis", "edad": 41},
            {"nombre": "Marta", "edad": 28},
            {"nombre": "Javier", "edad": 55},
            ]

    datos = analiza_datos(personas)
    
    
    imprime_datos(datos)



main()