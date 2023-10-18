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
