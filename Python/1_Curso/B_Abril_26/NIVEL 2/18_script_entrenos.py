
def total_km(entrenamientos):

    total_km = 0
    for n in entrenamientos:
        total_km += n['distancia']

    return total_km    


def total_tiempo(entrenamientos):

    tiempo_entreno = 0
    for n in entrenamientos:
        tiempo_entreno += n['tiempo']

    return tiempo_entreno

def tipo_entreno(entrenamientos):

    tipo = entrenamientos[0]['tipo']
    tipos = []
    for n in entrenamientos:
        if n['tipo'] not in tipos:
           tipos.append(n['tipo'])
                
    return len(tipos)


def main():
    entrenamientos = [{"tipo": "bici", "tiempo": 120, "distancia":40},
                  {"tipo": "running", "tiempo": 45, "distancia":8},
                  {"tipo": "bici", "tiempo": 90, "distancia":30},
                  {"tipo": "pesas", "tiempo": 60, "distancia":0},
                  {"tipo": "natación", "tiempo": 180, "distancia":5},
                  ]
    
    km_totales = total_km(entrenamientos)
    tiempo_total = total_tiempo(entrenamientos)
    entreno = tipo_entreno(entrenamientos)

    print(f"El total de km ha sido de: {km_totales}")
    print(f"El total de tiempo ha sido de: {tiempo_total}")
    print(f"El total de tipos diferentes de entrenamiento son de: {entreno}")





main()

