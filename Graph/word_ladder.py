from collections import defaultdict

def build_ladder(beginWord, endWord, wordList):
    graph = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            graph[word[:i]+"*"+word[i+1:]].append(word)
    print(bfs(beginWord,endWord,graph))
    
def bfs(beginWord, endWord, graph):
    que = [(beginWord,1)]
    visited = set()
    while que:
        current, step = que.pop(0)
        for i in range(len(beginWord)):
            inter_word = current[:i] + "*" + current[i+1:]
            for word in graph[inter_word]:
                if word == endWord:
                    return step+1
                if word not in visited:
                    visited.add(word)
                    que.append((word,step+1))
            graph[inter_word] = []
    return 0
    

build_ladder("hit","cog",["hot","dot","dog","lot","log","cog"])

