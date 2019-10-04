# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    # Invert both linked lists
    invertedA = []
    invertedB = []
    # Reverse both linked lists
    while a != None:
        invertedA.insert(0, a.value)
        a = a.next
    while b != None:
        invertedB.insert(0, b.value)
        b = b.next
    # Adjust lengths in order to facilitate result conformation
    if len(invertedA) > len(invertedB):
        for _ in range(0, len(invertedA) - len(invertedB)):
            invertedB.append(0)
    if len(invertedB) > len(invertedA):
        for _ in range(0, len(invertedB) - len(invertedA)):
            invertedA.append(0)
    # Initialize final result
    finalResult = []
    rem = None
    indx = 0
    while indx < len(invertedA):
        sum = invertedA[indx] + invertedB[indx]
        if sum <= 9999:
            if rem != None:
                sum += rem
                if sum <= 9999:
                    finalResult.insert(0, sum)
                    rem = None
                else:
                    rem = sum - 9999
                    finalResult.insert(0, 0)
            else:
                finalResult.insert(0, sum)
        else:
            rem = sum - 9999
            finalResult.insert(0, 0)
        indx += 1
    if rem != None:
        while rem > 9999:
            rem = int(rem / 10000)
        finalResult.insert(0, rem)
    return finalResult
