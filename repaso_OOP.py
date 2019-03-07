from math import pi

class Circulo:
    def __init__(self,radio,coordenada):
        self.radio=radio
        self.coordenada=coordenada
        
    def obtener_area(self):
        return ((self.radio)**2)*pi

    def obtener_perimetro(self):
        return 2*pi*self.radio

    def __str__(self):
        return "Circulo - radio " + str(self.radio)

class Rectangulo:
    def __init__(self,lado1,lado2,coordenada):
        self.a=lado1
        self.b=lado2
        self.coordenada=coordenada

    def obtener_area(self):
        return self.a*self.b

    def obtener_perimetro(self):
        return (2*self.a)+(2*self.b)

    def es_cuadrado(self):
        if self.a==self.b:
            return True
        False
    
