# There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with
# the kth person, and removing every successive kth person going clockwise until there is no one left.
#
# Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.
#
# For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.
#
# Bonus: Find an O(log N) solution if k = 2.


def findLastExecutedPrisoner(prisoners, k):
    ptrExec = k
    while len(prisoners) > 1:
        print(prisoners)
        prisoners.pop(ptrExec)
        ptrExec += k
        if ptrExec >= len(prisoners):
            ptrExec = ptrExec - len(prisoners)
    # Last prisoner to be executed
    return prisoners


N = 5
k = 2
print(findLastExecutedPrisoner(list(range(1, N + 1)), k - 1))
