# Sort a list with 3 unique numbers in O(n) time


def sortNums(l):
    sortedList = []
    # Three options: number is max, number is min or neither of these two.
    # Max num is appended, min num is set to index 0 and middle number is
    # put in between
    for n in l:
        if n == max(l):
            sortedList.append(n)
        elif n == min(l):
            sortedList.insert(0, n)
        else:
            if len(sortedList) > 0:
                if min(l) in sortedList:
                    # Find last index of min num
                    lastIndexOfMin = len(sortedList) - sortedList[::-1].index(min(l))
                    # Set n to that index
                    sortedList.insert(lastIndexOfMin, n)
                else:
                    sortedList.insert(0, n)
            else:
                sortedList.append(n)
    return sortedList


lst = [3, 3, 2, 1, 3, 2, 1, 2, 1, 2, 3, 1, 3, 1, 3, 2, 3, 1, 1, 2, 3, 1, 3, 1, 1, 2, 1, 3, 1]

print(lst)
print(sortNums(lst))
