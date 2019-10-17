# You are given an array of desired filenames in the order of their creation. Since two files cannot have equal
# names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest
# positive integer such that the obtained name is not used yet.
#
# Return an array of names that will be given to the files.


def fileNaming(names):
    if not len(names):
        return []
    if len(names) == 1:
        return names
    index = 1
    return checkPreviousNames(names[:index], index, names[index], names)


def checkPreviousNames(prevNames, index, currName, fileNames):
    if currName in prevNames:
        currName += '(1)'
        currNameAsList = list(currName)
        kToAdd = 1
        while currName in prevNames:
            # Increment the parenthesis number
            kToAdd += 1
            # Last parenthesis number is always going to be at position -2
            currNameAsList[-2] = str(kToAdd)
            currName = "".join(currNameAsList)
        fileNames[index] = currName
    if index + 1 < len(fileNames):
        index += 1
        fileNames = checkPreviousNames(fileNames[:index], index, fileNames[index], fileNames)
    return fileNames


print(fileNaming(["doc",
                  "doc",
                  "image",
                  "doc(1)",
                  "doc"]))
