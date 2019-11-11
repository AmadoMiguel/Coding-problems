# You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that
# represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up
# these huge integers and return the result in the same format.

# Example
#
# For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
# addTwoHugeNumbers(a, b) = [9876, 5434, 0].
#
# Explanation: 987654321999 + 18001 = 987654340000.


# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None


def addTwoHugeNumbers(a, b):
    (aInv, bInv, result) = ([], [], [])
    aCopy = a
    while aCopy:
        aInv.insert(0, aCopy.value)
        aCopy = aCopy.next
    bCopy = b
    while bCopy:
        bInv.insert(0, bCopy.value)
        bCopy = bCopy.next
    # Then add both lists in the same format
    (indxLst1, indxLst2, currentSum, res) = (0, 0, 0, 0)
    while indxLst1 < len(aInv) or indxLst2 < len(bInv):
        currentSum = 0  # Reset current sum
        # Add numbers for current indexes (including res)
        if indxLst1 < len(aInv):
            currentSum += aInv[indxLst1]
        if indxLst2 < len(bInv):
            currentSum += bInv[indxLst2]
        # Add res
        currentSum += res
        res = 0  # Flush res to avoid accumulation
        # Check length of number
        sumAsList = list(str(currentSum))
        while len(sumAsList) > 4:
            res += int(sumAsList[0])
            del sumAsList[0]
        # Then add the current sum to the result list
        result.insert(0, int("".join(sumAsList)))
        # Update indexes
        (indxLst1, indxLst2) = (indxLst1 + 1, indxLst2 + 1)
    if res:
        result.insert(0, res)
    return result


# Initialize numbers
a = ListNode(123)
a.next = ListNode(4)
a.next.next = ListNode(5)

b = ListNode(100)
b.next = ListNode(100)
b.next.next = ListNode(100)

print(addTwoHugeNumbers(a, b))
