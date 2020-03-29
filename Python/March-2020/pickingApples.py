# A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she
# goes along, but is meticulous about not putting different kinds of apples in the same bag.
#
# Given an input describing the types of apples she will pass on her path, in order, determine the length of the
# longest portion of her path that consists of just two types of apple trees.
#
# For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a
# length of four.


def findLongestPortion(appleTypes):
    leftHandType, rightHandType = None, None
    numApplesLeft, numApplesRight = 0, 0
    maxPortion = 0
    for t in appleTypes:
        if leftHandType is None:
            numApplesLeft += 1
            leftHandType = t
        elif leftHandType == t:
            numApplesLeft += 1
        elif rightHandType is None:
            numApplesRight += 1
            rightHandType = t
        elif rightHandType == t:
            numApplesRight += 1
        else:
            # Reset picked up apples so far
            if maxPortion < numApplesRight + numApplesLeft:
                maxPortion = numApplesRight + numApplesLeft
                print("Longest portion types:", leftHandType, rightHandType)
            leftHandType, rightHandType, numApplesLeft, numApplesRight = t, None, 1, 0
    return maxPortion


print(findLongestPortion([2, 1, 2, 3, 3, 1, 3, 5]))
