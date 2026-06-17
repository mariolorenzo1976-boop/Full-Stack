# imprime solo los mayores de 30
def mayor_30(datos):
    resultado = []
    
    for clave, valor in datos:
        if valor > 30:
            resultado.append((clave, valor))
        
    return resultado




datos = [("bici", 100), ("run", 20), ("bici", 50), ("swim", 80),]

print(mayor_30(datos))


