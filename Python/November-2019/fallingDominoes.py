# Given a string with the initial condition of dominoes, where:
#
# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side
#
# Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force
# cancels out and that domino remains upright.
#
# Example:
# Input:  ..R...L..R.
# Output: ..RR.LL..RR


def reArrangeDominoes(domList):
    print("original list")
    print(domList)
    weight = [0 for _ in range(len(domList))]

    # Calculate weight from left to right
    acumWeight = 0
    for i in range(len(domList)):
        if domList[i] == '.':
            if acumWeight:
                acumWeight -= 1
                weight[i] = acumWeight
        elif domList[i] == 'R':
            acumWeight = len(domList)
            weight[i] = acumWeight
        elif domList[i] == 'L':
            acumWeight = 0

    # Calculate weight from right to left
    acumWeight = 0
    for i in range(len(domList)):
        if domList[::-1][i] == '.':
            if acumWeight:
                acumWeight += 1
                weight[len(domList) - 1 - i] += acumWeight
        elif domList[::-1][i] == 'L':
            acumWeight = -1 * len(domList)
            weight[len(domList) - 1 - i] += acumWeight
        elif domList[::-1][i] == 'R':
            acumWeight = 0

    # Determine result
    for i in range(len(domList)):
        if weight[i] == 0:
            domList[i] = '.'
        elif weight[i] > 0:
            domList[i] = 'R'
        elif weight[i] < 0:
            domList[i] = 'L'

    print(weight)

    return domList


print(reArrangeDominoes(list("R.R...L...R...L.R..L")))
