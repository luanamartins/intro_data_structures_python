#Extenda a classe MyQueue, adicione um novo método chamado “count”. 
# Ele não recebe argumentos, mas retorna o número de itens existentes na fila. 
# (Não é permitido usar laços nesse novo método!)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def enqueue(self, value):
        if (self.head): # queue is not empty
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode 
        else: # queue is empty
            self.head = Node(value)
            self.tail = self.head
        self.length += 1
    
    def dequeue(self):
        if (self.head):
            toRemove = self.head.data
            self.head = self.head.next
            self.length -= 1
            return toRemove
        else:
            return -1
    
    def print(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def count(self):
        return self.length
        

q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.count())
