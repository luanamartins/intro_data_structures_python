class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Tree:
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

    def dfs(self):
        result = [self.data]

        if (self.left):
            result.extend(self.left.dfs())
        
        if (self.right):
            result.extend(self.right.dfs())

        return result


tree = Tree(5)
tree.add(10)
tree.add(1)
print(tree.dfs())