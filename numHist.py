l = [1,1,3,4,5,5,6,2,4,2,2]
numHist = {}

for n in l:
    numHist[str(n)] = numHist.get(str(n),0) + 1

print(l,numHist)

for k,v in numHist.items():
    if v > 1:
        print(k)
        break