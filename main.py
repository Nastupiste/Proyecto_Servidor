# Para manipular JSON.
import json
# Para acceder a una url.
import requests
# Para generar un número aleatorio
import random
# Para poder tener ventana.
from tkinter import *
from tkinter import ttk

numPreguntas=""

# Funciones
def respuestaValida(opciones):
    while True:
        try:
            respuesta=int(entry.get())
            if 1<=respuesta<=opciones:
                return respuesta
            else:

                print("Invalid answer. Please choose a number between 1 and", opciones)
        except ValueError:
            print("Sorry, you should write a valid answer: ")

def validarNumPreguntas():
    while True:
        try:
            respuesta=int(entry.get())
            #self.value=respuesta
            if 1<=respuesta<=50:
                return respuesta
            else:
                label = ttk.Label(root_window, text="Invalid answer. Please choose a number between 1 and 50.")
        except ValueError:
            label = ttk.Label(root_window, text="Sorry, you should enter a number between 1 and 50.")

# Creo ventana principal

root_window=Tk()
root_window.minsize(width=500, height=500)
root_window.title("Welcome to the Trivia´s API quest!")


# Interacción con el usuario
label = ttk.Label(root_window, text="How many questions do yo want to answer?\n(from 1 to 50):")
label.pack()
# Recogida de datos

entry=ttk.Entry(root_window)
entry.pack()
submit_button = ttk.Button(root_window, text="Enviar", command=validarNumPreguntas)
submit_button.pack()
#print(self.value)

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

label = ttk.Label(root_window, text="The category is "+preguntas[0]["category"])

"""for pregunta in preguntas:
    opciones=[]
    
    label_question=ttk.Label(root_window, text=pregunta["question"])
    label_question.pack()

    option_title=ttk.Label(root_window, text="Options: ")
    option_title.pack()

    # Este for añade las respuestas malas a una lista de opciones
    for numRespuesta in range(len(pregunta["incorrect_answers"])): 
       opciones.append(pregunta["incorrect_answers"][numRespuesta])
    # Añadimos la respuesta correcta
    opciones.append(pregunta["correct_answer"])
    
    # Las reordenamos para sea un poco más aleatório
    random.shuffle(opciones)
   
    # imprimimos la respuesta por pantalla. ¡Hasta aquí genial! 
    contador=0
    cadena_respuestas=""

    for respuesta in range(len(opciones)):
        contador=contador+1
        cadena_respuestas+=(f"{contador} {opciones[respuesta]}\n")

    label_answers=ttk.Label(root_window, text=cadena_respuestas)
    label_answers.pack()

    # recogemos la respuesta del usuario y realizo la comprobación
    # prevengo que la respuesta no sea un carácter o un número mayor que las opciones disponibles.
    respuestaUsuario=-1


    label = ttk.Label(root_window, text="Enter your answer: ")

    respuestaUsuario=respuestaValida(len(opciones))
    
    # Necesitamos restar 1 a la respuesta, porque la lista va de 0 a 3 como máximo.
    respuestaUsuario-=1
    if opciones[respuestaUsuario]==pregunta["correct_answer"]:
        aciertos+=1
    else:
        fallos+=1

#porcentaje_Acierto = (aciertos/numPreguntas) * 100

if porcentaje_Acierto>=50:
    final_label=ttk.Label(root_window, text="Well done! You have passed the quiz!")
    final_label.pack()
else:
    final_label=ttk.Label(root_window, text="You lose... Don't worry, you'll get them next time!")
    final_label.pack()

print(f"You had {aciertos} correct answers.")
print(f"You had {fallos} incorrect answers.")
print(f"Your final score is {porcentaje_Acierto}")"""
root_window.mainloop()