possibleWays = 0

def nWaysDecode(numStr):
    global possibleWays
    if '0' in numStr:
        print("No possible ways to represent the number.")
    else:
        ind = 0
        possibleWays += 1
        for n in numStr:
            if ind + 1 > len(numStr)-1:
                break  
            if int(n + numStr[ind+1]) <= 26:
                print(int(n + numStr[ind+1]))
                possibleWays += 1
                if ind + 2 < len(numStr)-1:
                    if int(numStr[ind+1]+numStr[ind+2]) <= 26:
                        possibleWays += 1 
            ind += 1    
    return possibleWays

print( nWaysDecode("52125") )