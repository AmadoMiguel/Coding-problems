import string

def atbash(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    atbashAlph = {}
    d = 7
    for l in letters:
        # Determine ASCII code of each letter
        letCode = ord(l)
        atbashAlph[l] = chr(letCode-d)
        d += 2
    newWord = []
    for l in word:
        newWord.append( atbashAlph[l] )
    return "".join(newWord)    

print( atbash('himynameismiguel') )