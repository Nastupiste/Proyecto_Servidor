# Para manipular JSON.
import json
# Para acceder a una url.
import requests
# Para generar un número aleatorio
import random
# Para poder tener ventana.
import tkinter as tk
from tkinter import *

# Interacción con el usuario
print("Welcome to the Trivia´s API quest!")     
numPreguntas=int(input("How many questions do yo want to answer?\n(from 1 to 50):"))
while numPreguntas<1 or numPreguntas>50:
    numPreguntas=int(input("How many questions do yo want to answer?\n(from 1 to 50):"))

# Hacemos la solicitud de los datos a la url.
categoria=int(random.randint(9,30))

API_url=f"https://opentdb.com/api.php?amount={numPreguntas}+&category={categoria}"
respuesta=requests.get(API_url)

# Convertimos el resultado de llamada a la API "JSON" a una estructura de datos manejable
datos=json.loads(respuesta.text)

# La URL podría devolvernos un JSON, de momento lo voy a controlar con un while.
while datos["response_code"] == 1:
    categoria = int(random.randint(9, 30))
    API_url = f"https://opentdb.com/api.php?amount={numPreguntas}&category={categoria}"
    respuesta = requests.get(API_url)
    datos = json.loads(respuesta.text)

# Creamos variable para almacenar las preguntas que se encuentran en el diccionario.
preguntas=datos["results"]
# Comprobamos que la variable preguntas es una lista de diccionarios:
#print(type(preguntas))

# Ahora vamos a iterar sobre esa lista, para acceder a las preguntas y sus respuestas.
fallos=0
aciertos=0
# En la cada vuelta accedemos a una pregunta que contienen respuestas buenas y malas
print()
print("The category is "+preguntas[0]["category"])
for pregunta in preguntas:
    opciones=[]
    print()
    print(pregunta["question"])
    print("Options: ")
    # Este for añade las respuestas malas a una lista de opciones
    for numRespuesta in range(len(pregunta["incorrect_answers"])): 
       opciones.append(pregunta["incorrect_answers"][numRespuesta])
    # Añadimos la respuesta correcta
    opciones.append(pregunta["correct_answer"])
    
    # Las reordenamos para sea un poco más aleatório
    random.shuffle(opciones)
   
    # imprimimos la respuesta por pantalla. ¡Hasta aquí genial! 
    contador=0
    for respuesta in range(len(opciones)):
        contador=contador+1
        print(f"{contador} {opciones[respuesta]}")

    # recogemos la respuesta del usuario y realizo la comprobación
    
    respuestaUsuario=-1

    while respuestaUsuario<=0 or respuestaUsuario>len(opciones):
        respuestaUsuario=int(input("Enter the number of your answer: "))
    
    respuestaUsuario-=1
    if opciones[respuestaUsuario]==pregunta["correct_answer"]:
        aciertos+=1
    else:
        fallos+=1

porcentaje_Acierto = (aciertos/numPreguntas) * 100
print()
print(f"You had {aciertos} correct answers.")
print(f"You had {fallos} incorrect answers.")
print(f"Your final score is {porcentaje_Acierto}")











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
