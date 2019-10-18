# Write a function that reverses characters in (possibly nested) parentheses in the input string.
#
# Input strings will always be well-formed with matching ()s.


def reverseInParentheses(inputString):
    return revStringInParenthesis(inputString)


def revStringInParenthesis(string):
    print(string)
    # Transform input string into list
    strAsList = list(string)
    if '(' in string and ')' in string:
        # Find first index of appereance of '(' from end to beginning
        indxLastOpenPar = (len(strAsList) - 1) - strAsList[::-1].index('(')
        # Find first index of appereance of ')'
        indxFirstClosePar = strAsList[indxLastOpenPar:].index(')') + indxLastOpenPar
        # Reverse the enclosed substring between those indeces
        subStr = strAsList[indxLastOpenPar + 1:indxFirstClosePar]
        reversedSubStr = subStr[::-1]
        strAsList[indxLastOpenPar + 1:indxFirstClosePar] = reversedSubStr[:]
        # Remove brackets (first last, then first)
        del strAsList[indxFirstClosePar]
        del strAsList[indxLastOpenPar]
        # Reassign string
        string = "".join(strAsList)
        string = revStringInParenthesis(string)
    return string


print(reverseInParentheses("foo(bar(baz))blim"))
