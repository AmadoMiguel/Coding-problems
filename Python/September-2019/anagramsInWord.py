# Given a word W and a string S, find all starting indices in S which are anagrams of W.
#
# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.


def findAnagIndeces(word, s):
    # Prepare the array that will hold the indexes of start of the sub-anagrams
    startIndexes = []
    # iterate over each word and extract len(s) characters, sort both and check if are equal
    index = 0
    if len(s) > len(word):
        return "Word not long enough"
    while index <= len(word) - len(s):
        frag = word[index:index + len(s)]
        # Compare fragment and s
        sortFrag = sorted(frag)
        sortS = sorted(s)
        if sortFrag == sortS:
            startIndexes.append(index)
            print("Anagram found:", sortS, sortFrag)
        index += 1
    return startIndexes


print(findAnagIndeces("abxaba", "ab"))
