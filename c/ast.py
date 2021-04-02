global i
i = 0


class Node:

    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.left_most_sibiling = None  # left sibiling
        self.right_sibiling = None  # right sibiling
        self.left_most_child = None

    def makeNode(data=None):
        if data is None:
            return Node()
        # elif data in IntNum.__members__:
        #     return IntNumNode(data)
        # elif data in ID.__members__:
        #     return IdNode(data)
        # elif data in Operator.__members__:
        #     return OpNode(data)

    def _get_rightmost_sibiling(self):
        node = self
        while self.right_sibiling is not None:
            node = self.right_sibiling
        return node

    def make_siblings(self, y):
        xsibs = self._get_rightmost_sibiling()
        # join lists
        ysibs = y.left_most_sibiling
        xsibs.right_sibiling = ysibs
        # set pointers to new sibilings
        ysibs.left_most_sibiling = xsibs.left_most_sibiling
        ysibs.parent = xsibs.parent
        while ysibs.right_sibiling is not None:
            ysibs = ysibs.right_sibiling
            ysibs.left_most_sibiling = xsibs.left_most_sibiling
            ysibs.parent = xsibs.parent

        return ysibs

    def adopt_children(self, y):
        if self.left_most_child is not None:
            self.left_most_child.make_sibilings(y)
        else:
            ysibs = y.left_most_sibiling
            self.left_most_child = ysibs
            while ysibs is not None:
                ysibs.parent = self
                ysibs = ysibs.right_sibiling

    def make_familly(node, list_children_nodes):
        if list_children_nodes is not None and len(list_children_nodes) >= 2:
            for i in range(0, len(list_children_nodes) - 1):
                list_children_nodes[i].make_siblings(list_children_nodes[i + 1])

            return node.adopt_children(list_children_nodes[0])


#################################################################
# Nodes
#################################################################

# class IntNum(Node):
#     def __init__(self, data):
#         self.data = data
#
#
# class IdNode(Node):
#     def __init__(self, data):
#         self.data = data
#
#
# class OpNode(Node):
#     def __init__(self, data):
#         self.data = data
#
#
# class BinaryOpNode:
#     def __init__(self, left_node, op_tok, right_node):
#         self.left_node = left_node
#         self.op_tok = op_tok
#         self.right_node = right_node
#
#     def __repr__(self):
#         return f'({self.left_node}, {self.op_tok}, {self.right_node})'
#
#
# class LeafNode(Node):
#     def __init__(self, token):
#         self.token = token
