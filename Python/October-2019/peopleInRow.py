# There are n people lined up, and each person's height is represented as an integer. A show is going on
# right in front of them, and only people who are taller than everyone in front of them are able to see it.
# How many people can see the show?
# Example:
# Input: [1, 4, 2, 3, 6, 3]
# Output: 3
# Explanation: Only [6, 4, 1] were able to see in front of them.


def peopleInRow(peopleHeights):
    return whoCanSeeTheShow(peopleHeights, 1, [peopleHeights[0]])


def whoCanSeeTheShow(heights, currentPerson, peopleWhoSeeTheShow):
    if currentPerson < len(heights):
        if heights[currentPerson] > max(heights[:currentPerson]):
            peopleWhoSeeTheShow.append(heights[currentPerson])
        peopleWhoSeeTheShow = whoCanSeeTheShow(heights, currentPerson + 1, peopleWhoSeeTheShow)
    return peopleWhoSeeTheShow


print(peopleInRow([1, 4, 2, 3, 6, 3, 2, 5, 7, 5, 2, 3, 4, 9]))
