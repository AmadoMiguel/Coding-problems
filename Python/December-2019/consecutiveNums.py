# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.
#
# Example:
# Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
# Output: ['0->2', '5->5', '7->11', '15->15']
# Assume that all numbers will be greater than or equal to 0, and each element can repeat.


def buildConsecutiveNumsString(nums):
    consecNums = []
    num1, num2 = None, None
    for n in nums:
        if num1 is None:  # Only for initial iteration
            num1 = n
            continue
        if (num2 is None and (n == num1 + 1 or n == num1)) or (num2 is not None and (n == num2 + 1 or n == num2)):
            num2 = n
        else:  # Found range
            if num2 is None:  # No next consecutive or repeated number found
                consecNums += [str(num1) + "->" + str(num1)]
            else:  # Place current range
                consecNums += [str(num1) + "->" + str(num2)]
            num1, num2 = n, None
    # Place the last range similarly
    if num2 is None:  # No next consecutive or repeated number found
        consecNums += [str(num1) + "->" + str(num1)]
    else:  # Place current range
        consecNums += [str(num1) + "->" + str(num2)]
    return consecNums


n = [0, 1, 2, 3, 5, 5, 5, 6, 7, 8, 9, 9, 10, 11, 15, 16, 17, 18, 18, 18, 19, 19, 19, 20, 21, 23]
print(buildConsecutiveNumsString(n))
