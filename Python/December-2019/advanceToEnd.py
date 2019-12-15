# You are given an array of non-negative integers. Let's say you start at the beginning of the array and are trying to
# advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can
# get to the end of the array.
#
# For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.
#
# Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.


def checkIfCanAdvanceToEnd(steps):
    if len(steps):
        currentPos = 0
        prevIndex = 0
        while currentPos < len(steps):
            print(currentPos)
            currentPos += steps[currentPos]
            while currentPos < len(steps) and steps[currentPos] == 0:  # Avoid falling into a 0
                currentPos -= 1
            if currentPos <= prevIndex:  # Couldn't advance anymore
                return False
            prevIndex = currentPos  # Take track of the previous index to see if there was advance at all
        return True


s = [1, 3, 1, 2, 0, 1]  # True
# s = [1, 3, 1, 2, 0, 1, 2, 0, 3, 0, 2, 0, 1]  # True
# s = [1, 2, 1, 0, 0]  # False

print(checkIfCanAdvanceToEnd(s))
