def capitalize_1st_letter(sentence):
    i, transition= 0, []
    sentence = sentence.capitalize()
    transition = sentence.split()
    while i < len(transition)-1:
        transition[i + 1] = " " + transition[i + 1].capitalize()
        i += 1
    sentence = ""
    sentence = sentence.join(transition) 
    return sentence

print(capitalize_1st_letter("i'm good at programmig And my friend too"))