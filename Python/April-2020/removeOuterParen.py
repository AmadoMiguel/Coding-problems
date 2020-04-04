# Given a valid parenthesis string (with only '(' and ')', an open parenthesis will always end with a close
# parenthesis, and a close parenthesis will never start first), remove the outermost layers of the parenthesis
# string and return the new parenthesis string.
#
# If the string has multiple outer layer parenthesis (ie (())()), remove all outer layers and construct the
# new string. So in the example, the string can be broken down into (()) + (). By removing both components outer
# layer we are left with () + '' which is simply (), thus the answer for that input would be ().


def removeOuterParenthesis(parenString):
    innerParen = ""
    numOpen, numClose = 0, 0
    currInner = ""
    for p in parenString:
        if p == "(":
            numOpen += 1
        elif p == ")":
            numClose += 1
        currInner += p
        if numOpen == numClose:
            innerParen += currInner[1:-1]
            currInner = ""
    # print(innerParen)
    return innerParen


assert removeOuterParenthesis("(())()") == "()"  # True
assert removeOuterParenthesis("(()())") == "()()"  # True
assert removeOuterParenthesis("()()()") == ""  # True
