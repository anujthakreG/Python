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
    curr = head
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
print("\nInsertion at the kth index")
k = 2
NewNode3 = Node(9)
curr = head
for i in range(k-1):
    curr = curr.next

NewNode3.next = curr.next.next
curr.next = NewNode3
# NewNode3.next = curr.next.next
printLinkedList(head)


# Deleteion at the kth index 
print("\n Deleteion at the kth index ")
k = 1 # [0,5,9,1] -> 5 removed 
curr = head
for i in range(k-1):
    curr = curr.next

curr.next = curr.next.next
printLinkedList(head)

"""
LEETCODE QUESTION PRACTICE :- 
876   -> floor division discards the decimal value and then return the value 
237
19
83
82
160 -> intersection of the linked list 
60 -> rotataion of the linked list
"""
### curr != None and curr.next != None  --> return different values 
# remove the kth node from the last -> fir (l-n+1)

"""
reversing the linked list 
"""
# curr = head
#         nxt = None
#         prev =None 
#         while curr != None :
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt             -> this are the four main pointers for it 


# ->  restarting on 29 Mar
print("\n rotating the Linked List ")
class Reverse :
    def rrll() :
        if head == None or head.next == None:
            return head
        
        last = head
        l = 0  # length of the linked list
        while last != None:
            last = last.next
            l+=1
        l+=1 # to also include the last node 
        k = k % l # k = 10 , l = 7 , k = 3 
        curr = head
        for i in range(l-k-1):
            curr = curr.next
        last.next = head
        head = curr.next
        curr.next = None

        return head
"""
class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        c = 0
        while True :
            if p1 == p2 :
                return p1
            p1 = p1.next
            p2 = p2.next

            
            if p1==None:
                c+=1
                p1 = headB
            if p2 == None :
                # c+=1
                p2 = headA

            if c>1 :
                return None
"""


"""
-----------------------------------------------------------------------------------------------------------------------------------
"""
# -----------------------------------------------------------------------------------------------------------------------------------
# Stack 
print("\n\t Stack !")
st = [] 
st.append(1)
st.append(2)
st.append(3)

print("Elements of the stack :- " ,st)
print(" after Poping Stack :- ")
st.pop()
print(st)
print("Now the top element is :- ")
print(st[-1])  # the top index

class Stack :
    def __init__(self):
        self.st = []

    def push(self,x):
        self.st.append(x)

    def pop(self):
        if len(self.st) == 0:
            return -1
        x = self.st[-1]
        st.pop
        return x
    def print(self):
        if len(self.st) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:", self.st)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print()


# Linked List implementation of Stack :
print("\nLinked List implementation of Stack :")
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack :
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self,x):
        self.length += 1
        if self.top is None:
            self.top = Node(x)
            return 
        else :
            NewNode = Node(x)
            NewNode.next = self.top
            self.top = NewNode

    def pop(self):
        if self.top is None:
            return -1
        self.length -= 1
        x = self.top.data
        self.top = self.top.next
        return x
    
    def getTop(self):
        if self.top is None:
            return -1
        return self.top.data
    
    def size(self):# if we will apply loop then the tc will be o(n)
        return self.length
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.size())
print(stack.pop())
print(stack.getTop())

#--------------------------------------------------------------------------------------------------------------------
print("\tQueue\n")

class Queue :
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self,x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)

    def pop(self):
        if len(self.st) == 0:
            return -1
        x = self.st[-1]
        st.pop
        return x
    def print(self):
        if len(self.st) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:", self.st)

#--------------------------------------------------------------------------------------------------------------------
#L linked List Implementation of Queue
# front :- elements are removed from here
# rear :- elements are pushed from here

print("\n linked List Implementation of Queue")
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue :
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def push(self,x):
        NewNode = Node(x)
        self.length+=1
        if self.front is None :
            self.front = NewNode
            self.rear = NewNode
        else :
            NewNode = Node(x)
            self.rear.next = NewNode
            self.rear = NewNode

    def pop(self):
        self.length-=1
        if self.front is None:
            return -1
        x = self.front.data
        self.front = self.front.next
        if self.front is None :
            self.rear = None 
        return x 
    
    def getFront(self):
        if self.front is None :
            return -1 
        x = self.front.data
        return x 
    
    def getSize(self):
        return self.length
  
q = Queue()
q.push(5)
q.push(4)
q.push(3)
q.push(1)


print(q.getFront())
q.pop()
print(q.getFront())
print(q.getSize())

# LC 232 Implementing Queue Using Stacks 



#--------------------------------------------------------------------------------------------------------------------
# Starting with Lecture 8-9-10
class Node :
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
root = Node(5)
root.left = Node(3)
root.right=  Node(1)
root.left.right = Node(8)

# types of binary tree :-
#  Full Bt :- 0 or 2 child , with imbalance leaf nodes 
# Complete Bt :- 0 or 2 Child with balanced Leaf nodes
#  perfect Binary tree :- 0 , 1 , 2 with imbalance Nodes 
# Degenrate Binary Tree :- 0 or 1 childern
# Skewed BT :- 0 or 1 Child ,all nodes either right or left side 
# Balanced Bt :- Node-> diff[len(left_subtree) - len(right_subtree)] <= 1 

#--------------------------------------------------
# Types of traversals : Pre,Post,Inorder Traversals achieved thru Recusion(stack), Level Order(Queue)

# 1> PreOrder Traversal -> root, Left_Subtree, Right_Subtree 