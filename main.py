# Para manipular JSON.
import json

# Para acceder a una url.
import requests
# Para poder tener ventana.
import tkinter as tk
from tkinter import *


# Hacemos la solicitud de los datos a la url.
respuesta=requests.get("https://www.bne.es/sites/default/files/redBNE/datosgob/awe/tema/videojuegos.json")
datos=respuesta.json()

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


# Si quisiera imprimir los datos obtenidos en formato json:
# print(json.dumps(datos, indent=4, sort_keys=True))
