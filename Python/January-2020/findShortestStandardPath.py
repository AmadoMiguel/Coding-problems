# Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.
#
# For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

from collections import deque


def findShortestStandardPath(path):
    # ./ means that is going to access a directory within current directory
    # ../ means that is going to go back to parent directory from current directory
    dirstHistory = []
    for dir in path.split("/"):
        # Stays in same directory
        if dir != ".":
            # Goes back to parent directory
            if dir == "..":
                dirstHistory.pop()
                continue
            # Goes to child directory
            dirstHistory.append(dir)
    return "/".join(dirstHistory)


print(findShortestStandardPath("/usr/bin/../bin/./scripts/../"))
