from ventana_ui import *
from main import *
from Cuestionario import *

cuestionario=Cuestionario()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.eTitulo.setText("Welcome to the Trivia´s API quest!")
        self.eSubTitulo.setText("How many questions do yo want to answer?\n(from 1 to 50):")
        self.bConfirmar.clicked.connect(self.Confirmar)
        self.BotonConfRespuesta.setEnabled(False)
        self.BotonConfRespuesta.clicked.connect(self.respuestaUsuario) 
    
    def Confirmar(self):
        cuestionario.set_numPreguntas(int(self.spinBoxNumPreguntas.value()))
        cuestionario.set_categoria(generaCategoria())
        cuestionario.set_datos(llamadaApi(cuestionario.get_numPreguntas(),cuestionario.get_categoria()))
        self.cargaPreguntas()
        self.bConfirmar.setEnabled(False)
        self.BotonConfRespuesta.setEnabled(True)

    def cargaPreguntas(self):

        preguntas=cuestionario.get_datos()["results"]
        self.eSubTitulo.setText("The category is "+preguntas[0]["category"])
        
        self.fallos=0
        self.aciertos=0

        for pregunta in preguntas:
            opciones=[]
            self.textAreaPregunta.setText(pregunta["question"])
            # Este for añade las respuestas malas a una lista de opciones
            for numRespuesta in range(len(pregunta["incorrect_answers"])): 
                opciones.append(pregunta["incorrect_answers"][numRespuesta])
            # Añadimos la respuesta correcta
            opciones.append(pregunta["correct_answer"])
            random.shuffle(opciones)
            cadenaOpciones=""
            contador=0
            for respuesta in range(len(opciones)):
                contador=contador+1
                cadenaOpciones+=f"{contador} {opciones[respuesta]}\n"
            self.textAreaRespuestas.setText(cadenaOpciones)
            cuestionario.set_opciones(opciones)
            cuestionario.set_preguntaActual(pregunta)

        resultadoFinal=calculaResultado(self.aciertos,self.fallos, cuestionario.get_numPreguntas())
        self.texAreaResultados.setText(resultadoFinal)
    

    def respuestaUsuario(self):
        opciones = cuestionario.get_opciones()
        respuestaValida = respuestaValida(self, len(opciones))
        pregunta = cuestionario.get_preguntaActual()
        if opciones[respuestaValida] == pregunta["correct_answer"]:
            self.aciertos += 1
        else:
            self.fallos += 1


              
     















"""if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        window = MainWindow()
        window.show()
        app.exec_()
    except Exception as e:
        print(f"An error occurred: {str(e)}")"""

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

