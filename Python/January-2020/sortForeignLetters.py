# You come across a dictionary of sorted words in a language you've never seen before. Write a program that
# returns the correct order of letters in this language.
#
# For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].


def getSortedLetters(words):
    letters = []
    for i in range(len(words)):
        # Compare current letter with next letter
        if i < len(words) - 1:
            word1, word2 = words[i], words[i+1]
            ptrW1, ptrW2 = 0, 0
            while ptrW1 < len(word1) or ptrW2 < len(word2):
                if ptrW1 < len(word1) and ptrW2 < len(word2):
                    letW1, letW2 = word1[ptrW1], word2[ptrW2]
                    # Analise different cases.
                    #   Letters are different and none of them are in the array
                    if letW1 != letW2 and (letW1 not in letters and letW2 not in letters):
                        letters += [letW1, letW2]
                        break
                    #   Letters are different and one of them is in the array (could be any)
                    elif letW1 != letW2 and (letW1 in letters and letW2 not in letters):
                        indxOfLet1 = letters.index(letW1)
                        letters[:indxOfLet1+1] += [letW2]
                        break
                    elif letW1 != letW2 and (letW1 not in letters and letW2 in letters):
                        indxOfLet2 = letters.index(letW2)
                        letters.insert(indxOfLet2, letW1)
                        break
                    #   Letters are equal and that letter is not in the array
                    elif letW1 == letW2 and letW1 not in letters:
                        letters += [letW1]
                        break
                # In case letters are repeated and one of the words is longer than the other
                else:
                    if ptrW1 < len(word1):
                        if word1[ptrW1] not in letters:
                            letters += [word1[ptrW1]]
                            break
                    if ptrW2 < len(word2):
                        if word2[ptrW2] not in letters:
                            letters += [word2[ptrW2]]
                            break
                ptrW1, ptrW2 = ptrW1 + 1, ptrW2 + 1
    return letters


print(getSortedLetters(["baa", "abcd", "abca", "cab", "cad"]))
