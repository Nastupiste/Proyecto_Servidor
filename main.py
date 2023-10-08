# Para manipular JSON.
import json

# Para acceder a una url.
import requests
# Para poder tener ventana.

import tkinter as tk
from tkinter import *


# Hacemos la solicitud de los datos a la url.

API_url="https://opentdb.com/api.php?amount=24&category=22"
respuesta=requests.get(API_url)

# Convertimos el resultado de llamada a la API "JSON" a una estructura de datos manejable
datos=json.loads(respuesta.text)
# Comprobamos que la variable datos es un diccionario.
#print(type(datos))

# Creamos variable para almacenar las preguntas que se encuentran en el diccionario.
preguntas=datos["results"]
# Comprobamos que la variable preguntas es una lista de diccionarios:
#print(type(preguntas))

# Ahora vamos a iterar sobre esa lista, para acceder a las preguntas y sus respuestas.
fallos=0
aciertos=0
# En la cada vuelta accedemos a una pregunta que contienen respuestas buenas y malas
for pregunta in preguntas:
    opciones=[]
    print(pregunta["question"])
    print("Options: ")
    # Este for añade las respuestas malas a una lista de opciones
    for numRespuesta in range(len(pregunta["incorrect_answers"])): 
       opciones.append(pregunta["incorrect_answers"][numRespuesta])
    # Añadimos la respuesta correcta
    opciones.append(pregunta["correct_answer"])
    
    # Las reordenamos para sea un poco más aleatório
    opciones.sort
    
    # imprimimos la respuesta por pantalla. ¡Hasta aquí genial! 
    contador=0
    for respuesta in range(len(opciones)):
        contador=contador+1
        print(f"{contador} {opciones[respuesta]}")

    # recogemos la respuesta del usuario ¿Como hago la comprobación?
    respuesta_Usuario=int(input("Enter the number of your answer: "))
    
    #if respuesta_Usuario==ni idea














# Creamos una nueva ventana:
# Convertimos a texto los datos:
#texto = json.dumps(datos, ensure_ascii= False, indent=2)
#ventana = tk.Tk()

# Añado un elemento scrollBar a la ventana:
#scrol_bar= tk.Scrollbar(ventana)
#scrol_bar.pack(side='right', fill='y')

# Para poder configurar el texto y formato de la ventana
#txt = tk.Text(ventana, font="Times32")
#txt.pack()
#txt.config(yscrollcommand=scrol_bar.set)
#scrol_bar.config(command=txt.yview)
#txt.insert('end', texto)

#ventana.mainloop()

# Si quisiera imprimir los datos obtenidos en formato json:
# print(json.dumps(datos, indent=4, sort_keys=True))*/
