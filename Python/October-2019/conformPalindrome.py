# Given a string, find the shortest possible string which can be achieved by adding characters to the end of
# initial string to make it a palindrome.


def buildPalindrome(st):
    if st == st[::-1]:
        return st
    return conformPalindromes(st, None, len(st))


def conformPalindromes(inputString, shortestPalind, index):
    currentString = inputString + "".join(list(inputString)[:index][::-1])
    if isPalindrome(currentString):
        if shortestPalind is None or len(currentString) < len(shortestPalind):
            shortestPalind = currentString
    if index > 0:
        shortestPalind = conformPalindromes(inputString, shortestPalind, index - 1)
    return shortestPalind


def isPalindrome(s):
    return s == s[::-1]


print(buildPalindrome("abbcd"))
