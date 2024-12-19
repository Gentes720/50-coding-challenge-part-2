import numpy as np
def copy_column(twoD_array, column):
    column1 = np.zeros((1,3))
    a = int(column)
    for i in range (0, 3):
        column1[0][i] = twoD_array[i][a] # in column1[0][i] makes to iterate through the columns only 
    print(column1)        # twoD_array[i][a] as doesn't change iterates through the lines only

copy_column([[1,2,3], [1,2,3], [1,2,3]], 0)
