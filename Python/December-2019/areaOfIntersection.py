# Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect,
# return 0.
#
# For example, given the following rectangles:
#
# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3) # width, height
# }
# and
#
# {
#     "top_left": (0, 5),
#     "dimensions": (4, 3) # width, height
# }
# return 6.


def calculateIntersectionBetweenRectangles(rect1, rect2):
    rect1LeftBorder = list(range(rect1["top_left"][1] - rect1["dimensions"][1], rect1["top_left"][1]))
    rect1DownBorder = list(range(rect1["top_left"][0], rect1["top_left"][0] + rect1["dimensions"][0]))

    rect2LeftBorder = list(range(rect2["top_left"][1] - rect2["dimensions"][1], rect2["top_left"][1]))
    rect2DownBorder = list(range(rect2["top_left"][0], rect2["top_left"][0] + rect2["dimensions"][0]))

    print("Rec1 dimensions", rect1DownBorder, rect1LeftBorder)
    print("Rec2 dimensions", rect2DownBorder, rect2LeftBorder)

    vertIntersec = len([n for n in rect2LeftBorder if n in rect1LeftBorder])
    horiIntersec = len([n for n in rect2DownBorder if n in rect1DownBorder])

    return vertIntersec * horiIntersec

rectangles = [
    {
        "top_left": (0, 5),
        "dimensions": (4, 3)  # width, height
    },
    {
        "top_left": (1, 4),
        "dimensions": (3, 3)  # width, height
    }
]


print(calculateIntersectionBetweenRectangles(rectangles[0], rectangles[1]))
