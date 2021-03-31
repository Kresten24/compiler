class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data
        if self.children is not None:
            for child in self.children:
                self.add_child(child)

    def __repr__(self):
        return self.data

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
