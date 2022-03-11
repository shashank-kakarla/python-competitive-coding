from queue import Empty


def dft(graph, node):
    stac = [node]
    
    while len(stac)>0:
        node = stac.pop()
        print(node,end="->")
        for i in graph[node]:
            stac.append(i)

def dft_rec(graph,node):
    print(node,end="->")
    for i in graph[node]:
        dft_rec(graph, i)

graph_1 = {'a': ['b','c'],
         'b':['d'],
         'c':['e'],
         'd':['f'],
         'e':[],
         'f':[],
         }

dft_rec(graph_1, 'a')