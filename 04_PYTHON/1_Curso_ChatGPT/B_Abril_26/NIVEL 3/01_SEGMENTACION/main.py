
from datos import entrenamientos
from funsiones import *

def main():


    
    
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