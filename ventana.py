from ventana_ui import *
from main import *
from Cuestionario import *
from PyQt5.QtWidgets import QApplication,QPushButton
from PyQt5.QtCore import pyqtSlot,pyqtSignal,QEventLoop

cuestionario=Cuestionario()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

       
        self.eTitulo.setText("Welcome to the Trivia´s API quest!")
        self.eSubTitulo.setText("How many questions do yo want to answer?\n(from 1 to 50):")
        self.bConfirmar.clicked.connect(self.Confirmar)
        self.BotonRespuesta1.clicked.connect(self.boton1)
        self.BotonRespuesta2.clicked.connect(self.boton2)
        self.BotonRespuesta3.clicked.connect(self.boton3)
        self.BotonRespuesta4.clicked.connect(self.boton4)
    
    def boton1(self):
        respuestaElegida=self.BotonRespuesta1.getText()
    
    def boton2(self):
        respuestaElegida=self.BotonRespuesta2.getText()

    def boton3(self):
        respuestaElegida=self.BotonRespuesta3.getText()
    
    def boton4(self):
        respuestaElegida=self.BotonRespuesta4.getText()  


    def Confirmar(self):
        cuestionario.set_numPreguntas(int(self.spinBoxNumPreguntas.value()))
        cuestionario.set_categoria(generaCategoria())
        cuestionario.set_datos(llamadaApi(cuestionario.get_numPreguntas(),cuestionario.get_categoria()))
        self.bConfirmar.setEnabled(False)
        preguntas=cuestionario.get_datos()["results"]
        self.eSubTitulo.setText("The category is "+preguntas[0]["category"])
        self.textAreaPregunta.setText(preguntas[0]["question"])
        cuestionario.set_preguntaActual(preguntas[0]["question"])
        cuestionario.set_respuestaActual(preguntas[0]["correct_answer"])
        cuestionario.set_respuestasIncorrectas(preguntas[0]["incorrect_answers"])
       
        self.BotonRespuesta1.setText(cuestionario.get_respuestaActual())
        self.BotonRespuesta1.setText(cuestionario.get_respuestasIncorrectas()[0])



    def cargaPreguntas2(self):
        respuesta=int(self.spinBoxNumRespuesta.value())
        
        if True: #respuestaEstaBien:
            pass
        else:
            pass

        


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
                cadenaOpciones+=f"{contador}.  {opciones[respuesta]}\n"
            self.textAreaRespuestas.setText(cadenaOpciones)
            cuestionario.set_opciones(opciones)
            cuestionario.set_preguntaActual(pregunta)

            
            
            
            
            #https://pybonacci.org/2020/03/27/curso-de-creacion-de-guis-con-qt-capitulo-09-signals-y-slots/
            


        resultadoFinal=calculaResultado(self.aciertos,self.fallos, cuestionario.get_numPreguntas())
        self.texAreaResultados.setText(resultadoFinal)
    

    def respuestaUsuario(self):
        opciones = cuestionario.get_opciones()
        respuestaValida = validarRespuesta(self, len(opciones))
        pregunta = cuestionario.get_preguntaActual()
        if opciones[respuestaValida] == pregunta["correct_answer"]:
            self.aciertos += 1
        else:
            self.fallos += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

