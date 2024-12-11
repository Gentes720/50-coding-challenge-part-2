def caeser_cypher(string, key):
    alphabet = "abcdefgkijklmnopqrstuvwxyz"
    crypted_string = ""
    for letter in string:                   # for each letter in the word
        for i in range (0, len(alphabet)):  # we find it index inside the alphabet
            if letter == alphabet[i]:              
                crypted_string += ""+ alphabet[(i + int(key))%26] # add the key to the index and add the corresponding letter
    return(crypted_string)

print(caeser_cypher("abcz", 8))    