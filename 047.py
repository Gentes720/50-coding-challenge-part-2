import numpy as np
initial_array = np.arange(27).reshape(3, 3, 3)
copied_array = np.zeros((3, 3, 3))
print(initial_array)
for line_counter in range(0, 3):
    for column_counter in range(0, 3):
        for item_counter in range(0, 3):
            copied_array[line_counter][column_counter][item_counter] = initial_array[line_counter][column_counter][item_counter]
print(copied_array)