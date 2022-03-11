from collections import defaultdict

def shortest_path_1(edges, src, dest):
    visited = set()
    smallest = 99999
    graph = generate_graph(edges)
    #while len(visited) < len(graph):
    size = search_dest_1(graph, src, dest, visited)
    smallest = size if size < smallest else smallest
    return smallest
    

def search_dest_1(graph, src, dest, visited):
    if src in visited:
        return 0
    
    visited.add(src)
    size = 1
    for i in graph[src]:
        if i == dest:
            return size
        else:
            size+=search_dest_1(graph,i,dest,visited)
    return size

def shortest_path(edges, src, dest):
    graph = generate_graph(edges)
    visited = {src}
    dist = 0
    que = [(src,dist)]
    
    while que:
        current, dist = que.pop(0)
        if current == dest:
            return dist
        for node in graph[current]:
            if node not in visited:
                visited.add(node)
                que.append([node,dist+1])
    return -1
            
def generate_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        a,b = edge[0],edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph

edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

print(shortest_path(edges, 'a', 'e'))