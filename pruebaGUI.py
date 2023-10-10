
import tkinter as tk
from tkinter import ttk

def validarNumPreguntas():
    while True:
        try:
            respuesta = int(entry.get())
            if 1 <= respuesta <= 50:
                return respuesta
            else:
                label.config(text="Respuesta inválida. Por favor, elija un número entre 1 y 50.")
        except ValueError:
            label.config(text="Lo siento, debe ingresar un número válido.")

# Crear ventana principal
root_window = tk.Tk()
root_window.minsize(width=500, height=500)
root_window.title("Bienvenido a la Trivia API Quest")

# Etiqueta
label = ttk.Label(root_window, text="¿Cuántas preguntas desea responder?\n(De 1 a 50):")
label.pack()

# Recogida de datos
entry = ttk.Entry()
entry.pack()

# Botón para enviar y usar validarNumPreguntas como comando
submit_button = ttk.Button(root_window, text="Enviar", command=validarNumPreguntas)
submit_button.pack()

# Iniciar la ventana
root_window.mainloop()

# Después de cerrar la ventana, puedes acceder al valor devuelto por la función.
valor_elegido = validarNumPreguntas()
print("El valor elegido por el usuario es:", valor_elegido)