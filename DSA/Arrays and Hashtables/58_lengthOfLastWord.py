word = 'Hello World   Chitra '

def lastWord(word):
    i, length = len(word)-1, 0
    while word[i] == ' ':
        i = i-1
    while i>=0 and word[i] != ' ':
        length = length +1
        i = i -1
    return length

print(lastWord(word))
