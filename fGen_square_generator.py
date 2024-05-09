# Cree una función generadora llamada square_generator() que retorne lo
# números del 1 al 10 elevados al cuadrado


def square_generator():
    for i in range(1, 11):
        yield i ** 2
    
squares = square_generator()

for square in squares:
    print(square)