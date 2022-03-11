class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev.val

def reverse_list_recur(head, prev = None):
    if not head:
        return prev
    next = head.next
    head.next = prev    
    return reverse_list(next, head)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print(reverse_list(a))