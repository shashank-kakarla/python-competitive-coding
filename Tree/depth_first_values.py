class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        
        
def depth_first_values(node):
    stac = [node]
    while stac:
        current = stac.pop()
        print(current.val,end="->")
        if current.right != None:
            stac.append(current.right)
        if current.left != None:
            stac.append(current.left)
            
def dfv_rec(node):
    if not node:
        return []
    
    left_val = dfv_rec(node.left)
    right_val = dfv_rec(node.right)
    
    return [node.val, *left_val, *right_val]
                    
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
print(dfv_rec(a))