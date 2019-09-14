# Given a number in the form of a list of digits, return all possible permutations.

# Solution taken from https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

permutations = []

def permute(a, l, r):
    global permutations
    if l == r:
        permutations.append(a[:])
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]


l = [1, 2, 3, 4]
listLength = len(l)
permute(l, 0, listLength - 1)
print(permutations)
