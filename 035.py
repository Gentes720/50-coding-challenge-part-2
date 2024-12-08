import numpy as np
def CSVtext_to_2Darray(text):
    i = 0
    array= np.empty((3,3), dtype= object)# object because numpy doesn't convert well list elements with variating lengths
    intermediate_list= text.split("\n")# break into a list of 3 elements. mean 'pierre,21,maoroc' is one element
    for element in intermediate_list:
        array[i] = element.split(",") # break each list element into another list of 3 element eg ['pierre' '21' 'maroc']
        i += 1 
    print(array)
CSVtext_to_2Darray("pierre,21,maroc\njean,20,france\npaul,19,chine")