# Write a function that reverses the digits a 32-bit signed integer, x. Assume that the environment can only store
# integers within the 32-bit signed integer range, [-2^31, 2^31 - 1]. The function returns 0 when the reversed integer
# overflows.
#
# Example:
# Input: 123
# Output: 321


def reverseInteger(num):
    numToStr = str(num)
    reversedNum = numToStr[::-1]
    reversedInt = int(reversedNum)
    if reversedInt > (2 ** 31) - 1:
        return 0
    if reversedInt < (2 ** 31) * (-1):
        return 0
    return reversedInt


num = 231
print(reverseInteger(num))
