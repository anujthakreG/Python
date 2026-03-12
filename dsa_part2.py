# Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
a = Node(5)
b = Node(2)
c = Node(1)
a.next = b
b.next = c

head = a
# 1st way of printing 
print(head.data)
print(head.next.data)

print("\n")
# 2nd way of printing (Traversing)
print("2nd way of printing the Linked_List :- ")
def printLinkedList(head):
    curr  = head
    while curr.next != None:
      print(curr.data, end =" ")
      curr = curr.next
printLinkedList(head)
print(" \n ")

# Insertion at the end
print("Insertion at the end")
NewNode = Node(1)
curr  = head
while curr.next != None:
    print(curr.data, end =" ")
    curr = curr.next

curr.next = NewNode
printLinkedList(head)

#Insertion at the front 
print("\nInsertion at the front ")
NewNode2 = Node(0)
curr = head
head = NewNode2 
head.next = curr
printLinkedList(head)

# Insertion at the kth index
