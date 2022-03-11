class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def are_symm(root1, root2):
    if not root1 and not root2:
        return True
    elif ((not root1) != (not root2)) or root1.val != root2.val:
        return False
    else:
        return are_symm(root1.left,root2.right) and are_symm(root1.right, root2.left)

a = Node('a')
b = Node('b')
c = Node('b')
d = Node('c')
e = Node('c')
f = Node('c')
g = Node('c')
h = Node('d')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = h

def are_symm_trees(root):
    if not root:
        return
    return are_symm(root.left, root.right)

print(are_symm_trees(a))

