class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value)


myList = MyLinkedList()
myList.add(2)
myList.add(3)
