
from core import *
from datos import *

def estadistica():
    
    datos_limpios = limpia_datos(datos)
    kms_por_usuarios = km_por_usuario(datos_limpios)
    usuario_con_mas_km = usuario_mas_km(kms_por_usuarios)
    kms_por_deporte = km_por_deporte(datos_limpios)
    
          
    return {
            "usuarios": kms_por_usuarios,
            "top-usuario": usuario_con_mas_km, 
            "deportes": kms_por_deporte
    }

    
    

  

   