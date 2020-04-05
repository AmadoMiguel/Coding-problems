# Given a list of undirected edges which represents a graph, find out the number of connected components.


def findNumConnectedComponents(edges):
    comps = []
    # Each edge is represented as a tuple with 2 values
    for e in edges:
        placed = False
        for c in comps:
            if e[0] in c and e[1] not in c:
                c.append(e[1])
                placed = True
                break
            elif e[0] not in c and e[1] in c:
                c.append(e[0])
                placed = True
                break
            elif e[0] in c and e[1] in c:
                placed = True
                break
        if not placed:
            comps.append([e[0], e[1]])
    print(comps)
    return len(comps)


graph = [(1, 2), (2, 3), (4, 1), (5, 6), (6, 7), (8, 5)]
assert findNumConnectedComponents(graph) == 2  # True
