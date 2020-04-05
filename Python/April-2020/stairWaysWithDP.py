# You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how
# many distinct ways you can climb to the top of the staircase.


def countWays(n):
    if n <= 2:
        return n
    ways = [0 for _ in range(n)]
    ways[0], ways[1] = 1, 1
    for i in range(2, n):
        currIndx = 1
        while currIndx <= 2 and currIndx <= i:
            ways[i] += ways[i - currIndx]
            currIndx += 1
    print(ways)
    return ways[n - 1]


def climbingStairs(n):
    if n <= 2:
        return n
    return countWays(n + 1)


assert climbingStairs(5) == 8
