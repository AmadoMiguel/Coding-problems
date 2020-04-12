# Given a string, determine if you can remove any character to create a palindrome.


def isPalindrome(string):
    lS = len(string)
    if lS <= 1:
        return True
    return string[0] == string[-1] and isPalindrome(string[1:-1])


def canBePalindrome(charSeq):
    lCh = len(charSeq)
    for i in range(lCh):
        if isPalindrome(charSeq[:i] + charSeq[i + 1:]):
            return True
    return False


tests = ["abcdcbea", "abccba", "abccaa"]
for t in tests:
    print(canBePalindrome(t))

