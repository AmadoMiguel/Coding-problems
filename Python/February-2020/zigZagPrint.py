

def zigZagPrint(sentence, k):
    if k == 1:
        print(sentence)
    else:
        zigZagString = [[" " for _ in range(len(sentence))] for _ in range(k)]
        currIndx = 0
        up, down = False, True
        for i in range(len(sentence)):
            zigZagString[currIndx][i] = sentence[i]
            if up:
                currIndx -= 1
            if down:
                currIndx += 1
            if currIndx == k - 1:
                up, down = True, False
            elif currIndx == 0:
                up, down = False, True
        
        for r in zigZagString:
            print("".join(r))

zigZagPrint("thisisazigzag", 4)
