# Para poder tener ventana.
import tkinter as tk
from tkinter import *

# Creamos una nueva ventana:
# Convertimos a texto los datos:
texto = json.dumps(datos, ensure_ascii= False, indent=2)
ventana = tk.Tk()
# Creamos una nueva ventana:
# Convertimos a texto los datos:
texto = json.dumps(datos, ensure_ascii= False, indent=2)
ventana = tk.Tk()

# Añado un elemento scrollBar a la ventana:
scrol_bar= tk.Scrollbar(ventana)
scrol_bar.pack(side='right', fill='y')

# Para poder configurar el texto y formato de la ventana
txt = tk.Text(ventana, font="Times32")
txt.pack()
txt.config(yscrollcommand=scrol_bar.set)
scrol_bar.config(command=txt.yview)
txt.insert('end', texto)

ventana.mainloop()