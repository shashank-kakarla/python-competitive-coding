import tarfile


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def printList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
    
    def addNode(self, node):
        if self.head == None:
            self.head = node
            return
        last =  self.next
        while last.next:
            last = last.next
        last.next = node
            
    def addToList(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = node
        
def printList(head):
    while head:
        print(head.value)
        head = head.next

def mergeLinkedLists(headA,headB):
    temp = Node(0)
    tail = temp
    a = headA.head
    b = headB.head
    
    while a is not None and b is not None:
        if a.value < b.value:
            tail.next =  a
            a = a.next
        elif b.value <= a.value:
            tail.next = b
            b = b.next
        tail = tail.next
            
    while a is not None:
        tail.next = a
        a = a.next
        tail = tail.next
        
    while b is not None:
        tail.next = b
        b = b.next
        tail = tail.next

    
    temp = temp.next
    while temp:
        print(temp.value,end="->")
        temp = temp.next

listA = LinkedList()
listA.addToList(1)
listA.addToList(5)
listA.addToList(13)
listA.addToList(18)

listB = LinkedList()
listB.addToList(2)
listB.addToList(8)
listB.addToList(11)
listB.addToList(19)


mergeLinkedLists(listA, listB)

    
        