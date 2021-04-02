from c.ast import Node
from c.constants.terminals import TerminalEnum


class StartNode(Node):
    def __init__(self, prog=None):
        super().__init__()


class ProgNode(Node):
    def __init__(self, classDecl=None, funcDef=None, funcBody=None):
        super().__init__()

class ClassDeclNode(Node):
    def __init__(self, inherit=None, classDeclBody=None, classDrcl=None):
        super().__init__()

class VisibilityNode(Node):
    pass

class memberDeclNode(Node):
    pass

class funcDeclNode(Node):
    pass

class funcHeadNode(Node):
    pass

class funcDefNode(Node):
    pass

class funcBodyNode(Node):
    pass

class varDeclNode(Node):
    pass

class statementNode(Node):
    pass

class assignStatNode(Node):
    pass

class statBlockNode(Node):
    pass

class exprNode(Node):
    pass

class relExprNode(Node):
    pass

class arithExprNode(Node):
    pass

class signNode(Node):
    pass

class termNode(Node):
    pass

class factorNode(Node):
    pass

class variableNode(Node):
    pass

class functionCallNode(Node):
    pass

class functionDefNode(Node):
    pass

class methodBodyNode(Node):
    pass

class statementListNode(Node):
    pass

class functionNode(Node):
    pass


class idnestNode(Node):
    pass

class indiceNode(Node):
    pass

class arraySizeNode(Node):
    pass

class typeNode(Node):
    pass

class fParamsNode(Node):
    pass

class aParamsNode(Node):
    pass

class fParamsTailNode(Node):
    pass

class aParamsTailNode(Node):
    pass

class inheritNode(Node):
    pass

class classDeclBodyNode(Node):
    pass

class NestedIdNode(Node):
    pass

class StatBlockNode(Node):
    pass





class TerminalNode(Node):
    def __init__(self, data):
        self.data = data

class AParamsTailNode(Node):
    def __init__(self, data):
        self.data = data

class AssignOpNode(Node):
    def __init__(self, data):
        self.data = data

class RelOpNode(Node):
    def __init__(self, data):
        self.data = data

class AddOpNode(Node):
    def __init__(self, data):
        self.data = data

class MultOpNode(Node):
    def __init__(self, data):
        self.data = data