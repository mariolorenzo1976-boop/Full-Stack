personas = [{"nombre": "Mario", "edad": 49},
            {"nombre": "Ana", "edad": 32},
            {"nombre": "Luis", "edad": 41},
            ]


def media(personas):

    suma_edad = 0
    n_personas = 0
    media_personas = 0
    for n in personas:
        suma_edad += n['edad']
        n_personas +=1
    
    media_personas = suma_edad / n_personas
    return media_personas

print("La edad media es:", media(personas))