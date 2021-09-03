# You are writing an AI for a 2D map game. You are somewhere in a 2D grid, and there are coins strewn 
# about over the map.

# Given the position of all the coins and your current position, find the closest coin to you in terms of 
# Manhattan distance. That is, you can move around up, down, left, and right, but not diagonally. If there 
# are multiple possible closest coins, return any of them.

# For example, given the following map, where you are x, coins are o, and empty spaces are . 
# (top left is 0, 0):

# ---------------------
# | . | . | x | . | o |
# ---------------------
# | o | . | . | . | . |
# ---------------------
# | o | . | . | . | o |
# ---------------------
# | . | . | o | . | . |
# ---------------------
# return (0, 4), since that coin is closest. This map would be represented in our question as:

# Our position: (0, 2)
# Coins: [(0, 4), (1, 0), (2, 0), (3, 2)]

def getManDistance(coord1,coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def getMinManDistanceCoordinate(ourCoord,coinsCoords):
    minManDist, minDisCoord = None, None
    for coord in coinsCoords:
        manDist = getManDistance(coord, ourCoord)
        if minManDist is None or manDist < minManDist:
            minManDist, minDisCoord = manDist, coord
    return minManDist, minDisCoord

ourCoord = (0, 2)
coinsCoords = [(1, 1), (1, 4), (0, 4), (1, 0), (2, 0), (3, 2)]

minManDist, minDisCoord = getMinManDistanceCoordinate(ourCoord, coinsCoords)
print("Having our coordinate:", ourCoord)
print("Among all the coins coordinates:", coinsCoords)
print("The closest to our coordinate is:", minDisCoord)
print("With a Manhattan distance of:", minManDist)