def distance_2points(a, b):
    distance = round(((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5, 3)
    return(distance)

print(distance_2points([1, 1], [4,4]))
