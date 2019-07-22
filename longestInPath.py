import re

lowestLvl = '\n\t'
finalStr = ["dir"]

def mainPathDict(path):
    global lowestLvl
    global finalStr
    lowLvlFound = False
    lastLnBr = ""
    for w in path:
        # If a tab is found
        if '\t' in w:
            # Store it
            lastLnBr = w 
        # A folder/file name is      
        else:
            # A sub level is found
            if len(lastLnBr) > len(lowestLvl):
                lowestLvl = lastLnBr
                finalStr.append('/'+w)
                lowLvlFound = True
            # Still the same folder level
            elif len(lastLnBr) == len(lowestLvl):
                if len(finalStr) == 1:
                    finalStr.append('/'+w)
                elif len(finalStr) > 1:    
                    finalStr[-1] = '/'+w
            # Decreases folder level        
            elif len(lastLnBr) < len(lowestLvl):
                lowestLvl = lastLnBr 
                # Delete last element
                del finalStr[-1]
                # Update value of deleted element
                finalStr[-1] = '/'+w     

        if lowLvlFound and re.search('.ext',finalStr[-1]):
            longPath = "".join(finalStr)      
    print(longPath)
    
pathStr = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\t\t\tfile2.ext\n\tsubdir2\n\t\tsubsubdir2"
# Find all folders and file names
allWords = re.findall('[a-z].*',pathStr)
# Find all linebreaks
allLineBrks = re.findall('\n.*\t',pathStr)
pathArr = []
# Basically, split the folder and filenames from the linebreaks and tabs
for j in range(0,len(allWords)+len(allLineBrks)):
    if j % 2 == 0:
        pathArr.append(allWords[0])
        allWords.remove(allWords[0])
    else:
        pathArr.append(allLineBrks[0])
        allLineBrks.remove(allLineBrks[0])    

mainPathDict(pathArr[1:])