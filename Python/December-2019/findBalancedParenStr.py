# Given a string of parentheses, find the balanced string that can be produced from it using the minimum number
# of insertions and deletions. If there are multiple solutions, return any of them.
#
# For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".


def reduceParenthesis(parStrList):
    ps = parStrList[:]
    while '(' in ps and ')' in ps:
        indxOfClose = ps.index(')')
        indxOfOpen = indxOfClose - 1
        del ps[indxOfOpen: indxOfClose + 1]
    return ps


def insertOpenPar(parStrList):
    ps = parStrList[:]
    ps.insert(0, '(')
    return ps


def insertClosePar(parStrList):
    ps = parStrList[:]
    ps.append(')')
    return ps


def conformBalancedString(parStr):
    parStrList = list(parStr)
    finalParList = parStrList[:]
    while len(parStrList):
        parStrList = reduceParenthesis(parStrList)
        if len(reduceParenthesis(insertOpenPar(parStrList))) < len(parStrList):
            finalParList.insert(0, '(')
            parStrList.insert(0, '(')
        if len(reduceParenthesis(insertClosePar(parStrList))) < len(parStrList):
            finalParList.append(')')
            parStrList.append(')')

    return "".join(finalParList)


paren = "()(()()(()(()()((()))("
print(conformBalancedString(paren))
