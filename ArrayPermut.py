# PRACTICE RECURSION ALGORITHMS

def permutations(lists, i):
    if i == len(lists):
        return [[]]

    res_next = permutations(lists, i+1)
    res = []
    
    for n in lists[i]:
        print(n)
        for l in res_next:
            # Conforms a list with each element
            res.append([n] + l)
    return res            

def permutations_of_lists(lists):
    return permutations(lists,0)

pLsts = permutations_of_lists( [[1, 2, 3], [4], [5, 6]] )
print(pLsts)