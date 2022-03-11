class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def tree_sum(node):
    if not node:
        return
    que = [node]
    sum = 0
    while que:
        current = que.pop(0)
        sum += current.val
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
    
    return sum

def tree_sum_rec(node):
    if not node:
        return 0
    return node.val + tree_sum_rec(node.left) + tree_sum_rec(node.right)

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

print(tree_sum_rec(a))   