pythtTripl = []
ind1 = 0
ind2 = 1

def findPythTripl(a):
    global pythtTripl
    global ind1
    global ind2
    for n3 in a[ind2+1:]:
        if a[ind1]**2 + a[ind2]**2 == n3**2:
            if (a[ind1],a[ind2],n3) not in pythtTripl: 
                pythtTripl.append( (a[ind1],a[ind2],n3) )
    if ind1 < len(a) - 3:
        if ind2 < len(a) - 2:
            ind2 += 1
        else:
            ind1 += 1
            ind2 = ind1 + 1
        findPythTripl(a)    

a = [0,1,2,3,5,13,9,20,2,25,3,8]
findPythTripl(sorted(a))
print(pythtTripl)