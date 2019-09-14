def nLoops(num):
    strNum = str(num)
    nLoops = 0
    for d in strNum:
        if d == '0' or d == '6' or d == '9':
            nLoops += 1
        elif d == '8':
            nLoops += 2    
    print("Number of loops in",num,":",nLoops)

nLoops(128069)    