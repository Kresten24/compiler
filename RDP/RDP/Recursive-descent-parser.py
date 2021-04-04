from TokenTypes import Operator, IntNum
from ast import Node
from parseTree import Tree
from NodeTypes import *

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

    Fs = semantic_stack.pop() #Fs

    stackChecker()
    if s[i] in ['(']:

        Es = EsNode()
        semantic_stack.append(Es)

        if (match("(")):
            if (E()):
                stackChecker()
                if (match(")")):
                    Fs = semantic_stack.pop() #pop(Es)
                    return True
                else:
                    return False
            else:
                return False
    elif s[i] in ['1']:
        if (match("1")):
            Fs = FsNode(1)
            semantic_stack.append(Fs)
            # Fs = Node.makeNode(IntNum.intnum.value)
            return True
    elif s[i] in ['0']:
        if (match("0")):
            Fs = FsNode(0)
            semantic_stack.append(Fs)
            # Fs = Node.makeNode(IntNum.intnum.value)
            return True
    else:
        return False


def Tx():  # Fi, Txs
    # if not skipErrors(['*', 'epsilon'], ['+', '$', ')']):
    #     return False


    Txs = semantic_stack.pop() #pop(Txs)
    Fi = semantic_stack.pop() #pop(Fs)

    stackChecker()
    if s[i] in [Operator.mult.value]:

        Fs = FsNode()
        Txs2 = TxsNode()

        semantic_stack.append(Txs2)
        semantic_stack.append(Fs)

        if (match(Operator.mult.value)):
            if (F()):
                stackChecker()
                if (Tx()):

                    Txs = Node.make_familly(Node(Operator.mult.value), [Fi,Txs2])
                    semantic_stack.append(Txs)

                    stackChecker()

                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif s[i] in ['+', ')', '$']:

        Txs = Fi
        semantic_stack.append(Txs)

        return True
    else:
        return False


def T():  # Ts
    # if not skipErrors(['0', '1', '('], ['+', '$', ')']):
    #     return False

    Ts = semantic_stack.pop() #pop(Ts)

    if s[i] in ['0', '1', '(']:

        Fs = FsNode()
        Txs = TxsNode()

        semantic_stack.append(Txs)
        semantic_stack.append(Fs)


        if (F()):
            stackChecker()
            if (Tx()):
                stackChecker()

                Ts = semantic_stack.pop() #pop(Txs)
                semantic_stack.append(Ts)

                return True
            else:
                return False
        else:
            return False


def Ex():  # Ti, Exs
    # if not skipErrors(['+', 'epsilon'], ['$', ')']):
    #     return False

    Ti = semantic_stack.pop() #Ts
    Exs = semantic_stack.pop() #Exs


    stackChecker()
    if s[i] in [Operator.plus.value]:

        Ts = TsNode()
        Ex2s = ExsNode()

        semantic_stack.append(Ex2s)
        semantic_stack.append(Ts)

        if (match(Operator.plus.value)):
            if (T()):
                stackChecker()
                if (Ex()):

                    Exs = Node.make_familly(Node(Operator.plus.value), [Ti, Ex2s])
                    semantic_stack.append(Exs)

                    stackChecker()

                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif s[i] in [')', '$']:

        Exs = Ti
        semantic_stack.append(Exs)

        return True
    else:
        return False


def E():  # Es
    # if not skipErrors(['0', '1', '('], [')', '$']):
    #     return False

    Es = semantic_stack.pop() #pop(Es)

    stackChecker()
    if s[i] in ['0', '1', '(']:


        Exs = ExsNode()
        Ts = TsNode()
        # Exs = Node()
        # Ts = Node()

        semantic_stack.append(Exs)
        semantic_stack.append(Ts)

        if (T()):
            stackChecker()
            if (Ex()):

                Es = semantic_stack.pop() #pop(Exs)
                semantic_stack.append(Es)

                stackChecker()
                return True
            else:
                return False
        else:
            return False


semantic_stack = []
# nodes = []

def parse():

    Es = EsNode()
    semantic_stack.append(Es)
    if E():  # Es

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
semantic_stack[0].printTree()


# (0+1)*0
