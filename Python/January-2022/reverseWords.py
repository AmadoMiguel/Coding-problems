# Create a function that receives a string of words, and reverses the individual words, but it doesn't change the
# ordering of the words within the sentence

def reverseWords(sentence):
    reversedWordsStr = ""
    lenSent = len(sentence)
    indxBeginCurrWord, indxEndCurrWord = 0, 0
    wordStarts = False
    for i in range(lenSent):
        # Check if current char is part of a word
        if sentence[i] not in [".", ",", "\n", " "]:
            if not wordStarts:
                wordStarts = True
                indxBeginCurrWord = i
        else:
            # Reverse word and add current punctuation char
            if wordStarts:
                indxEndCurrWord = i - 1
                reversedWordsStr += sentence[indxBeginCurrWord:indxEndCurrWord+1][::-1]
                wordStarts = False
            reversedWordsStr += sentence[i]
    #     Check for last word
    if wordStarts:
        reversedWordsStr += sentence[indxBeginCurrWord:][::-1]
    return reversedWordsStr


print(reverseWords("Hello, John and Me are in the park"))
