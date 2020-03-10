# Adicione na lista encadeada um método chamado count, 
# que retorna quantas vezes um número (passado como argumento) existe na lista, 
# se tal elemento não existir na lista, retorne 0


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

    def count(self, value):
        current = self.head

        result = 0
        while(current):
            if (current.data == value):
                result += 1
            current = current.next
        return result


myList = MyLinkedList()
myList.add(2)
myList.add(3)
myList.add(2)
myList.add(5)
myList.add(7)
myList.add(2)

print(myList.count(4))
