# There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with
# the kth person, and removing every successive kth person going clockwise until there is no one left.
#
# Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.
#
# For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.
#
# Bonus: Find an O(log N) solution if k = 2.


def findExecutionsOrder(prisoners, k):
    executions = []
    ptrPrisoner = k
    currExec = k + 1
    lenPris = len(prisoners)
    while len(executions) < lenPris:
        while currExec < k + 1:
            ptrPrisoner += 1
            if ptrPrisoner >= len(prisoners):
                ptrPrisoner = 0
            if prisoners[ptrPrisoner] not in executions:
                currExec += 1
        currPris = prisoners[ptrPrisoner]
        currExec = 0
        executions += [currPris]
    return executions, executions[-1]


N = 6
k = 3
print(findExecutionsOrder(range(1, N + 1), k - 1))
