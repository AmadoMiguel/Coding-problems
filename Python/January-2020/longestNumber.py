# Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. 
# For example, given [10, 7, 76, 415], you should return 77641510.


def compareNums(num1, num2):
    strNum1, strNum2 = str(num1), str(num2)
    # In case numbers have same length
    if len(strNum1) == len(strNum2):
        if num1 < num2:
            return 1
        if num1 > num2:
            return -1
        return 0
    # If numbers have different length, the "longest" number in this case
    # will be the one that has all its digits (even if is only one digit)
    # greater than the other number's digits even if it has more/less digits
    ptrNum1, ptrNum2 = 0, 0
    currDig1, currDig2 = None, None
    while ptrNum1 < len(strNum1) or ptrNum2 < len(strNum2):
        if ptrNum1 < len(strNum1):
            currDig1 = strNum1[ptrNum1]
        if ptrNum2 < len(strNum2):
            currDig2 = strNum2[ptrNum2]
        if currDig1 is not None and currDig2 is not None:
            if currDig1 < currDig2:
                return 1
            if currDig1 > currDig2:
                return -1
        ptrNum1 += 1
        ptrNum2 += 1
    return 0


# Typical selection sort algorithm
def sortNums(nums, callback):
    for i in range(len(nums)):
        maxIndex = i
        for j in range(i + 1, len(nums)):
            if callback(nums[maxIndex], nums[j]) >= 0:
                maxIndex = j
        temp = nums[maxIndex]
        nums[maxIndex] = nums[i]
        nums[i] = temp
    return nums


print(sortNums([10, 7, 79, 785], compareNums))
