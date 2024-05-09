def square_generator():
    for i in range(1, 11):
        yield i ** 2
    
squares = square_generator()

for square in squares:
    print(square)