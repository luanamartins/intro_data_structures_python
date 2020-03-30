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

    # Depth First Search
    def dfs(self):
        result = [self.data]

        if self.left:
            result.extend(self.left.dfs())
        
        if self.right:
            result.extend(self.right.dfs())

        return result

    # Breadth First Search
    def bfs(self):
        result = []
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            result.append(current.data)

            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
        
        return result


tree = Tree(5)
tree.add(1)
tree.add(8)
tree.add(10)
print(tree.bfs())