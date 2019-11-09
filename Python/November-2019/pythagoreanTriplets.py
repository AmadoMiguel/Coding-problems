# Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3
# variables a, b, c where a^2 + b^2 = c^2
#
# Example:
# Input: [3, 5, 12, 5, 13]
# Output: True
# Here, 5^2 + 12^2 = 13^2.

from itertools import permutations


def findPythagoreanTriplets(numsList):
    pythagoreanTriplets = set()
    # Find permutations of indexes triplets in order to check all combinations
    indexesPermuts = permutations(range(len(numsList)), 3)
    for p in indexesPermuts:
        # Get current triplet
        (a, b, c) = (numsList[p[0]], numsList[p[1]], numsList[p[2]])
        # Find out if is pythagorean
        if a**2 + b**2 == c**2:
            pythagoreanTriplets.add((a, b, c))
    return pythagoreanTriplets


print(findPythagoreanTriplets([3, 5, 12, 5, 13, 5, 0]))

