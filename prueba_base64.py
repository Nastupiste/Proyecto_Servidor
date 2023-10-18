import requests
import json
import base64

# Solicitar el JSON a través de una URL (reemplaza la URL con la que desees utilizar)
url = "https://opentdb.com/api.php?amount=15+&category=9"
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Decodificar la respuesta JSON
    json_data = response.json()

    # Convertir el JSON a una cadena en formato UTF-8
    json_str = json.dumps(json_data, ensure_ascii=False).encode('utf-8')

    # Codificar la cadena en Base64
    json_base64 = base64.b64encode(json_str)

    # Imprimir el JSON en formato Base64
    print("JSON en formato Base64:", json_base64.decode('utf-8'))
else:
    print("Error al obtener el JSON. Código de estado:", response.status_code)
