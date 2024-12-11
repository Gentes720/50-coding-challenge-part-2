import numpy as np
def sting_to_character(AsciiCode):
    string = "".join(chr(code) for code in AsciiCode)#for each code in ascii array we convert the code
    return(string)                                   #to a caracter then add the caracter to the final string

print(sting_to_character([105, 101, 119, 111, 106, 108, 98]))