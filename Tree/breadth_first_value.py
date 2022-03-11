class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def breadth_first_values(node):
    que = [node]
    result = []
    while que:
        current = que.pop(0)
        if current:
            result.append(current.val)
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)
    return result        
        
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#depth_first_values(a)
print(breadth_first_values(a)) 