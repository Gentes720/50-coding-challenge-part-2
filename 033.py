string = "1,2,3,4,5,6,7,87694586,65,5969"
list= string.split(",") # seperate the sting into list elements delimited by the comma
sum = 0
for element in list :
    if element != ",":
        sum = sum + int(element)# sum
print(sum)