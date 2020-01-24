# You are given two strings, A and B. Return whether A can be shifted some number of times to get B.
# #
# # Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and
# # B= acb should return false.


def shiftString(string):
    return string[1:] + string[0]


def isStringShifted(original, shifted):
    # The number of shifts should be less than len(shifted) to determine if is shifted respect to the original or not
    numShifts = 0
    while numShifts <= len(shifted):
        if original == shifted:
            return True
        shifted = shiftString(shifted)
        numShifts += 1
        print(shifted)
    return False


print(isStringShifted("abcde", "cdeab"))

