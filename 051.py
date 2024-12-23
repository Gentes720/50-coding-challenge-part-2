import numpy as np
sentence = "programming is cool"
frequences = np.empty((2,2))
for letter in sentence:
    i = 0
    c = 0
    while i < len(sentence):
        if letter == sentence[i]:
            c += 1
        i += 1
    frequence = np.array([letter, c])
    frequences_save = np.vstack((frequences, frequence))
    frequences = frequences_save

print(frequences)
