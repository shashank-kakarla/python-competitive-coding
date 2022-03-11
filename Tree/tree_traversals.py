class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def inorder(node):
    if not node:
        return []
    
    left_val = inorder(node.left)
    right_val = inorder(node.right)
    
    return [*left_val, node.val, *right_val]

def preorder(node):
    if not node:
        return []
    left_val = preorder(node.left)
    right_val = preorder(node.right)
    
    return [node.val, *left_val, *right_val]

def postorder(node):
    if not node:
        return []
    left_val = postorder(node.left)
    right_val = postorder(node.right)
    
    return [*left_val, *right_val, node.val]

def level_order(node):
    if not node:
        return []
    
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
        
    

a = Node('1')
b = Node('2')
c = Node('3')
d = Node('4')
e = Node('5')
a.left = b
a.right = c
b.left = d
b.right = e

print(inorder(a))
print(preorder(a))
print(postorder(a))
print(level_order(a))