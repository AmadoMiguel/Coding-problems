# Given an undirected graph, determine if a cycle exists in the graph.


def findCycleInGraph(graph, cycleFound):
    print("Current graph", graph)
    # Loop over its keys
    for k in graph.keys():
        if graph[k] == graph:
            print("Found Cycle!", graph[k])
            cycleFound = True
        else:  # Recurse
            cycleFound = findCycleInGraph(graph[k], cycleFound)
    return cycleFound


graph = {
    'a': {
        'a2': {}, 'a3': {}
    },
    'b': {'b2': {}},
    'c': {}
}
graph['c'] = graph

print(findCycleInGraph(graph, False))
