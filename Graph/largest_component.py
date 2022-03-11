def largest_component_1(graph):
    size = 0
    visited = set()
    
    for i in graph:
        prev = len(visited)
        explore_1(graph, i, visited)
        size = max(len(visited)-prev, size)
    return size

def explore_1(graph, node, visited):
    if node not in visited:
        visited.add(node)
        for i in graph[node]:
            explore(graph, i, visited)
            
def largest_component(graph):
    largest = 0
    visited = set()
    for node in graph:
        size = explore(graph, node, visited)
        largest = size if size > largest else largest
    return largest
    

def explore(graph, node, visited):
    if node in visited:
        return 0
    
    visited.add(node)
    size = 1
    for i in graph[node]:
        size+=explore(graph, i, visited)
    return size
    
def print_keys(graph):
    for node in graph:
        print(node)
    print(len(graph))

graph = {
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}

print(largest_component(graph))
#print_keys(graph)    