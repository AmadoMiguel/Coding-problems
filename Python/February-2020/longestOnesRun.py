# Return the longest run of 1s for a given integer n's binary representation.
#
# Example:
# Input: 242
# Output: 4
# 242 in binary is 0b11110010, so the longest run of 1 is 4.


def getLongestOnesRun(num):
    binRep = bin(num)[2:]
    currRun, longestRun = 0, None
    for d in binRep:
        if d == "1":
            currRun += 1
        else:
            currRun = 0
        if longestRun is None or currRun > longestRun:
            longestRun = currRun
    return longestRun


assert getLongestOnesRun(242) == 4  # Pass
