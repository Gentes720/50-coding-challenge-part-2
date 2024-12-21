import numpy as np
def sum_of_all_num_in_jaggedarray(jagged_array):
    numpyArray = np.array(jagged_array)
    return numpyArray.max()

print(sum_of_all_num_in_jaggedarray([[2, 3, 85], [57, 576, 55], [57, 577, 55]]))