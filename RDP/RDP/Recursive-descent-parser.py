from TokenTypes import Operator, IntNum
from ast import Node
from parseTree import Tree

print("Recursive Desent Parsing For following grammar\n")
print("E->TE'\nE'->+TE'/@\nT->FT'\nT'->*FT'/@\nF->(E)/1/0\n")
print("Enter the string want to be checked\n")

stack = ['$', 'E']

_E = ['Ex', 'T']
_T = ['Tx', 'F']
_Ex = ['Ex', 'T', '+']
_Tx = ['Tx', 'F', '*']
_F = [')', 'E', '(']
_F1 = ['0']
_F2 = ['1']

global s
# s = list(input())
s = list('1+1*1$')
global i
i = 0


def Union(lst1, lst2):
    final_list = lst1 + lst2
    return final_list


# def skipErrors(first, follow):
#     global i
#     if s[i] in first:
#         return True
#     elif 'epsilon' in first and s[i] in follow:
#         return True
#     else:
#         print('syntax error')
#         while s[i] not in Union(first, follow):
#             i += 1
#             if 'epsilon' in first and s[i] in follow:
#                 return False
#         return True

dict_of_Nodes = {}
terminals = []


def reverseStack():
    stack.reverse()
    print(terminals + stack)
    stack.reverse()


reverseStack()


def stackConstantChecker():
    return True
    # if (stack[-1] == '('):
    #     terminals.extend('(')
    #     stack.pop()
    #     reverseStack()
    #     # print(stack)
    #
    # elif (stack[-1] == ')'):
    #     terminals.extend(')')
    #     stack.pop()
    #     reverseStack()
    #     # print(stack)
    # elif (stack[-1] == '+'):
    #     terminals.extend('+')
    #     stack.pop()
    #     reverseStack()
    #     # print(stack)
    # elif (stack[-1] == '*'):
    #     terminals.extend('*')
    #     stack.pop()
    #     reverseStack()
    #     # print(stack)
    # elif (stack[-1] == '1'):
    #     terminals.extend('1')
    #     stack.pop()
    #     reverseStack()
    #     # print(stack)
    # elif (stack[-1] == '0'):
    #     terminals.extend('0')
    #     stack.pop()
    #     reverseStack()
    #     # print(stack)


def stackChecker():
    return True
    # global s
    # global i
    # if (stack[-1] == 'E'):
    #     stack.pop()
    #     stack.extend(_E)
    #     reverseStack()
    #     # print(stack)
    # elif (stack[-1] == 'Ex'):
    #     if s[i] == '+':
    #         stack.pop()
    #         stack.extend(_Ex)
    #     else:
    #         stack.pop()
    # elif (stack[-1] == 'T'):
    #     stack.pop()
    #     stack.extend(_T)
    #     reverseStack()
    #     # print(stack)
    # elif (stack[-1] == 'F'):
    #     stack.pop()
    #     if s[i] == '1':
    #         stack.extend(_F2)
    #     elif s[i] == '0':
    #         stack.extend(_F1)
    #     else:
    #         stack.extend(_F)
    #         reverseStack()
    #     # print(stack)
    # elif (stack[-1] == 'Tx'):
    #     if s[i] == '*':
    #         stack.pop()
    #         stack.extend(_Tx)
    #     else:
    #         stack.pop()
    #         reverseStack()
    # print(stack)


def match(a):
    global s
    global i
    if (i >= len(s)):
        return False
    elif (s[i] == a):
        stackConstantChecker()
        if (len(s) - 1 > i):
            i += 1
        return True
    else:
        # print('syntax error expected token' + s[i])
        # i += 1
        return False


def F():  # Fs
    # if not skipErrors(['0', '1', '('], ['*', '+', '$', ')']):
    #     return False

    # Fs = nodes.pop()

    stackChecker()
    if s[i] in ['(']:

        # Es = Node.makeNode()
        # nodes.append(Es)

        if (match("(")):
            if (E()):
                stackChecker()
                if (match(")")):
                    # Fs = nodes.pop()
                    return True
                else:
                    return False
            else:
                return False
    elif s[i] in ['1']:
        if (match("1")):
            # Fs = Node.makeNode(1)
            # nodes.append(Fs)
            # Fs = Node.makeNode(IntNum.intnum.value)
            # dict_of_Nodes['Fs'] = Node.makeNode(IntNum.intnum.value)
            return True
    elif s[i] in ['0']:
        if (match("0")):
            # Fs = Node.makeNode(IntNum.intnum.value)
            # dict_of_Nodes['Fs'] = Node.makeNode(IntNum.intnum.value)
            return True
    else:
        return False


def Tx():  # Fi, Txs
    # if not skipErrors(['*', 'epsilon'], ['+', '$', ')']):
    #     return False

    #
    # Txs = nodes.pop()
    # Fi = nodes.pop()

    stackChecker()
    if s[i] in [Operator.mult.value]:

        # Fs = Node.makeNode()
        # Tx2s = Node.makeNode()
        # nodes.append(Tx2s)
        # nodes.append(Fs)

        if (match(Operator.mult.value)):
            if (F()):
                stackChecker()
                if (Tx()):
                    # Txs = Node.make_familly(Operator.mult.value, [Fs, Tx2s])
                    # dict_of_Nodes['Txs'] = Node.make_familly(Operator.mult.value, [Fs, Tx2s])
                    stackChecker()

                    # Txs = Node.make_familly(Operator.mult, [Fi, Tx2s])
                    # nodes.append(Txs)

                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif s[i] in ['+', ')', '$']:

        # Txs = Fi
        # nodes.append(Txs)

        return True
    else:
        return False


def T(Ts):  # Ts
    # if not skipErrors(['0', '1', '('], ['+', '$', ')']):
    #     return False

    Fs = Tree('Fs')
    Txs = Tree('Txs')

    Ts.children = [Fs,Txs]

    # Ts = nodes.pop()


    if s[i] in ['0', '1', '(']:

        # Fs = Node.makeNode()
        # Txs = Node.makeNode()
        # nodes.append(Txs)
        # nodes.append(Fs)

        if (F()):
            stackChecker()
            if (Tx()):
                stackChecker()
                #
                # Ts = nodes.pop()
                # nodes.append(Ts)

                return True
            else:
                return False
        else:
            return False


def Ex(Ti, Exs):  # Ti, Exs
    # if not skipErrors(['+', 'epsilon'], ['$', ')']):
    #     return False

    # Ti = nodes.pop()
    # Exs = nodes.pop()

    Ts = Tree('Ts')
    Ex2s = Tree('EX2s')

    Ex.children = [Ts, Ex2s]

    stackChecker()
    if s[i] in [Operator.plus.value]:
        # Ts = Node.makeNode()
        # Ex2s = Node.makeNode()
        # nodes.append(Ex2s)
        # nodes.append(Ts)
        if (match(Operator.plus.value)):
            if (T(Ts)):
                stackChecker()
                if (Ex(Ts, Ex2s)):
                    # Exs = Node.make_familly(Operator.plus.value, [Ti, Ex2s])
                    # dict_of_Nodes['Exs'] = Node.make_familly(Operator.plus.value, [dict_of_Nodes['Ti'], Ex2s])
                    stackChecker()

                    # Exs = Node.make_familly(Operator.plus, [Ti, Ex2s])
                    # nodes.append(Exs)

                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif s[i] in [')', '$']:
        # Exs = Ti
        # nodes.append(Exs)
        return True
    else:
        return False


def E(Es):  # Es
    # if not skipErrors(['0', '1', '('], [')', '$']):
    #     return False

    # Es = nodes.pop()

    stackChecker()
    if s[i] in ['0', '1', '(']:

        # Ts = Node.makeNode()
        # Exs = Node.makeNode()
        # nodes.append(Exs)
        # nodes.append(Ts)

        Ts = Tree('Ts')
        Exs = Tree('Exs')

        Es.children = [Ts,Exs]

        print(Es.data)

        if (T(Ts)):
            stackChecker()
            if (Ex(Ts, Exs)):

                # Es = nodes.pop()
                # nodes.append(Es)

                stackChecker()
                return True
            else:
                return False
        else:
            return False


stack = []
# nodes = []

def parse():
    # Es = Node.makeNode()
    # nodes.append(Es)

    root = Tree('root')

    Es = Tree('Es');
    root.children = [Es]

    if E(Es):  # Es
        print(root.children)
        print(Es.children)

        reverseStack()
        # if (stack[-1] == '$'):
        #     print('success')
        if i == len(s) - 1:
            print("String is accepted")
        else:
            print("String is not accepted")

    else:
        print("string is not accepted")


parse()


# (0+1)*0
