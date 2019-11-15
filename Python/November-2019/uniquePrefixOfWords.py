# Given a list of words, return the shortest unique prefix of each word. For example, given the list:
#
# dog
# cat
# apple
# apricot
# fish
# Return the list:
#
# d
# c
# app
# apr
# f


def findSmallestUniquePrefixesOfWords(words):
    prefixes = set()
    for w in words:
        wAsList = list(w)
        currentPrefix = wAsList[0]
        indexOfPrefix = 0
        while any(wo.startswith(currentPrefix) for wo in words if wo != w):
            if indexOfPrefix < len(wAsList) - 1:
                indexOfPrefix += 1
                currentPrefix += wAsList[indexOfPrefix]
            else:
                break
        prefixes.add(currentPrefix)
    return prefixes


print(findSmallestUniquePrefixesOfWords(['dog', 'cat', 'apple', 'apricot', 'fish', 'app', 'word', 'day', 'car',
                                         'fight', 'book', 'dessert', 'day', 'seek', 'sea', 'peer']))
