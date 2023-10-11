# Para manipular JSON.
import json
# Para acceder a una url.
import requests
# Para generar un número aleatorio
import random
# Para poder tener ventana.
import tkinter as tk
from tkinter import *
#Funciones
def respuestaValida(opciones):
    r_incorrecta=True
    while r_incorrecta:
        try:
            respuesta=int(input("Enter the number of your answer: "))
            if 1<=respuesta<=opciones:
                r_incorrecta=False
                return respuesta
            else:
                print("Invalid answer. Please choose a number between 1 and", opciones)
        except ValueError:
            print("Sorry, you should write a valid answer: ")
def validarNumPreguntas():
    r_incorrecta=True
    while r_incorrecta:
        try:
            respuesta=int(input("How many questions do yo want to answer?\n(from 1 to 50):"))
            if 1<=respuesta<=50:
                r_incorrecta=False
                return respuesta
            else:
                print("Invalid answer. Please choose a number between 1 and 50.")
        except ValueError:
            print("Sorry, you should enter a number between 1 and 50. ")


# Interacción con el usuario
print()
print("Welcome to the Trivia´s API quest!")     
numPreguntas=validarNumPreguntas()
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
    # prevengo que la respuesta no sea un carácter o un número mayor que las opciones disponibles.
    respuestaUsuario=-1
    respuestaUsuario=respuestaValida(len(opciones))
    respuestaUsuario-=1
    if opciones[respuestaUsuario]==pregunta["correct_answer"]:
        aciertos+=1
    else:
        fallos+=1
porcentaje_Acierto = (aciertos/numPreguntas) * 100
print()
if porcentaje_Acierto>=50:
    print("Well done! You have passed the quiz!")
else:
    print("You lose... Don't worry, you'll get them next time!")
print()
print(f"You had {aciertos} correct answers.")
print(f"You had {fallos} incorrect answers.")
print(f"Your final score is {porcentaje_Acierto}")