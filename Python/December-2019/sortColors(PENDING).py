# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
# adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library’s sort function for this problem.
#
# Can you do this in a single pass?
#
# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


def sortColors(colors):
    for i in range(len(colors)):
        indexOfCurrMin = i
        for j in range(i + 1, len(colors)):
            if colors[j] < colors[indexOfCurrMin]:
                indexOfCurrMin = j
        temp = colors[i]
        colors[i] = colors[indexOfCurrMin]
        colors[indexOfCurrMin] = temp


cols = [2, 0, 2, 1, 1, 0, 1, 0, 2, 0, 1, 1, 2, 2, 0, 0, 1, 0, 2, 1, 0, 1, 0]
sortColors(cols)
print(cols)
