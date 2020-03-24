# Suppose we represent our file system as a string. For example, the string
# "user\n\tpictures\n\tdocuments\n\t\tnotes.txt" represents:
#
# user
#     pictures
#     documents
#         notes.txt
# The directory user contains an empty sub-directory pictures and a sub-directory documents containing a file notes.txt.
#
# The string "user\n\tpictures\n\t\tphoto.png\n\t\tcamera\n\tdocuments\n\t\tlectures\n\t\t\tnotes.txt" represents:
#
# user
#     pictures
#         photo.png
#         camera
#     documents
#         lectures
#             notes.txt
# The directory user contains two sub-directories pictures and documents. pictures contains a file photo.png and an
# empty second-level sub-directory camera. documents contains a second-level sub-directory lectures containing a
# file notes.txt.
#
# We want to find the longest (as determined by the number of characters) absolute path to a file within our system.
# For example, in the second example above, the longest absolute path is "user/documents/lectures/notes.txt", and its
# length is 33 (not including the double quotes).
#
# Given a string representing the file system in this format, return the length of the longest absolute path to a
# file in the abstracted file system. If there is not a file in the file system, return 0.
#
# Note: Due to system limitations, test cases use form feeds ('\f', ASCII code 12) instead of newline characters.


def isFile(name):
    if len(name):
        return name.find(".") != -1
    return False


def getLevelAndFilename(fileName):
    lvl, name = 0, ""
    for c in fileName:
        if c == "\t":
            lvl += 1
        else:
            break
    if lvl:
        name = fileName[lvl:]
    else:
        name = fileName
    return lvl, name


def longestPath(fileSystem):
    st = []
    longestPath = ""
    currPath = ""
    for name in fileSystem.split('\f'):
        lvl, fName = getLevelAndFilename(name)
        if not len(st):
            currPath += fName + "/"
            st.append((fName + "/", lvl))
        else:
            while st[-1][1] >= lvl:
                lastNameIndx = currPath.rfind(st[-1][0])
                currPath = currPath[:lastNameIndx]
                st.pop()
                if not len(st):
                    break
            st.append((fName + "/", lvl))
            currPath += fName + "/"
        if isFile(fName):
            if len(currPath) > len(longestPath):
                longestPath = currPath
    print(longestPath)
    if len(longestPath):
        return len(longestPath) - 1
    return 0


fileSystem = "user\f\tpictures\f\t\tphoto.png\f\t\tcamera\f\tdocuments\f\t\tlectures\f\t\t\tnotes.txt"
assert longestPath(fileSystem) == 33  # True
