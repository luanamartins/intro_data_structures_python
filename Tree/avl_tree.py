class AVLTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, value):
        if (self.data > value):
            if (self.left == None):
                self.left = Tree(value)
            else:
                self.left.add(value)
        
        elif (self.data < value):
            if (self.right == None):
                self.right = Tree(value)
            else:
                self.right.add(value)

    def remove(self, value):
        print('todo')
