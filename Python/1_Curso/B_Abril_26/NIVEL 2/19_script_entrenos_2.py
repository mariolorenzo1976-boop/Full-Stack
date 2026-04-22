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

def entreno_frencuente(tipos_entreno, entrenamientos):


    # print(tipo)
   
  
    nombre_cantidad_entreno = []
    contador = 0
    i=0

    for x in tipos_entreno:
        entreno = tipos_entreno[i]
        for n in entrenamientos:
            if n['tipo'] == entreno:
                contador += 1
           
                
        nombre_cantidad_entreno.append({'tipo':entreno, 'veces':contador})    
        contador = 0
        i += 1
        
  

   

    return nombre_cantidad_entreno
   



def main():

    entrenamientos= [{"tipo":"bici", "tiempo": 120, "distancia": 4},
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
    entreno_fre = entreno_frencuente(tipos_entreno,entrenamientos)

    formatear_entreno_frecuent = [f"{n['tipo']} {n['veces']} veces" for n in entreno_fre]

    print(f"La suma de km entre todas las actividades a sido de: {suma_km} km")
    print(f"El tiempo de todas las actividades suman: {tiempo} minutos")
    print(f"Has realizado, {len(tipos_entreno)} tipos de entreno diferentes")
    print(f"La frecuencias de los entrenos han sido {formatear_entreno_frecuent}")

main()