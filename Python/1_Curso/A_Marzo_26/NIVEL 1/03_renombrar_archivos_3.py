import os
carpeta="/Users/emfashiondesign/Desktop/Primerospasospython/Imagenes"
archivos=os.listdir(carpeta)
print (f"{archivos} es la cantidad de archivos")
contador=1

for nombre in archivos:
    
    if nombre.startswith("."):
        continue

    ruta_vieja=os.path.join(carpeta, nombre)
    if os.path.isfile(ruta_vieja):
        extencion=os.path.splitext(nombre)[1]
        nuevo_nombre=f"zorro_{contador}{extencion}"
        ruta_nueva=os.path.join(carpeta, nuevo_nombre)
        os.rename (ruta_vieja, ruta_nueva)
        print(f"{nombre} <> {nuevo_nombre}")
        contador +=1
    else:
        print (f"{nombre} es carpeta, no cuenta")