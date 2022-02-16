# Write a function fib(n) that takes in a number as an argument. The function should return the n-th number of
# the Fibonacci sequence

# If given a quite large input, it becomes an inefficient approach
# Time Complexity -> O(2^N) -> Inverse of the logarithmic time complexity
#   For each function call, there are 2 recursive calls to the function, which is repeated n times
# Space Complexity -> O(N)
def recurFib(n):
    if n <= 2:
        return 1
    return recurFib(n - 1) + recurFib(n - 2)

# Dynamic Programming: Pattern of overlapping subproblems. Any instance where there is a large problem, that can be
# decomposed into smaller instances of the same problem
#     Memoization: One of the overarching strategies that can be used to solve any DP problems
#       - Store results gotten in order to reutilize them instead of recalculate them
#       - For this particular implementation, use a hashmap (O(1)) in order to store previous solutions


# Time Complexity -> O(N)
# Space Complexity -> O(N)
def memoizationFib(n):
    fibDp = {}
    fibDp[1] = 1
    fibDp[2] = 1
    currPos = 3
    while currPos <= n:
        fibDp[currPos] = fibDp[currPos-1] + fibDp[currPos-2]
        currPos += 1
    return fibDp[n]


# print(recurFib(6))
# print(recurFib(7))
# print(recurFib(8))
# print(recurFib(50))

print(memoizationFib(6))
print(memoizationFib(7))
print(memoizationFib(8))
print(memoizationFib(50))
