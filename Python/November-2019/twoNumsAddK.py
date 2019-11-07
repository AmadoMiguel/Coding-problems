# Given a list and a number k, find out if two number in the list add up to k


def twoSum(lst, k):
    for i in range(len(lst)):
        # Get current number
        currNum = lst[i]
        print(currNum)
        # Check if k - currNum is in the list
        if i == 0:
            if k - currNum in lst[i+1:]:
                return True
        elif i == len(lst) - 1:
            if k - currNum in lst[:i]:
                return True
        else:
            if k - currNum in lst[:i] + lst[i:]:
                return True
    return False


print(twoSum([4, 7, 1, -3, 2], 3))
