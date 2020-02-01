# One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.
#
# For a pattern to be valid, it must satisfy the following:
#
# All of its keys must be distinct.
# It must not connect two keys by jumping over a third key, unless that key has already been used.
# For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.
#
# Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
# [
#     1  2  3
#     4  5  6
#     7  8  9
# ]


# Function to identify invalid combinations
def isInvalidCombination(comb):
    if len(comb):
        if len(comb) == 1:
            return False
        else:
            for i in range(len(comb)):
                if i + 1 < len(comb):
                    currNum = comb[i]
                    nextNum = comb[i + 1]
                    # For now hard-coded invalid patterns
                    if currNum == 1 and (nextNum == 3 or nextNum == 7 or nextNum == 9):
                        return True
                    elif currNum == 2 and nextNum == 8:
                        return True
                    elif currNum == 3 and (nextNum == 1 or nextNum == 7 or nextNum == 9):
                        return True
                    elif currNum == 4 and nextNum == 6:
                        return True
                    elif currNum == 6 and nextNum == 4:
                        return True
                    elif currNum == 7 and (nextNum == 3 or nextNum == 1 or nextNum == 9):
                        return True
                    elif currNum == 8 and nextNum == 2:
                        return True
                    elif currNum == 9 and (nextNum == 3 or nextNum == 1 or nextNum == 7):
                        return True
    return False


# Brute-force approach. Looking forward to enhance performance in the future.
def getAllValidCombinations(remNums, currNums, k, totalValidCombs):
    if not len(remNums) or len(currNums) == k:
        if not isInvalidCombination(currNums):
            totalValidCombs += 1
            print(currNums)
    else:
        for i in range(len(remNums)):
            curr = currNums + [remNums[i]]
            rem = remNums[:i] + remNums[i + 1:]
            totalValidCombs = getAllValidCombinations(rem, curr, k, totalValidCombs)
    return totalValidCombs


print(getAllValidCombinations([1, 2, 3, 4, 5, 6, 7, 8, 9], [], 4, 0))
