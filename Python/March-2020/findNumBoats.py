# An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat, and
# the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.
#
# For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats
# required will be three.


def findNumBoats(weights, k):
    boats = []
    boatsEmpty = True
    for w in weights:
        placedPerson = False
        if boatsEmpty:
            boats += [w]
            boats = False
        else:
            indx = 0
            while indx < len(boats):
                if w + boats[indx] <= k:
                    boats[indx] += w
                    placedPerson = True
                    break
                indx += 1
            if not placedPerson:
                boats += [w]
    return len(boats)


peopleWeights = [100, 200, 150, 80]
findNumBoats(peopleWeights, 200)
