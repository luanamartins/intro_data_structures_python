# Adicione um novo método chamado “isEmpty” em MyStack, que retorne se a pilha está vazia ou não.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

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

    def is_empty(self):
        return self.top is None


s = MyStack()
print(s.is_empty())
s.push(10)
print(s.is_empty())
