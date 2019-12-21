# Given a string, you need to reverse the order of characters in each word within a sentence while still
# preserving whitespace and initial word order.
#
# Example 1:
# Input: "The cat in the hat"
# Output: "ehT tac ni eht tah"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.


def reverseWords(string):
    ptrL1, ptrL2 = None, None
    for i in range(len(string)):
        if string[i] != " " and ptrL1 is None:
            ptrL1 = i
        if i + 1 == len(string):
            ptrL2 = i
        elif string[i + 1] == " ":
            ptrL2 = i
        if ptrL1 is not None and ptrL2 is not None:
            string = string.replace(string[ptrL1:ptrL2 + 1], string[ptrL1:ptrL2 + 1][::-1])
            ptrL1, ptrL2 = None, None

    return string


words = "The cat in the hat is too sad"
print(reverseWords(words))
