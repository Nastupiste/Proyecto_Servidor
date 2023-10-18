import requests
import json
import random
import html

API_url=f"https://opentdb.com/api.php?amount=20+&category=9"
respuesta=requests.get(API_url)
print(respuesta)
# Convertimos el resultado de llamada a la API "JSON" a una estructura de datos manejable



datos=json.loads(respuesta.content)

# La URL podría devolvernos un JSON, de momento lo voy a controlar con un while.

print(type(datos))
print(datos)




# String con caracteres HTML entities
texto_con_entidades = "Este es un ejemplo con &lt;b&gt;HTML entities&lt;/b&gt;."

# Utiliza html.unescape para convertir las entidades HTML en caracteres legibles
texto_arreglado = html.unescape(texto_con_entidades)

# Imprime el texto arreglado
print(texto_arreglado)
