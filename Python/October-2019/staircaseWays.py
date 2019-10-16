# You are given a positive integer N which represents the number of steps in a staircase.
# You can either climb 1 or 2 steps at a time. Write a function that returns the number of
# unique ways to climb the stairs.


def waysOfClimbingStaircase(n):
    return findClimbWay(n, 0, 0)


def findClimbWay(n, currSteps, nWays):
    options = [1, 2]
    if currSteps == n:
        nWays += 1
    if currSteps < n:
        for o in options:
            if currSteps + o <= n:
                nWays = findClimbWay(n, currSteps + o, nWays)
            else:
                continue
    return nWays


print(waysOfClimbingStaircase(5))
