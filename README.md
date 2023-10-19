TRIVIAL´S API

# Proyecto_Servidor

requisitos previos:

- Tener instalado python3 y pip
- Instalar el los paquetes incluidos en el archivo requirements.text para ello ejecutar el siguiente comando: pip install -r requirements.txt

Proyecto de investigación para la asignatura de Desarrollo de Entorno Servidor para el grado superior de FP DAW.

1. Nos conectaremos con una API de trivial a través de una URL:

- "https://opentdb.com/api.php?amount=25&category=21"

- La url será distinta en cada ejecución ya que el usuario eligirá una cantidad de preguntas (entre 1 y 50) y la categoría será elegida de manera aleatoria cada vez.

2. Accederemos al formato JSON de la misma. Un ejemplo:{ "category": "Sports", "type": "multiple", "difficulty": "easy", "question": "Which team has won the most Stanley Cups in the NHL?", "correct_answer": "Montreal Canadians", "incorrect_answers": [ "Chicago Blackhawks", "Toronto Maple Leafs", "Detroit Red Wings" ] }

3. Volcaremos el contenido en estructuras de datos para poder manipularlos.

- Usando diccionarios, mostraremos las preguntas y las posibles opciones.
- El usuario responderá y se hará una comprobación, ofreciéndole un resultado.

4. Enlace al video demostración en youtube: https://youtu.be/whHiXdI9h18?si=D8ADAnmyCkB8BoyV
