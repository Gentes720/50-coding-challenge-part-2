import random
import numpy as np
arrayOfString = np.array([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])

intermediate_array = np.random.permutation(arrayOfString.flatten())
shuffled_array = intermediate_array.reshape(arrayOfString.shape)
print(shuffled_array)