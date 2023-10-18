from ventana_ui import *
from main import *
from Cuestionario import *
import html

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
        self.bConfirmar.clicked.connect(self.confirmar)
        self.BotonRespuesta1.clicked.connect(self.boton1Pulsado)
        self.BotonRespuesta2.clicked.connect(self.boton2Pulsado)
        self.BotonRespuesta3.clicked.connect(self.boton3Pulsado)
        self.BotonRespuesta4.clicked.connect(self.boton4Pulsado)

        self.BotonRespuesta1.setEnabled(False)
        self.BotonRespuesta2.setEnabled(False)
        self.BotonRespuesta3.setEnabled(False)
        self.BotonRespuesta4.setEnabled(False)

    def arreglaStrings(self,string):
        return html.unescape(string)

    def confirmar(self):
        cuestionario.set_numPreguntas(int(self.spinBoxNumPreguntas.value()))
        self.spinBoxNumPreguntas.setEnabled(False)
        cuestionario.set_categoria(generaCategoria())
        cuestionario.set_datos(llamadaApi(cuestionario.get_numPreguntas(),cuestionario.get_categoria()))
        self.bConfirmar.setEnabled(False)
        self.BotonRespuesta1.setEnabled(True)
        self.BotonRespuesta2.setEnabled(True)
        self.BotonRespuesta3.setEnabled(True)
        self.BotonRespuesta4.setEnabled(True)
        self.preguntas=cuestionario.get_datos()["results"]
        self.eSubTitulo.setText("The category is "+self.arreglaStrings(self.preguntas[cuestionario.contador]["category"]))
        
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
        self.textAreaPregunta.setText(self.arreglaStrings(self.preguntas[cuestionario.contador]["question"])) 
        cuestionario.set_preguntaActual(self.preguntas[cuestionario.contador]["question"])
        cuestionario.set_respuestaActual(self.preguntas[cuestionario.contador]["correct_answer"])

        opciones=[]
        opciones.append(self.preguntas[cuestionario.contador]["correct_answer"])
        opciones.extend(self.preguntas[cuestionario.contador]["incorrect_answers"])
        random.shuffle(opciones)

        if(len(opciones)==4):
            self.BotonRespuesta3.setEnabled(True)
            self.BotonRespuesta4.setEnabled(True)

        cuestionario.set_boton1(opciones[0])
        self.BotonRespuesta1.setText(self.arreglaStrings(cuestionario.get_boton1()))

        cuestionario.set_boton2(opciones[1])
        self.BotonRespuesta2.setText(self.arreglaStrings(cuestionario.get_boton2()))
        try:
            cuestionario.set_boton3(opciones[2])
            self.BotonRespuesta3.setText(self.arreglaStrings(cuestionario.get_boton3()))

            cuestionario.set_boton4(opciones[3])
            self.BotonRespuesta4.setText(self.arreglaStrings(cuestionario.get_boton4()))

        except:
            self.BotonRespuesta3.setEnabled(False)
            self.BotonRespuesta4.setEnabled(False)
            self.BotonRespuesta3.setText("")
            self.BotonRespuesta4.setText("")
            pass

    def cargaPreguntas(self):
        cuestionario.contador+=1 
        
        if self.respuestaElegida==cuestionario.get_respuestaActual():
            self.aciertos+=1
        else:
            self.errores+=1     

        if cuestionario.contador<=cuestionario.get_numPreguntas()-1:
            self.listaDeRespuestas()

        else:
            self.BotonRespuesta1.setEnabled(False)
            self.BotonRespuesta2.setEnabled(False)
            self.BotonRespuesta3.setEnabled(False)
            self.BotonRespuesta4.setEnabled(False)
            self.texAreaResultados.setText(calculaResultado(self.aciertos,self.errores,cuestionario.get_numPreguntas()))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

