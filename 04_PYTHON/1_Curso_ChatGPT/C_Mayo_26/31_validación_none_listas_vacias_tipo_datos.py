# ejercicio 31 validamos con entrada None, lista vacia, y con errores de datos. 

datos = None
datos_1 = []
datos_2 = [("bici",100), ("run", "hola"), ("swim",50)]

def suma_robusta(datos):

    suma_km = 0
    
    if len(datos) == 0 or datos is None:  # o mejor - if not datos:
        return 0
    else:
        for clave, valor in datos:
            if isinstance(valor, (int, float)) == True: # o mejor - if isinstance(valor, (int, float)):
                suma_km += valor
            
        return suma_km
    
print(suma_robusta(datos=None))
print(suma_robusta(datos_1))
print(suma_robusta(datos_2))

