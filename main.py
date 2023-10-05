# Para manipular JSON.
import json
# Para acceder a una url.
import requests

# Hacemos la solicitud de los datos a la url.
respuesta=requests.get("https://www.bne.es/sites/default/files/redBNE/datosgob/awe/tema/videojuegos.json")
datos=respuesta.json()

# Si quisiera imprimir los datos obtenidos en formato json:
# print(json.dumps(datos, indent=4, sort_keys=True))
