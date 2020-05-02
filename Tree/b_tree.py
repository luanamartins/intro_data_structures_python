class BNode:
    def __init__(self, contents=[], children=[]):
        self.contents = contents
        self.children = children
    
    def add(self, data):
        self.contents.insert(data)
