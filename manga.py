import requests
from bs4 import BeautifulSoup
import os

# URL base del manga
url_base = "https://s1.3hentai.net/d1044412/"
# Número total de páginas del manga
total_paginas = 6

# Carpeta donde se guardarán las imágenes
carpeta_destino = "manga_descargado"
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Función para descargar una imagen
def descargar_imagen(url, ruta_destino):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open(ruta_destino, 'wb') as archivo:
            archivo.write(respuesta.content)

# Descarga todas las imágenes
for i in range(1, total_paginas + 1):
    url_imagen = f"{url_base}{i}.jpg"
    ruta_destino = os.path.join(carpeta_destino, f"pagina_{i}.jpg")
    print(f"Descargando {url_imagen}...")
    descargar_imagen(url_imagen, ruta_destino)

print("Descarga completada.")
