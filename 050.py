import numpy as np
import random
def arrayCreator(n):
    arrayOfElement = np.arange(n)
    arrayOfElement = np.insert(arrayOfElement,n , n)
    return np.random.permutation(arrayOfElement)

print(arrayCreator(8))