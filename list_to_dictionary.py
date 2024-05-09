def list_to_dictionary(list: list):
    dictionary = {}
    for element in list:
        if (element not in dictionary):
            dictionary[element] = 0
        else:
            dictionary[element] += 1
    return dictionary

print(list_to_dictionary([1,1,1,5,6,5,2,1,2,3,5,1,1,2,3]))