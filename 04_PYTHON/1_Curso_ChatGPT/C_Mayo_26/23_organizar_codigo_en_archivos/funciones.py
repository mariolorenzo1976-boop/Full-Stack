
#función de filtrado de datos con un límite

def filtrar (datos, limite):
    
    resultado = []
    for n in datos:
        if n > limite:
            resultado.append(n)

    return resultado


def suma_clave (datos_deporte, deporte):

    deporte_agrupado = {}
    for clave, valor in datos_deporte:
        if clave == deporte:
            if clave not in deporte_agrupado:
                 deporte_agrupado[clave] = 0
            deporte_agrupado[clave] += valor

    return deporte_agrupado
    