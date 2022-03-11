class Node:
    def __init__(self,val):
        self.val = val
        self.left =None
        self.right = None
        
def LCA(root, node1, node2):
    if root == node1 or root == node2:
        return root.val
    
    left = right = None
    if root.left:
        left = LCA(root.left,node1,node2)
    if root.right:
        right = LCA(root.right, node1, node2)
    if left and right:
        return root.val
    else:
        return left or right

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(LCA(a,d,e))