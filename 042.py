def are_intersecting(coordinate1, coordinate2, radius1, radius2):
    def distance_2points(a, b):
        distance = round(((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5, 3)
        return(distance)
    if distance_2points(coordinate1, coordinate2) <= radius1 + radius2 :
        return True
    else:
        return False
    
print(are_intersecting([2, 4], [1, 2], 4,8))
 


