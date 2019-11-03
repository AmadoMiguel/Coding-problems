# Find the nearest K points to the given central point from the given list of points


def findNearestKPoints(points, centralPoint, k):
    return findNearestPoint(points, centralPoint, [], k)


# Used for recursion
def findNearestPoint(points, centralPoint, nearestPoints, k):
    print(points, "Closest point(s)", nearestPoints)
    # Exit recursion condition
    if len(nearestPoints) < k:
        closestDistance = None
        closestPoint = None
        for p in points:
            # Get distance between current point and central point
            currDistance = abs(p[0] - centralPoint[0]) + abs(p[1] - centralPoint[1])
            if closestDistance is None or currDistance < closestDistance:
                closestDistance = currDistance
                closestPoint = p
        # Add the current closest point to the list
        nearestPoints.append(closestPoint)
        # Remove if from the points list
        points.remove(closestPoint)
        # Recurse
        nearestPoints = findNearestPoint(points, centralPoint, nearestPoints, k)

    return nearestPoints


print(findNearestKPoints([(0, 0), (5, 4), (3, 1), (1, 1), (0, 3)], (1, 2), 3))
