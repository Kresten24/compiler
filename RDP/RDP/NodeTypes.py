from ast import Node

class StartNode(Node):
    def __init__(self, prog=None):
        super().__init__()


class EsNode(Node):
    def __init__(self, prog=None):
        super().__init__()
        self.name = 'EsNode'
    pass

class TsNode(Node):
    def __init__(self, prog=None):
        super().__init__()
        self.name = 'TsNode'
    pass

class FsNode(Node):
    def __init__(self, prog=None):
        super().__init__()
        self.name = 'FsNode'
    pass

class ExsNode(Node):
    def __init__(self, prog=None):
        super().__init__()
        self.name = 'ExsNode'
        pass

class TxsNode(Node):
    def __init__(self, prog=None):
        super().__init__()
        self.name = 'TxsNode'
        pass
