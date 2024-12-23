# longest word in a string
def the_longestWordIn(sentence):
    list_of_words = sentence.split()
    longest_Word = list_of_words[0]
    print(list_of_words)
    for i in range(1, len(list_of_words)):
        if len(longest_Word) < len(list_of_words[i]):
            longest_Word = list_of_words[i]
    return longest_Word
sentence = "the boy is cool"
print(the_longestWordIn(sentence))