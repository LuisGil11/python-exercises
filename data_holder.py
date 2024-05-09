# Escriba una clase llamada Data_Holder con dos(2) parámetros x, y. Implemente
# las funciones __str_ ) y __repr__ para que devuelva la representación formateada ₍
# de los valores x, y

class Data_Holder:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"el valor de x es: {self.x} y el de y es: {self.y}"
    
    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"
    
myDataHolder = Data_Holder(10,5)
