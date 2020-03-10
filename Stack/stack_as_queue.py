# Implemente uma nova classe que simule uma pilha usando apenas duas filas.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def enqueue(self, value):
        if (self.head): # queue is not empty
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode 
        else: # queue is empty
            self.head = Node(value)
            self.tail = self.head
    
    def dequeue(self):
        if (self.head):
            toRemove = self.head.data
            self.head = self.head.next
            return toRemove
        else:
            return -1
    
    def is_empty(self):
        return self.head is None

class MyStack:
    def __init__(self):
        self.q1 = MyQueue()
        self.q2 = MyQueue()

    def push(self, value):
        self.q2.enqueue(value)

        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

    def pop(self):
        if self.q1.is_empty():
            return -1
        
        return self.q1.dequeue()

st = MyStack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)

print(st.pop())
print(st.pop())
print(st.pop())