from cgitb import reset


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
def tree_path(node):
    if not node:
        return []
    stack = [(node,"")]
    result = []
    
    while stack:
        current, ls = stack.pop()
        if not current.left and not current.right:
            result.append(ls+str(current.val))
        if current.right:
            stack.append((current.right,ls+str(current.val)+"->"))
        if current.left:
            stack.append((current.left,ls+str(current.val)+"->"))
            
    return result

a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

print(tree_path(a))