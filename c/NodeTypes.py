from c.ast import Node
from c.constants.terminals import TerminalEnum


class StartNode(Node):
    def __init__(self, prog):
        self.prog = prog


class ProgNode(Node):
    def __init__(self, classDecl, funcDef, funcBody):
        self.classDecl = classDecl
        self.funcDef = funcDef
        self.funcBody = funcBody
        self.main = TerminalNode(TerminalEnum._main.value)

class ClassDeclNode(Node):
    def __init__(self, inherit, classDeclBody, classDrcl):
        self.inherit = inherit
        self.classDeclBody = classDeclBody
        self.classDrcl = classDrcl

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