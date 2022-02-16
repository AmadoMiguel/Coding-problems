# Given a grid of Robot positions, indicate if it is a valid time series for the number of robots specified, if robots
# can only travel up to 1 index further than their position 1 step before.

# Input format: An array of arrays, of which each index can be 0 or 1. An index corresponds to the physical location,
# which is either occupied by a Robot (1) or empty (0)

# Time complexity: O(N*M), where N is the number of time series and M is each series length
# Space complexity: O(N), because the previous indexes of the robots are stored, as well as the current ones
def isTimeSeriesValid(robotsSeries, numRobots):
    # Assuming all of the series have the same length
    lenS = len(robotsSeries[0])
    prevIndx, currIndx, currBotIndx = [], [], 0
    for s in robotsSeries:
        # Reset variables for tracking the indexes of the Robot
        prevIndx = [] + currIndx
        currIndx = []
        currBotIndx = -1
        for i in range(lenS):
            # If is a Robot position
            if s[i]:
                currBotIndx += 1
                currIndx.append(i)
                try:
                    if abs(currIndx[currBotIndx] - prevIndx[currBotIndx]) > 1:
                        return False
                except IndexError:
                    pass
        # Number of 1s found should be same as numRobots
        if currBotIndx + 1 != numRobots:
            return False
    print(prevIndx, currIndx, currBotIndx)
    return True


# True
print(isTimeSeriesValid([[1, 0, 0, 0, 1],
                         [1, 0, 0, 1, 0],
                         [0, 1, 1, 0, 0],
                         [1, 0, 0, 1, 0],
                         [1, 0, 0, 0, 1],
                         [0, 1, 0, 1, 0],
                         [0, 0, 1, 0, 1]], 2))
