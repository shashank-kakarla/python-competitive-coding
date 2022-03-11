class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.random = None
        
def copyRandomList(head1):
    if not head1:
        return None
    current = head1
    copy = {None:None}
    
    while current:
        copy[current] =  Node(current.val)
        current = current.next
    
    current = head1
    while  current:
        copy[current].next = copy[current.next]
        copy[current].random = copy[current.random]  
        current = current.next
    return print_list(copy[head1])

def print_list(head1):
    while head1:
        print(head1.val,end="->")
        head1 = head1.next

def check_list(head1, head2):
    while head1 and head2:
        return head1 == head2 and check_list(head1.next, head2.next)
    

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

a.random = c
b.random = a
c.random = None
d.random = f
e.random = f
f.random = a

print(copyRandomList(a))





