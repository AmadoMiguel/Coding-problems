# You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string.
# Determine whether the parentheses are balanced.
#
# For example, (()* and (*) are balanced. )*( is not balanced.


def checkBalancedParenthesis(strWithPar):
    return checkParenthesis(strWithPar)


def checkParenthesis(parStr):
    print(parStr)
    strAsLst = list(parStr)
    if '(' in strAsLst:
        # Find last index for '('
        lastOpenIndex = (len(strAsLst) - 1) - strAsLst[::-1].index('(')
        # Next ')' or '*' from that index
        if ')' in strAsLst[lastOpenIndex:]:
            nextCloseIndex = strAsLst[lastOpenIndex:].index(')') + len(strAsLst[:lastOpenIndex])
            # Delete close index and open parenthesis index
            del strAsLst[nextCloseIndex]
            del strAsLst[lastOpenIndex]
            checkParenthesis("".join(strAsLst))
        elif '*' in strAsLst[lastOpenIndex:]:
            nextStarIndex = strAsLst[lastOpenIndex:].index('*') + len(strAsLst[:lastOpenIndex])
            # Delete star index and open parenthesis index
            del strAsLst[nextStarIndex]
            del strAsLst[lastOpenIndex]
            checkParenthesis("".join(strAsLst))
        else:
            return "Parenthesis aren't balanced"
    elif '*' in strAsLst and len(strAsLst) > 1:
        # Find first index of '*'
        firstStarIndex = strAsLst.index('*')
        if ')' in strAsLst[firstStarIndex+1:]:
            nextCloseIndex = strAsLst[firstStarIndex+1:].index(')') + len(strAsLst[:firstStarIndex+1])
            # Delete items in both indexes
            del strAsLst[nextCloseIndex]
            del strAsLst[firstStarIndex]
            checkParenthesis("".join(strAsLst))
        elif '*' in strAsLst[firstStarIndex+1:]:
            nextStarIndex = strAsLst[firstStarIndex+1:].index('*') + len(strAsLst[:firstStarIndex+1])
            # Delete indexes
            del strAsLst[nextStarIndex]
            del strAsLst[firstStarIndex]
            checkParenthesis("".join(strAsLst))
        else:
            return "Parenthesis aren't balanced"
    elif len(strAsLst) >= 1:
        return "Parenthesis aren't balanced"

    return "Parenthesis are balanced"


print(checkBalancedParenthesis(')((*(*)*)*(())))()(((((*())*))(*'))
