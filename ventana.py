from ventana_ui import *
from main import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.etiquetaSaludo.setText("Welcome to the Trivia´s API quest!")
        self.etiquetaNumPregunta("How many questions do yo want to answer?\n(from 1 to 50):")
        self.botonConfirmar.clicked.connect(self.Confirmar)
    
    def Confirmar(self):
        numPreguntas=self.spinBoxNumPreguntas.toPlainText()
        categoria=generaCategoria()
        datos=llamadaApi(numPreguntas,categoria)
        ##falta genera cuestionario    

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        window = MainWindow()
        window.show()
        app.exec_()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

 

