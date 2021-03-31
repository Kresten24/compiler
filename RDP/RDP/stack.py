
stack = ['$', 'E']

_E = ['Ex', 'T']
_T = ['Tx', 'F']
_Ex = ['Ex', 'T', '+']
_Tx = ['Tx', 'F', '*']
_F = [')', 'E', '(']
_F1 = ['0']
_F2 = ['1']

terminals = []


def reverseStack():
    stack.reverse()
    print(terminals + stack)
    stack.reverse()


reverseStack()


def stackConstantChecker():
    if (stack[-1] == '('):
        terminals.extend('(')
        stack.pop()
        reverseStack()
        # print(stack)

    elif (stack[-1] == ')'):
        terminals.extend(')')
        stack.pop()
        reverseStack()
        # print(stack)
    elif (stack[-1] == '+'):
        terminals.extend('+')
        stack.pop()
        reverseStack()
        # print(stack)
    elif (stack[-1] == '*'):
        terminals.extend('*')
        stack.pop()
        reverseStack()
        # print(stack)
    elif (stack[-1] == '1'):
        terminals.extend('1')
        stack.pop()
        reverseStack()
        # print(stack)
    elif (stack[-1] == '0'):
        terminals.extend('0')
        stack.pop()
        reverseStack()
        # print(stack)


def stackChecker():
    global s
    global i
    if (stack[-1] == 'E'):
        stack.pop()
        stack.extend(_E)
        reverseStack()
        # print(stack)
    elif (stack[-1] == 'Ex'):
        if s[i] == '+':
            stack.pop()
            stack.extend(_Ex)
        else:
            stack.pop()
    elif (stack[-1] == 'T'):
        stack.pop()
        stack.extend(_T)
        reverseStack()
        # print(stack)
    elif (stack[-1] == 'F'):
        stack.pop()
        if s[i] == '1':
            stack.extend(_F2)
        elif s[i] == '0':
            stack.extend(_F1)
        else:
            stack.extend(_F)
            reverseStack()
        # print(stack)
    elif (stack[-1] == 'Tx'):
        if s[i] == '*':
            stack.pop()
            stack.extend(_Tx)
        else:
            stack.pop()
            reverseStack()
        # print(stack)