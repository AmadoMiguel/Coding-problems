def checkAnagramInWord(parentString,childString):
    times = 0

    for i in range(0,len(parentString) - len(childString)):
        auxStr = parentString[ i:i+len(childString) ]
        if (sorted(auxStr.lower()) == sorted(childString.lower())):
            times += 1

    print(times)

checkAnagramInWord('AbrAcadAbRa','cAda')