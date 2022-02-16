# Given an Integer N, generate all the valid combinations of N pairs of parenthesis

def isParenValid(paren):
    parenDif = 0
    for p in paren:
        if p == "(":
            parenDif += 1
        else:
            if not parenDif:
                return False
            parenDif -= 1
    return not parenDif


combs = []


def combinePar(currPar, currParLen, n):
    # Base case
    if currParLen == n * 2:
        if isParenValid(currPar):
            combs.append(currPar)
    else:
        combinePar(currPar+"(", currParLen+1, n)
        combinePar(currPar+")", currParLen+1, n)


def generateParen(n):
    combinePar("", 0, n)
    return combs


print(generateParen(4))
