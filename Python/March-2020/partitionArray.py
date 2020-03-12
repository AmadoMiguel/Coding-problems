# Given a list of numbers and an integer k, partition/sort the list such that the all numbers less than k occur
# before k, and all numbers greater than k occur after the number k.


def partitionNums(nums, pivot):
    lessThan, equalTo, greaterThan = [], [], []
    for n in nums:
        if n < pivot:
            lessThan += [n]
        elif n == pivot:
            equalTo += [n]
        elif n > pivot:
            greaterThan += [n]
    return lessThan + equalTo + greaterThan


numbers = [3, 4, 1, 2, 7, 6, 8, 5, 9]
partNum = 2
print(partitionNums(numbers, partNum))
