def number_of_words(sentence):
    numberOfWords = 0
    for element in sentence:
        if element == " ": # each words are separated by spaces then the numbeer of worrs
            numberOfWords +=1 # is the number of spaces +1
    return numberOfWords +1
print(number_of_words("I'm good at python and my friend too"))