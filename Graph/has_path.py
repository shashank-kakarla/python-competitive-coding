def has_path_dft(graph, src, dest):
    stac = [src]
    while len(stac)>0:
        for i in graph[stac.pop()]:
            if i == dest:
                return True
            else:
                stac.append(i)
    return False
  
def has_path_bft(graph, src, dest):
    stac = [src]
    while len(stac)>0:
      for i in graph[stac.pop(0)]:
        if i == dest:
          return True
        else:
          stac.append(i)
    return False
  
def has_path(graph,src,dest):
    if src == dest:
      return True
    for i in graph[src]:
      if has_path(graph,i,dest):
        return True
    return False

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path_bft(graph, 'f', 'k'))