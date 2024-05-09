# Cree una función generadora llamada number_doubler() que tome una lista de
# números y entregue cada número multiplicado por 2

def number_doubler(list: list): 
    for element in list:
        yield element * 2

a = number_doubler([2,5,4,6,8,4,2,5,6])

for element in a:
    print(element)