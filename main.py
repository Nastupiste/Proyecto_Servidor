# Para manipular JSON.
import json
# Para acceder a una url.
import requests
# Para generar un número aleatorio
import random

# Generamos una categoría random para el url.

def generaCategoria():
    categoria=int(random.randint(9,30))
    return categoria

# Hacemos la solicitud de los datos a la url.

def llamadaApi(numPreguntas,categoria):
    API_url=f"https://opentdb.com/api.php?amount={numPreguntas}+&category={categoria}"
    respuesta=requests.get(API_url)

# Convertimos el resultado de llamada a la API "JSON" a una estructura de datos manejable

    datos=json.loads(respuesta.content)

# La URL podría devolvernos un JSON, de momento lo voy a controlar con un while.
    while datos["response_code"] == 1:
        categoria = int(random.randint(9, 30))
        API_url = f"https://opentdb.com/api.php?amount={numPreguntas}&category={categoria}"
        respuesta = requests.get(API_url)
        datos = json.loads(respuesta.content)
        print(type(datos))
    return datos

def calculaResultado(aciertos,errores,numPreguntas):    
    cadenaResultado=""
    porcentaje_Acierto = (aciertos/numPreguntas) * 100
    if porcentaje_Acierto>=50:
        cadenaResultado+="Well done! You have passed the quiz!\n"
    else:
        cadenaResultado+="You lose... Don't worry, you'll get them next time!\n"

    cadenaResultado+=(f"You had {aciertos} correct answers.\n")
    cadenaResultado+=(f"You had {errores} incorrect answers.\n")
    cadenaResultado+=(f"Your final score is {porcentaje_Acierto}\n")
    return cadenaResultado