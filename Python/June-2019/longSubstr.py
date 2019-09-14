indxInit = 0
indxFin = 1
foundSubstr = []

# This function returns a substring with k different 
# characters at the most
def allSubStrings(s,k,le):
    subStr = []
    nDiffChar = 0
    foundSub = False
    global indxInit
    global indxFin
    global foundSubstr
    
    for l in s[indxInit:indxFin+1]:
        # A new character found
        if l not in subStr:
            nDiffChar += 1
        # Add character to substring
        subStr.append(l)

        if nDiffChar > k or len(subStr) == le-1:
            break
    if nDiffChar == k:       
        if "".join(subStr) not in foundSubstr: foundSubstr.append("".join(subStr))
    
    if indxInit == 0:
        if indxFin <= le-2:
            indxFin += 1
            allSubStrings( s,k,le )
        else:
            indxInit += 1
            indxFin = indxInit + 1
            allSubStrings( s,k,le )
    elif indxInit <= le-2:
        if indxFin <= le-1:
            indxFin += 1
            allSubStrings( s,k,le )
        else:
            indxInit += 1
            indxFin = indxInit + 1
            allSubStrings( s,k,le )
    
    return foundSubstr            
    
    
st = "abcbaefabd"    
l = len(st)
subStrings = allSubStrings(st,4,l)
print(subStrings)