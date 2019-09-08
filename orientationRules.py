# A rule looks like this:
#
# A NE B
#
# This means this means point A is located northeast of point B.
#
# A SW C
#
# means that point A is southwest of C.
#
# Given a list of rules, check if the sum of the rules validate

import re
import numpy as np

# Map to store each point with its assigned coordinate
pointsAndCoordinatesMap = {}


def assignCoordinates(firstPoint, secondPoint, coordinates):
    # Modify the global map in order to access its updated version in the other function
    global pointsAndCoordinatesMap
    if firstPoint not in pointsAndCoordinatesMap.keys():
        pointsAndCoordinatesMap[firstPoint] = np.array(coordinates)
    elif secondPoint not in pointsAndCoordinatesMap.keys():
        pointsAndCoordinatesMap[secondPoint] = np.subtract(pointsAndCoordinatesMap[firstPoint], coordinates)
    if secondPoint not in pointsAndCoordinatesMap.keys():
        pointsAndCoordinatesMap[secondPoint] = np.array([0, 0])


def validateOrientationRules(rules):
    global pointsAndCoordinatesMap

    # Iterate over the rules list
    for r in rules:
        # Extract the orientation letter(s)
        orientation = re.findall('\s(.*)\s',r)[0]
        # Extract the points
        firstPoint = r[0]
        secondPoint = r[-1]
        # Determine the coordinate for each one according to the orientation
        if orientation == "N":
            assignCoordinates(firstPoint, secondPoint, [0, 1])
        elif orientation == "E":
            assignCoordinates(firstPoint, secondPoint, [1, 0])
        elif orientation == "W":
            assignCoordinates(firstPoint, secondPoint, [-1, 0])
        elif orientation == "S":
            assignCoordinates(firstPoint, secondPoint, [0, -1])
        elif orientation == "NE":
            assignCoordinates(firstPoint, secondPoint, [1, 1])
        elif orientation == "NW":
            assignCoordinates(firstPoint, secondPoint, [-1, 1])
        elif orientation == "SE":
            assignCoordinates(firstPoint, secondPoint, [1, -1])
        elif orientation == "SW":
            assignCoordinates(firstPoint, secondPoint, [-1, -1])

listOfRules = ["A NW B", "A N B"]
validateOrientationRules(listOfRules)
print(pointsAndCoordinatesMap)
