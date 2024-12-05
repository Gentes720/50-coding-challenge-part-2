import numpy as np
def text_to_array(text):
    textArray = np.array(text.split())
    print(textArray)

text_to_array("je suis une star")