class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
def max_path_sum(node):
    if not node:
        return -9999
    if not node.left and not node.right:
        return node.val
    sum = max(node.val+max_path_sum(node.left),node.val+max_path_sum(node.right))
    return sum

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

print(max_path_sum(a))