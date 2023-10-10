
from tkinter import *
from tkinter import ttk

def validarNumPreguntas():
    while True:
        try:
            respuesta=int(entry.get())
            if 1<=respuesta<=50:
                return respuesta
            else:
                label = ttk.Label(root_window, text="Invalid answer. Please choose a number between 1 and 50.")
        except ValueError:
            label = ttk.Label(root_window, text="Sorry, you should enter a number between 1 and 50.")


root_window=Tk()
root_window.minsize(width=500, height=500)
root_window.title("Welcome to the Trivia´s API quest!")

# Interacción con el usuario
label = ttk.Label(root_window, text="How many questions do yo want to answer?\n(from 1 to 50):")
label.pack()
# Recogida de datos
entry=ttk.Entry()
entry.pack()
submit_button = ttk.Button(root_window, text="Enviar", command=validarNumPreguntas)
submit_button.pack()
#numPreguntas=validarNumPreguntas(entry)
root_window.mainloop()