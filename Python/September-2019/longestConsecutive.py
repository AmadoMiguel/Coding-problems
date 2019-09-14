# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

consecutiveNumsList = []
consecutiveNums = []
index = 0


def findLongestConsecutiveNums(arr, i):
    global consecutiveNumsList
    global consecutiveNums
    global index

    if i + 1 < len(arr):
        # Index to traverse the list from current global index to the
        # end-1 index of the list
        idx = i
        # Retrieve current number
        currNum = arr[idx]
        # Insert current number into array of consecutive numbers
        consecutiveNums.append(currNum)
        # Retrieve next number
        nextNum = arr[idx + 1]
        # Conform list of consecutive numbers within the range of the array
        # from the current global index
        while nextNum - currNum == 1:
            idx += 1
            if idx + 1 < len(arr):
                consecutiveNums.append(nextNum)
                currNum = arr[idx]
                nextNum = arr[idx+1]
            else:
                nextNum = arr[idx]
                consecutiveNums.append(nextNum)
                break
        # Add it to the general list of lists of consecutive numbers
        if len(consecutiveNums) > 1:
            consecutiveNumsList.append(consecutiveNums)
        # Clear the consecutive numbers list
        consecutiveNums = []
        # Go to next index
        index += 1
        findLongestConsecutiveNums(arr, index)
    # Retrieve largest list of consecutive numbers
    lenLargetsList = 0
    largestList = []
    for l in consecutiveNumsList:
        if len(l) > lenLargetsList:
            lenLargetsList = len(l)
            largestList = l

    return largestList


a = [100, 99, 4, 200, 199, 198, 197, 196, 1, 3, 2]
a.sort()
print(findLongestConsecutiveNums(a, 0))
