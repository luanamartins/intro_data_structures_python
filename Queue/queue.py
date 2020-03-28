class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
    
    def print(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
        

q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print()
