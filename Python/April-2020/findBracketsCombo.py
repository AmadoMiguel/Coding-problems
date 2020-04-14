# You're a coder - you know how important it is to have a closing parenthesis for every opening parenthesis!
# Given n pairs of parentheses, write a function that generates all of the possible combinations of regular
# parentheses, sorted in lexicographical order.


def addPar(n, nO, nC, nP, cC):
    if nC == n:
        addPar.brackets.append("".join(cC))
    else:
        if nO < n:
            cC[nP] = "("
            addPar(n, nO + 1, nC, nP + 1, cC)
        if nO > nC:
            cC[nP] = ")"
            addPar(n, nO, nC + 1, nP + 1, cC)


def generateParentheses(n):
    combs = ["" for _ in range(n * 2)]
    addPar.brackets = []
    addPar(n, 0, 0, 0, combs)
    return addPar.brackets
