def total_km(entrenamiento):
    
    suma_km = 0
    for n in entrenamiento:
        suma_km +=  n['distancia']

    return suma_km


def total_tiempo(entrenamiento):

    tiempo = 0
    for n in entrenamiento:
        tiempo += n['tiempo']

    return tiempo


def tipo_entreno(entrenamiento):

    tipos_entreno = []
    for n in entrenamiento:
        if n['tipo'] not in tipos_entreno:
            tipos_entreno.append(n['tipo'])

    return tipos_entreno


# Aquí contamos dentro de la lista entrenamientos cuanta cantidad de entrenamientos se repiten, y lo
# guardamos en un diccionario llamado contador. Guardamos solo los datos. el tipo de entrenamiento y 
# luego las veces que se repiten ej: {'bici': 3, 'running': 2, 'pesas': 1, 'natación': 1} frente a como
# estaban en la lista entrenamiento: {"tipo":"bici", "tiempo": 120, "distancia": 40}

def entreno_frencuente(entrenamientos):

    contador = {}
   
    for n in entrenamientos:
        entreno = n['tipo']
        if entreno in contador:
            contador[entreno] += 1
        else:
            contador[entreno] = 1
        
   
    return contador
   

# aquí desempaquetamos con un for, añadiendole nombres a los diferentes datos del diccionario, 
# pero en formato variable, ya que el diccionario solo trae los datos en crudo. Esto no modifica el
# diccionario. Todo esto lo hacemos con este for: --- for tipo, valor in entreno_fre.items():  --

def mas_frecuentado(entreno_fre):
    max_tipo = None
    conteo_tipo = 0

    for tipo, valor in entreno_fre.items():
        if valor > conteo_tipo:
            max_tipo = tipo
            conteo_tipo = valor

    return(max_tipo, conteo_tipo)
            

def main():

    entrenamientos= [{"tipo":"bici", "tiempo": 120, "distancia": 40},
                     {"tipo":"running", "tiempo": 45, "distancia": 8},
                     {"tipo":"bici", "tiempo": 90, "distancia": 30},
                     {"tipo":"pesas", "tiempo": 60, "distancia": 0},
                     {"tipo":"natación", "tiempo": 180, "distancia": 5},
                     {"tipo":"bici", "tiempo": 150, "distancia": 50},
                     {"tipo":"running", "tiempo": 30, "distancia": 5}
                 

                     ]
    
    
    suma_km = total_km(entrenamientos)
    tiempo = total_tiempo(entrenamientos)
    tipos_entreno = tipo_entreno(entrenamientos)
    entreno_fre = entreno_frencuente(entrenamientos)
    sport_frecuente = mas_frecuentado(entreno_fre)

    

    print(f"La suma de km entre todas las actividades a sido de: {suma_km} km")
    print(f"El tiempo de todas las actividades suman: {tiempo} minutos")
    print(f"Has realizado, {len(tipos_entreno)} tipos de entreno diferentes")
    print(f"La frecuencias de los entrenos han sido {entreno_fre}")
    # entreno_mas = max(entreno_fre, key=entreno_fre.get) 
    # print(f"El deporte más entrenado es: {entreno_mas}")
    print(f"El deporte más frecuentado es: {sport_frecuente}")

if __name__ == "__main__":
    main()