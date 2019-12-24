# Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888.
# 678 is not a palindrome. Do not convert the integer into a string.


def getPowOf10(num):
    powOfTen = 0
    while 10 ** (powOfTen + 1) < num:
        powOfTen += 1
    return 10 ** powOfTen


def getMiddleNumber(num, powOf10):
    midNum = num % powOf10  # Remove first digit
    midNum = int(midNum / 10)  # Remove last digit
    return midNum


def firstAndLastDigits(num, powOf10):
    fd = int(num / powOf10)
    ld = num % 10
    return fd, ld


def isPalindrome(num):
    print("number:", num)
    # Base case
    if num < 10:
        return True
    # Get first and last digits
    powOf10 = getPowOf10(num)
    fd, ld = firstAndLastDigits(num, powOf10)
    return fd == ld and isPalindrome(getMiddleNumber(num, powOf10))


num = 122353221
print(isPalindrome(num))
