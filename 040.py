def bubble_sort(array):
    n = len(array)
    for i in range(n -1):
        for j in range (n - i - 1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
    return(array)

print(bubble_sort([1, 3, 5, 9, 2, 4, 8, 6, 7, 0]))
