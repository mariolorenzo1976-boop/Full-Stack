import os
carpeta="/Users/emfashiondesign/Desktop/Primerospasospython/Imagenes"
archivos=os.listdir(carpeta)
for i, nombre in enumerate(archivos, start=1):
    ruta_vieja = os.path.join(carpeta,nombre)
    if os.path.isfile(ruta_vieja):
        extension= os.path.splitext(nombre)[1]
        nuevo_nombre=f"entreno_{i}{extension}"
        ruta_nueva=os.path.join(carpeta,nuevo_nombre)
        os.rename(ruta_vieja, ruta_nueva)
        print(f"{nombre} <> {nuevo_nombre}")
    else:
        print(f"{nombre} es una carpeta, se ignora")