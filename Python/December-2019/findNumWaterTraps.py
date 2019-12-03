# You have a landscape, in which puddles can form. You are given an array of non-negative integers representing
# the elevation at each location. Return the amount of water that would accumulate if it rains.
#
# For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
#        X
#    X███XX█X
#  X█XX█XXXXXX
# # [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def getNumOfTrapsInPuddle(puddle):
    innerTraps = puddle[1:len(puddle) - 1]
    difBetweenExtremes = abs(puddle[0] - puddle[-1])
    maxBorder = max(puddle[0], puddle[-1])
    numOfTraps = sum([((maxBorder - n) - difBetweenExtremes) for n in innerTraps])
    return numOfTraps


def findTotalNumOfTraps(landscape, currentPuddleIndex, totalWaterTraps):
    if currentPuddleIndex + 1 < len(landscape):
        currentPuddleEnd = currentPuddleIndex + 1
        currentPuddle = [landscape[currentPuddleIndex]]
        # Conform the current puddle
        while currentPuddleEnd < len(landscape):
            if landscape[currentPuddleEnd] >= currentPuddle[0] and len(currentPuddle) > 1:
                currentPuddle.append(landscape[currentPuddleEnd])
                break
            elif landscape[currentPuddleEnd] < currentPuddle[0]:
                currentPuddle.append(landscape[currentPuddleEnd])
                currentPuddleEnd += 1
            else:
                break
        # Add total number of water traps in case current puddle is at least 3 points large
        if len(currentPuddle) >= 3:
            # Avoid malformed puddles
            if currentPuddle[-1] < currentPuddle[-2]:
                del currentPuddle[-1]
            print("Current puddle", currentPuddle)
            totalWaterTraps += getNumOfTrapsInPuddle(currentPuddle)
        totalWaterTraps = findTotalNumOfTraps(landscape, currentPuddleEnd, totalWaterTraps)
    return totalWaterTraps


print(findTotalNumOfTraps([1, 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 0, 0))
