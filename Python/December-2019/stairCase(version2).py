# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement
# a method to count how many possible ways the child can run up the stairs.


def countWaysToClimbStairs(nStairs):
    return climbStair(nStairs, 0)


def climbStair(nStairs, nSteps):
    if nSteps == nStairs:
        return 1
    if nSteps > nStairs:
        return 0
    return climbStair(nStairs, nSteps + 1) + climbStair(nStairs, nSteps + 2) + climbStair(nStairs, nSteps + 3)


stairs = 4
print(countWaysToClimbStairs(stairs))
