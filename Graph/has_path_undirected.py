from collections import defaultdict

def has_path_dft(graph, src, dest):
    visited = {src}
    stac = [src]
    while len(stac)>0:
        for i in graph[stac.pop()]:
            if i == dest:
                return True
            if i not in visited:
                visited.add(i)
                stac.append(i)
    return False

def has_path_rec(graph, src, dest, visited):
    if src == dest:
        return True
    
    if src not in visited:
        visited.add(src)    
        for i in graph[src]:
            if(has_path_rec(graph, i, dest, visited)):
                return True
    return False

def has_path_bft(graph, src, dest):
    visited = set()
    que = [src]
    while len(que)>0:
        for i in graph[que.pop(0)]:
            if i == dest:
                return True
            if i not in visited:
                visited.add(i)
                que.append(i)
    return False
            

def build_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]
print(build_graph(edges))
print(has_path_dft(build_graph(edges), 'i', 'm'))
print(has_path_rec(build_graph(edges), 'i', 'm',set()))
print(has_path_bft(build_graph(edges), 'i', 'm'))