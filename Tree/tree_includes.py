class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_inludes(node, target):
    if not node:
        return False
    que = [node]
    
    while que:
        current = que.pop(0)
        if current.val == target:
            return True
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
    return False

def tree_includes_rec(node,target):
    if not node:
        return False
    if node.val == target:
        return True
    return tree_includes_rec(node.left,target) or tree_includes_rec(node.right,target)
    

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#print(tree_inludes(a,'z'))
print(tree_includes_rec(a,'f'))