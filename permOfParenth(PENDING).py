def printBalancedBrackets(n):
    openBrack = '('
    closeBrack = ')'
    nOfBracks = n * 2
    brackStr = ""
    for i in range(nOfBracks):
        if i < n:
            brackStr = brackStr + openBrack
        else:
            brackStr = brackStr + closeBrack        

    print(brackStr)    

printBalancedBrackets(2)    