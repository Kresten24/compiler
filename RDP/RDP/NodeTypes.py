from ast import Node

class StartNode(Node):
    def __init__(self, data=None):
        super().__init__(data)


class EsNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.name = 'EsNode'
    pass

class TsNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.name = 'TsNode'
    pass

class FsNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.name = 'FsNode'
    pass

class ExsNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.name = 'ExsNode'
        pass

class TxsNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.name = 'TxsNode'
        pass
