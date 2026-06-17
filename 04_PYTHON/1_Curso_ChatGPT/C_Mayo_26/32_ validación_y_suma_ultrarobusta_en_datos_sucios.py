
# Ejercicio 32 - suma robusta de todos los km con datos ultra-sucios

datos = [
    ("bici", 100),
    ("run", None),
    ("swim", "hola"),
    999,
    ("bike", 50)
]

def suma_ultrarobusta (datos):

    suma_km = 0
    nueva_lista = []
   
    if not datos:
        return 0
    else:
        for n in datos:
            if isinstance(n, (tuple)) and len(n) == 2:
                nueva_lista.append(n)
             
       
        
        for clave, valor in nueva_lista:
            if isinstance(valor, (int, float)):
                suma_km += valor
        
        return suma_km        
        
         
print(suma_ultrarobusta(datos))