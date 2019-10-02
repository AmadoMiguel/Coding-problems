# A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits,
# such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.
#
# You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits,
# solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3],
# which should be interpreted as the word1 + word2 = word3 cryptarithm.
#
# If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping
# in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true.
# If it does not become a valid arithmetic solution, the answer is false.
#
# Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).


def isCryptSolution(crypt, solution):
    # Transform solution to a map for more intuitive indexing
    solutionMap = {i[0]: i[1] for i in solution}
    # Iterate over the crypt words
    decryptedSolution = []
    for w in crypt:
        decryptedWord = ""
        # Iterate over each letter and get the mapped number
        for l in w:
            decryptedWord += solutionMap[l]
        # Check if there is any leading 0, otherwise continue
        if len(decryptedWord) > 1 and decryptedWord[0] == '0':
            return False
        decryptedSolution.append(decryptedWord)
    # Check if the decrypted solution is valid
    if int(decryptedSolution[0]) + int(decryptedSolution[1]) == int(decryptedSolution[2]):
        return True
    else:
        return False


print(isCryptSolution(["SEND", "MORE", "MONEY"],
                      [['O', '0'],
                       ['M', '1'],
                       ['Y', '2'],
                       ['E', '5'],
                       ['N', '6'],
                       ['D', '7'],
                       ['R', '8'],
                       ['S', '9']]
                      ))
