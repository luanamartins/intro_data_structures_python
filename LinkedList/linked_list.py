class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value)


myList = MyLinkedList()
myList.add(2)
myList.add(3)
myList.add(4)
myList.add(3)
myList.add(7)

