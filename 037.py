import numpy as np
def sting_to_character(string):
    array_of_Asciicaracters = np.empty((len(string)-1,))
    array_of_caracters = np.array(list(string), dtype = object)#from sting to list then from list to array
    for i in range(0, len(array_of_caracters)-1):
        array_of_Asciicaracters[i] = ord(array_of_caracters[i])# conversion of each caracter
    return(array_of_Asciicaracters)


print(sting_to_character("jewojlreljej"))
