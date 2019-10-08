# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one.
# Find the minimal number of moves required to obtain a strictly increasing sequence from the input.


def arrayChange(inputArray):
    minNumMoves = 0
    index = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[index]:
            minNumMoves += (inputArray[index]+1) - inputArray[i]
            inputArray[i] = (inputArray[index]+1)
        index += 1
    return minNumMoves


print(arrayChange([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]))
