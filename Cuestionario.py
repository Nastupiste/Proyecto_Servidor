class Cuestionario:
    def __init__(self, numPreguntas=None, categoria=None, datos=None, opciones=None, preguntaActual=None, respuestaActual=None, respuestasIncorrectas=None):
        self.numPreguntas = numPreguntas
        self.categoria = categoria
        self.datos = datos
        self.preguntaActual = preguntaActual
        self.respuestaActual = respuestaActual
        self.respuestasIncorrectas = respuestasIncorrectas
        self.opciones = opciones
        self.contador = 0
        self.boton1 = ""
        self.boton2 = ""
        self.boton3 = ""
        self.boton4 = ""

    def siguientePregunta(self):
        self.contador+=1

    def set_numPreguntas(self, numPreguntas):
        self.numPreguntas = numPreguntas

    def get_numPreguntas(self):
        return self.numPreguntas

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_categoria(self):
        return self.categoria

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos
        
    def set_opciones(self, opciones):
        self.opciones = opciones

    def get_opciones(self):
        return self.opciones
    
    def set_preguntaActual(self,preguntaActual):
        self.preguntaActual = preguntaActual

    def get_preguntaActual(self):
        return self.preguntaActual
    
    def set_respuestaActual(self,respuestaActual):
        self.respuestaActual = respuestaActual

    def get_respuestaActual(self):
        return self.respuestaActual
    
    def set_respuestasIncorrectas(self,respuestasIncorrectas):
        self.respuestasIncorrectas = respuestasIncorrectas

    def get_respuestasIncorrectas(self):
        return self.respuestasIncorrectas

    def set_boton1(self,boton1):
        self.boton1 = boton1

    def get_boton1(self):
        return self.boton1
    
    def set_boton2(self,boton2):
        self.boton2 = boton2

    def get_boton2(self):
        return self.boton2
    
    def set_boton3(self,boton3):
        self.boton3 = boton3

    def get_boton3(self):
        return self.boton3

    def set_boton4(self,boton4):
        self.boton4 = boton4

    def get_boton4(self):
        return self.boton4