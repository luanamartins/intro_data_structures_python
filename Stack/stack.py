class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        newNode = Node(value)
        
        if (self.top):
            newNode.next = self.top
        
        self.top = newNode

    def pop(self):
        if (self.top):
            toRemove = self.top.data
            self.top = self.top.next
            return toRemove
        else:
            return -1
    
    def print(self):
        current = self.top
        while (current):
            print(current.data)
            current = current.next


s = MyStack()
s.push(1)
s.push(2)
s.push(3)
s.print()
