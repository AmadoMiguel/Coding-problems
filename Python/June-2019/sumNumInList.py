import random

randList = []
randNum = random.randint(10,15)
for i in range(0,random.randint(4,7)):
    randList.append(random.randint(0,9))

print(randList,randNum)

for i in range(0,len(randList)):
    auxNum = randList[i]
    for i in randList[i+1:]:
        if auxNum + i == randNum:
            print(auxNum,"+",i,"=",randNum)