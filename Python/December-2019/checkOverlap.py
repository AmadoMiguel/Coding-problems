# You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether
# or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered
# overlapping.
#
# For example, given the following rectangles:
#
# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3) # width, height
# },
# {
#     "top_left": (-1, 3),
#     "dimensions": (2, 1)
# },
# {
#     "top_left": (0, 5),
#     "dimensions": (4, 3)
# }
# return true as the first and third rectangle overlap each other.

from itertools import permutations


def checkIfRectanglesOverlap(rect1, rect2):
    rect1LeftBorder = list(range(rect1["top_left"][1] - rect1["dimensions"][1], rect1["top_left"][1]))
    rect1DownBorder = list(range(rect1["top_left"][0], rect1["top_left"][0] + rect1["dimensions"][0]))

    rect2LeftBorder = list(range(rect2["top_left"][1] - rect2["dimensions"][1], rect2["top_left"][1]))
    rect2DownBorder = list(range(rect2["top_left"][0], rect2["top_left"][0] + rect2["dimensions"][0]))

    vertInter = len([n for n in rect2LeftBorder if n in rect1LeftBorder])
    horiInter = len([n for n in rect2DownBorder if n in rect1DownBorder])

    return vertInter and horiInter


rectangles = [
    {
        "top_left": (1, 4),
        "dimensions": (3, 3)  # width, height
    },
    {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    },
    {
        "top_left": (0, 5),
        "dimensions": (4, 3)
    }
]

indecesPerms = permutations(range(len(rectangles)), 2)
isAnyOverlap = False
for p in indecesPerms:
    if checkIfRectanglesOverlap(rectangles[p[0]], rectangles[p[1]]):
        isAnyOverlap = True
        break
if isAnyOverlap:
    print("At least two rectangles overlap")
else:
    print("None of the rectangles overlap to each other")
