def connected_components_1(graph):
    comp = 0
    visited = set()
    
    for i in graph.keys():
        if i not in visited:
            visited.add(i)
            visited = dft_1(graph, i, visited)
            comp+=1     
    return comp

def dft_1(graph, node, visited):
    for i in graph[node]:
        if i not in visited:
            visited.add(i)
            visited = dft_1(graph, i, visited)
    return visited

def connected_components(graph):
    comp = 0
    visited = set()
    
    for i in graph.keys():
        if(explore(graph, i, visited)):
            comp+=1     
    return comp

def explore(graph, node, visited):
    if node in visited:
        return False
    
    visited.add(node)
    for i in graph[node]:
        explore(graph, i, visited)
    return True

graph = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}

print(connected_components(graph))