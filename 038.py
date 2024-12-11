import numpy as np
def sting_to_character(AsciiCode):
    string = "".join(chr(code) for code in AsciiCode)
    return(string)

print(sting_to_character([105, 101, 119, 111, 106, 108, 98]))