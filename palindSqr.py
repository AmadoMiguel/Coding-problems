import numpy as np

def isPalindrome(num):
    strNum = str(num)
    isPalim = True

    ind = len(strNum) - 1
    if len(strNum) % 2 == 0:
        midPoint = (len(strNum) / 2)
    else:
        midPoint = ((len(strNum)+1) / 2) - 1
    for i in strNum[:midPoint]:
        if i != strNum[ind]:
            isPalim = False
            break
        else:
            ind -= 1
            continue    
    return isPalim

def hasSquareRoot(num):
    flag = False
    if int(np.sqrt(num) + 0.5) ** 2 == num:
        flag = True
    return flag       


def isPalAndSquare(num):
    if isPalindrome(num) and hasSquareRoot(num):
        if isPalindrome(int(np.sqrt(num))):
            return True
        else:
            return False
    else:
        return False        
            
l = range(1,10000)
nPalAndSq = 0
lPalAndSq = []
for n in l:
    if isPalAndSquare(n):
        nPalAndSq += 1
        lPalAndSq.append(n)
    else:
        continue    
print(lPalAndSq)