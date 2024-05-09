# Crear una clase que represente un Círculo, que reciba como parámetro un
# número positivo que indique el radio, usando la modalidad de propiedades para los
# métodos gettter y setter, además calcule el área y el perímetro.

import math

class Circulo:

    def __init__(self, radius) -> None:
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius
    
    def area(self):
        return round((self._radius * math.pi) ** 2, 2)
    
    def perimetro(self):
        return round((2 * math.pi * self._radius), 2)
    
circle = Circulo(10)

print(circle.radius)
circle.radius = 5
print(circle.radius)
print(circle.area())
print(circle.perimetro())
