# You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN) representing a polygon.
# You can assume these points are given in order; that is, you can construct the polygon by connecting
# point 1 to point 2, point 2 to point 3, and so on, finally looping around to connect point N to point 1.
#
# Determine if a new point p lies inside this polygon. (If p is on the boundary of the polygon,
# you should return False).


# O(N ^ 2) implementation
# For each pair of points, check if the point is inside bounds
def isPointInsidePolygon(points, pointToCheck):
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            currPoint1, currPoint2 = points[i], points[j]
            if currPoint1 < currPoint2:
                # For each coordinate x and y of the point to check, verify that is in
                # bounds respect to the two current polygon points
                for c in range(len(pointToCheck)):
                    if currPoint1[c] != currPoint2[c]:
                        if pointToCheck[c] < currPoint1[c] or pointToCheck[c] > currPoint2[c]:
                            return False
            else:
                for c in range(len(pointToCheck)):
                    if currPoint1[c] != currPoint2[c]:
                        if pointToCheck[c] < currPoint2[c] or pointToCheck[c] > currPoint1[c]:
                            return False
    # Default return
    return True


pts = [(4, 3), (2, 1), (2, 3)]
pt = (3, 3.1)
assert not isPointInsidePolygon(pts, pt)  # Pass
pt = (3, 2.5)
assert isPointInsidePolygon(pts, pt)  # Pass
pt = (2.3, 1.7)
assert isPointInsidePolygon(pts, pt)  # Pass
pt = (1.9, 2.9)
assert not isPointInsidePolygon(pts, pt)  # Pass
