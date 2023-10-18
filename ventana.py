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
        
        self.respuestaElegida=""
        self.aciertos=0
        self.errores=0
        
        self.eTitulo.setText("Welcome to the Trivia´s API quest!")
        self.eSubTitulo.setText("How many questions do yo want to answer?\n(from 1 to 50):")
        self.bConfirmar.clicked.connect(self.Confirmar)
        self.BotonRespuesta1.clicked.connect(self.boton1Pulsado)
        self.BotonRespuesta2.clicked.connect(self.boton2Pulsado)
        self.BotonRespuesta3.clicked.connect(self.boton3Pulsado)
        self.BotonRespuesta4.clicked.connect(self.boton4Pulsado)
     

    def Confirmar(self):
        cuestionario.set_numPreguntas(int(self.spinBoxNumPreguntas.value()))
        cuestionario.set_categoria(generaCategoria())
        cuestionario.set_datos(llamadaApi(cuestionario.get_numPreguntas(),cuestionario.get_categoria()))
        self.bConfirmar.setEnabled(False)
        self.preguntas=cuestionario.get_datos()["results"]
        self.eSubTitulo.setText("The category is "+self.preguntas[cuestionario.contador]["category"])
        
        self.listaDeRespuestas()

       
    def boton1Pulsado(self):
        self.respuestaElegida=cuestionario.get_boton1()
        self.cargaPreguntas()

    def boton2Pulsado(self):
        self.respuestaElegida=cuestionario.get_boton2()
        self.cargaPreguntas()

    def boton3Pulsado(self):
        self.respuestaElegida=cuestionario.get_boton3()
        self.cargaPreguntas()

    def boton4Pulsado(self):
        self.respuestaElegida=cuestionario.get_boton4()
        self.cargaPreguntas()

    def listaDeRespuestas(self):

        self.textAreaPregunta.setText(self.preguntas[cuestionario.contador]["question"]) 
        cuestionario.set_preguntaActual(self.preguntas[cuestionario.contador]["question"])
        cuestionario.set_respuestaActual(self.preguntas[cuestionario.contador]["correct_answer"])

        opciones=[]
        opciones.append(self.preguntas[cuestionario.contador]["correct_answer"])
        opciones.extend(self.preguntas[cuestionario.contador]["incorrect_answers"])
        random.shuffle(opciones)

        cuestionario.set_boton1(opciones[0])
        self.BotonRespuesta1.setText(cuestionario.get_boton1())

        cuestionario.set_boton2(opciones[1])
        self.BotonRespuesta2.setText(cuestionario.get_boton2())
        try:
            cuestionario.set_boton3(opciones[2])
            self.BotonRespuesta3.setText(cuestionario.get_boton3())

            cuestionario.set_boton4(opciones[3])
            self.BotonRespuesta4.setText(cuestionario.get_boton4())

        except:
            print("No hay más de 2 respuestas")
            pass


    def cargaPreguntas(self):
        cuestionario.contador+=1
        
        if cuestionario.contador<cuestionario.get_numPreguntas():
           
            if self.respuestaElegida==cuestionario.get_respuestaActual():
                self.aciertos+=1
            else:
                self.errores+=1        
            
            self.listaDeRespuestas()

        else:
            print("He terminado el cuestionario")
            self.texAreaResultados.setText(calculaResultado(self.aciertos,self.errores,cuestionario.get_numPreguntas()))

        

        

        




            
            
            
        #https://pybonacci.org/2020/03/27/curso-de-creacion-de-guis-con-qt-capitulo-09-signals-y-slots/
        #resultadoFinal=calculaResultado(self.aciertos,self.fallos, cuestionario.get_numPreguntas())
        #self.texAreaResultados.setText(resultadoFinal)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

