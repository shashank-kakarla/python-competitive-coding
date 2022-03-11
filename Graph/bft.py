def bft(graph, node):
    que = [node]
    
    while len(que)>0:
        current = que.pop(0)
        print(current,end="->")
        for i in graph[current]:
            que.append(i)

graph_1 = {'a': ['b','c'],
         'b':['d'],
         'c':['e'],
         'd':['f'],
         'e':[],
         'f':[],
         }

bft(graph_1, 'a')