# Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given
# words in a string.
#
# For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world",
# return 1 because there's only one word "cat" in between the two words.


def findSmallestDistanceBetweenWords(word1, word2, words):
    smallestDistance = findDistanceBetweenWords(word1, word2, list(words), None)


def findDistanceBetweenWords(w1, w2, listOfWords, smallestDistance):
    if w1 in listOfWords and w2 in listOfWords:  # Avoid words not in list error
        # Find index of w1 in current list of words
        indxW1 = listOfWords.index(w1)
        # Find index of w2 in current list of words
        indxW2 = listOfWords.index(w2)
        # Then compare to smallest distance
        currentDistance = indxW2 - indxW1 - 1
        if currentDistance >= 0:
            if currentDistance < smallestDistance or smallestDistance is None:
                smallestDistance = currentDistance
        # Then recurse from the last found index of w1
        smallestDistance = findDistanceBetweenWords(w1, w2, listOfWords[indxW1 + 1:], smallestDistance)
    return smallestDistance


print(findSmallestDistanceBetweenWords('hello', 'world', 'dog cat hello cat dog dog hello cat world'))
