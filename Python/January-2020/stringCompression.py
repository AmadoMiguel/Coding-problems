# Given an array of characters with repeats, compress it in place. The length after compression should be less than or
# equal to the original array.
#
# Example:
# Input: ['a', 'a', 'b', 'c', 'c', 'c']
# Output: ['a', '2', 'b', 'c', '3']


def compressStringArray(array):
    currentIndex = 0
    while currentIndex < len(array):
        numOfChars = 0
        replaceIndex = currentIndex
        currentChar = array[currentIndex]
        while replaceIndex < len(array) and array[replaceIndex] == currentChar:
            numOfChars += 1
            replaceIndex += 1
        # Check if there is need to compress current equal characters
        if numOfChars > 1:
            del array[currentIndex:replaceIndex]
            array[:currentIndex] += [currentChar, str(numOfChars)]
            currentIndex += 2
        else:
            # Advance general index
            currentIndex += 1


# array = ['a', 'a', 'b', 'c', 'c', 'c', 'd', 'd', 'a', 'f', 'f']
array = ['a', 'b', 'c', 'd', 'a', 'f']
compressStringArray(array)
print(array)
