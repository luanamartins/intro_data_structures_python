# Adicione na classe MyLinkedList, um método que retorne a quantidade de elementos na lista.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, value):
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value)
        self.length += 1

    def count(self):
        return self.length




myList = MyLinkedList()
myList.add(2)
myList.add(3)
print(myList.count())

myList.add(4)
myList.add(3)
print(myList.count())

myList.add(7)
print(myList.count())