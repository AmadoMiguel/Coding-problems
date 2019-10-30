# Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses
# in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can
# approximate this using strings.
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string
# is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.


def validateBalancedBrackets(brackStr):
    return checkBrackets(brackStr)


def checkBrackets(brackets):
    brackAsList = list(brackets)
    if len(brackAsList) % 2 != 0:
        return False
    else:
        # Find index of last opening bracket of any kind
        if '(' in brackAsList:
            indxOfLastOpenBrack = len(brackAsList) - 1 - brackAsList[::-1].index('(')
            # Find index of next closing ')'
            if ')' in brackAsList[indxOfLastOpenBrack:]:
                indxOfNextClosBrack = brackAsList[indxOfLastOpenBrack:].index(')') + indxOfLastOpenBrack
                # Delete both indexes from the list and proceed
                del brackAsList[indxOfNextClosBrack]
                del brackAsList[indxOfLastOpenBrack]
                print(brackAsList)
            else:
                # Next closing bracket wasn't found
                return False
        if '[' in brackAsList:
            indxOfLastOpenBrack = len(brackAsList) - 1 - brackAsList[::-1].index('[')
            # Find index of next closing ']'
            if ']' in brackAsList[indxOfLastOpenBrack:]:
                indxOfNextClosBrack = brackAsList[indxOfLastOpenBrack:].index(']') + indxOfLastOpenBrack
                # Delete both indexes from the list and proceed
                del brackAsList[indxOfNextClosBrack]
                del brackAsList[indxOfLastOpenBrack]
                print(brackAsList)
            else:
                # Next closing bracket wasn't found
                return False
        if '{' in brackAsList:
            indxOfLastOpenBrack = len(brackAsList) - 1 - brackAsList[::-1].index('{')
            # Find index of next closing '}'
            if '}' in brackAsList[indxOfLastOpenBrack:]:
                indxOfNextClosBrack = brackAsList[indxOfLastOpenBrack:].index('}') + indxOfLastOpenBrack
                # Delete both indexes from the list and proceed
                del brackAsList[indxOfNextClosBrack]
                del brackAsList[indxOfLastOpenBrack]
                print(brackAsList)
            else:
                # Next closing bracket wasn't found
                return False
        # If no more '(, [, {' opening brackets and length is even, is not balanced
        if '(' not in brackAsList and '[' not in brackAsList and '{' not in brackAsList and len(brackAsList) > 0:
            return False
        if len(brackAsList) > 0:
            checkBrackets("".join(brackAsList))
        # If all brackets have a proper match, then are balanced
        return True


print(validateBalancedBrackets('{({)[(}]){[}}]'))
