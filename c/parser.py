from lexer import tokenize
from constants.terminals import terminal, non_terminals
from constants.grammar import my_grammar

from c.NodeTypes import *

testsFolder = 'tests/'
tokens = list(tokenize(testsFolder + 'polynomial.src'))

global tokenIndex
tokenIndex = 0

stack = ['$', 'START']
error_file = open("results/polynomial.outsyntaxerrors", 'w')

terminals = []
derivation_file = open("results/polynomial.outderivation", 'w')


#################################################################
# Skip error
#################################################################

def skipErrors(first, follow):
    global tokenIndex
    if tokens[tokenIndex][0] in first:
        return True
    elif 'epsilon' in first and tokens[tokenIndex][0] in follow:
        return True
    else:
        error_file.write('syntax error at ' + str(tokens[tokenIndex][2]))
        while tokens[tokenIndex][0] not in first + follow:
            tokenIndex = tokenIndex + 1
            if 'epsilon' in first and tokens[tokenIndex][0] in follow:
                return False
        return True


#################################################################
# Derivation - reverse stack
#################################################################

def derivation():
    stack.reverse()
    # print(terminals + stack)
    derivation_file.write(str(terminals + stack) + '\n')
    stack.reverse()


derivation()


def stackTerminalChecker():
    if stack[-1] in terminal:
        terminals.extend([str(stack[-1])])
        stack.pop()
        derivation()


def stackChecker():
    if stack[-1] in non_terminals:
        if stack[-1] in my_grammar.keys():
            pop = stack.pop()
            stack.extend(my_grammar[pop])
            derivation()


#################################################################
# Parser
#################################################################


def parse():
    start = StartNode()
    semantic_stack.append(start)
    if _start():
        stackChecker()
        if match('EOF'):
            return True
        else:
            return False
    else:
        return False
    # return _start() and match('EOF')


def match(token):
    global tokenIndex
    if tokenIndex >= len(tokens):
        return False
    elif tokens[tokenIndex][0] == token:
        if tokens[tokenIndex][0] in terminal:
            pass#LeafNode(tokens[tokenIndex])
        stackTerminalChecker()
        tokenIndex = tokenIndex + 1
        return True
    else:
        # print('syntax error at ' + str(tokens[tokenIndex][2]) + ' expected ' + token)
        # tokenIndex = tokenIndex + 1
        return False


def _visibility():
    stackChecker()
    if not skipErrors(['private', 'public'], ['id', 'func', 'integer', 'float', 'string']):
        return False
    if tokens[tokenIndex][0] in ['private', 'public']:
        if match('public'):
            return True
        elif match('private'):
            return True
        # return match('public') or match('private')
    elif tokens[tokenIndex][0] in ['id', 'func', 'integer', 'float', 'string']:
        return True
    else:
        return False


def _type():
    if not skipErrors(['id', 'integer', 'float', 'string'], ['id', 'lcurbr', 'semi']):
        return False
    stackChecker()
    if tokens[tokenIndex][0] in ['integer', 'float', 'string', 'id']:
        # return match('integer') or match('float') or match('string') or match('id')
        if match('integer'):
            return True
        elif match('float'):
            return True
        elif match('string'):
            return True
        elif match('id'):
            return True
    else:
        return False


def _multi_op():
    if not skipErrors(['mult', 'div', 'and'],
                      ['plus', 'minus', 'id', 'intnum', 'floatnum', 'stringlit', 'lpar', 'not', 'qm']):
        return False
    if tokens[tokenIndex][0] in ['mult', 'div', 'and']:
        # return match('mult') or match('div') or match('and')
        if match('mult'):
            return True
        elif match('div'):
            return True
        elif match('and'):
            return True
    else:
        return False


def _add_op():
    if not skipErrors(['plus', 'minus', 'or'],
                      ['plus', 'minus', 'id', 'intnum', 'floatnum', 'stringlit', 'lpar', 'not', 'qm', '$']):
        return False
    if tokens[tokenIndex][0] in ['plus', 'minus', 'or']:
        # return match('plus') or match('minus') or match('or')
        if match('plus'):
            return True
        elif match('minus'):
            return True
        elif match('or'):
            return True
    else:
        return False


def _sign():
    if not skipErrors(['plus', 'minus'],
                      ['plus', 'minus', 'id', 'intnum', 'floatnum', 'stringlit', 'lpar', 'not', 'qm']):
        return False
    if tokens[tokenIndex][0] in ['plus', 'minus']:
        # return match('plus') or match('minus')
        if match('plus'):
            return True
        elif match('minus'):
            return True
    else:
        return False


def _rel_op():
    if tokens[tokenIndex][0] in ['eq', 'neq', 'lt', 'gt', 'leq', 'get']:
        # return match('eq') or match('neq') or match('lt') or match('gt') or match('leq') or match('get')
        if match('eq'):
            return True
        elif match('neq'):
            return True
        elif match('lt'):
            return True
        elif match('gt'):
            return True
    else:
        return False


def _assign_op():
    if tokens[tokenIndex][0] in ['assign']:
        # return match('assign')
        if match('assign'):
            return True
        else:
            return False


def _a_params():
    stackChecker()
    if tokens[tokenIndex][0] in ['plus', 'minus', 'id', 'intnum', 'floatnum', 'stringlit', 'lpar', 'not', 'qm']:
        # return _expr() and _a_params_tail()
        if _expr():
            stackChecker()
            if _a_params_tail():
                stackChecker()
                return True
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['rpar']:
        return True
    else:
        return False


def _a_params_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['comma']:
        # return match('comma') and _expr() and _a_params_tail()
        if match('comma'):
            if _expr():
                stackChecker()
                if _a_params_tail():
                    stackChecker()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['rpar']:
        return True
    else:
        return False


def _arith_expr():
    stackChecker()
    if tokens[tokenIndex][0] in ['plus', 'minus', 'id', 'intnum', 'floatnum', 'stringlit', 'lpar', 'not', 'qm']:
        # return _term() and _arith_expr_tail()
        if _term():
            stackChecker()
            if _arith_expr_tail():
                stackChecker()
                return True
            else:
                return False
        else:
            return False


def _arith_expr_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['plus', 'minus', 'or']:
        # return _add_op() and _term() and _arith_expr_tail()
        if _add_op():
            stackChecker()
            if _term():
                stackChecker()
                if _arith_expr_tail():
                    stackChecker()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['comma', 'rsqbr', 'semi', 'rpar', 'colon', 'eq', 'neq', 'lt', 'gt', 'leq', 'geq']:
        return True
    else:
        return False


def _array_size_rept():
    stackChecker()
    if tokens[tokenIndex][0] in ['lsqbr']:
        # return match('lsqbr') and _int_num() and match('rsqbr') and _array_size_rept()
        if match('lsqbr'):
            if _int_num():
                stackChecker()
                if match('rsqbr'):
                    if _array_size_rept():
                        stackChecker()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['comma', 'semi', 'rpar']:
        return True
    else:
        return False


def _assign_stat_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['assign']:
        # return _assign_op() and _expr()
        if _assign_op():
            stackChecker()
            if _expr():
                stackChecker()
                return True
            else:
                return False
        else:
            return False


def _class_declaration():
    class_declaration = semantic_stack.pop()

    stackChecker()
    if tokens[tokenIndex][0] in ['class']:
        # return match('class') and match('id') and _inherits() and match(
        #     'lcurbr') and _class_declaration_body() and match('rcurbr') and match('semi') and _class_declaration()

        class_declaration = ClassDeclNode()
        semantic_stack.append(class_declaration)

        class_declaration_body = classDeclBodyNode()
        semantic_stack.append(class_declaration_body)

        inherits = inheritNode()
        semantic_stack.append(inherits)



        if match('class'):
            if match('id'):
                if _inherits():
                    stackChecker()
                    if match('lcurbr'):
                        if _class_declaration_body():
                            stackChecker()
                            if match('rcurbr'):
                                if match('semi'):
                                    if _class_declaration():
                                        stackChecker()
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['func', 'main']:
        return True
    else:
        return False


def _class_declaration_body():
    stackChecker()
    if tokens[tokenIndex][0] in ['id', 'func', 'integer', 'float', 'string', 'public', 'private']:
        # return _visibility() and _member_declaration() and _class_declaration_body()
        if _visibility():
            stackChecker()
            if _member_declaration():
                stackChecker()
                if _class_declaration_body():
                    stackChecker()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['rcurbr']:
        return True
    else:
        return False


def _class_method():
    stackChecker()
    if tokens[tokenIndex][0] in ['sr']:
        # return match('sr') and match('id')
        if match('sr'):
            if match('id'):
                return True
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['lpar']:
        return True
    else:
        return False


def _expr():
    stackChecker()
    if tokens[tokenIndex][0] in ['plus', 'minus', 'id', 'intnum', 'floatnum', 'stringlit', 'lpar', 'not', 'qm']:
        # return _arith_expr() and _expr_tail()
        if _arith_expr():
            stackChecker()
            if _expr_tail():
                stackChecker()
                return True
            else:
                return False
        else:
            return False


def _expr_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['eq', 'neq', 'lt', 'gt', 'leq', 'geq']:
        # return _rel_op() and _arith_expr()
        if _rel_op():
            stackChecker()
            if _arith_expr():
                stackChecker()
                return True
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['comma', 'rsqbr', 'semi', 'rpar', 'colon']:
        return True
    else:
        return False


def _f_params():
    stackChecker()
    if tokens[tokenIndex][0] in ['id', 'integer', 'float', 'string']:
        # return _type() and match('id') and _array_size_rept() and _f_params_tail()
        if _type():
            stackChecker()
            if match('id'):
                if _array_size_rept():
                    stackChecker()
                    if _f_params_tail():
                        stackChecker()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['rpar']:
        return True
    else:
        return False


def _f_params_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['comma']:
        # return match('comma') and _type() and match('id') and _array_size_rept() and _f_params_tail()
        if match('comma'):
            if _type():
                stackChecker()
                if match('id'):
                    if _array_size_rept():
                        stackChecker()
                        if _f_params_tail():
                            stackChecker()
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['rpar']:
        return True
    else:
        return False


def _factor():
    stackChecker()
    if tokens[tokenIndex][0] in ['plus', 'minus', 'id', 'intnum', 'floatnum', 'stringlit', 'lpar', 'not', 'qm']:
        if _func_or_var():
            return True
        elif match('intnum'):
            return True
        elif match('floatnum'):
            return True
        elif match('stringlit'):
            return True
        # elif match('lpar') and _expr() and match('rpar'):
        #     return True
        elif match('lpar'):
            if _expr():
                stackChecker()
                if match('rpar'):
                    return True
                else:
                    return False
            else:
                return False
        # elif match('not') and _factor():
        #     return True
        elif match('not'):
            if match(_factor):
                stackChecker()
                return True
            else:
                return False
        elif _sign() and _factor():
            return True
        # elif match('qm') and match('lsqbr') and _expr() and match('colon') and _expr() and match(
        #         'colon') and _expr() and match('rsqbr'):
        #     return True
        elif match('qm'):
            if match('lsqbr'):
                if _expr():
                    stackChecker()
                    if match('colon'):
                        if _expr():
                            stackChecker()
                            if match('colon'):
                                if _expr():
                                    stackChecker()
                                    if match('rsqbr'):
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


def _func_body():
    stackChecker()
    # return match('lcurbr') and _method_body_var() and _statement_list() and match('rcurbr')
    if match('lcurbr'):
        if _method_body_var():
            stackChecker()
            if _statement_list():
                stackChecker()
                if match('rcurbr'):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def _func_declaration():
    if tokens[tokenIndex][0] in ['func']:
        # return match('func') and match('id') and match('lpar') and _f_params() and match('rpar') and match(
        #     'colon') and _func_declaration_tail() and match('semi')
        if match('func'):
            if match('id'):
                if match('lpar'):
                    if _f_params():
                        stackChecker()
                        if match('rpar'):
                            if match('colon'):
                                if _func_declaration_tail():
                                    stackChecker()
                                    if match('semi'):
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def _func_declaration_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['id', 'integer', 'float', 'string']:
        # return _type() or match('void')
        if _type():
            stackChecker()
            return True
    if tokens[tokenIndex][0] in ['void']:
        if match('void'):
            return True
        else:
            return False
    else:
        return False


def _func_def():
    stackChecker()
    if tokens[tokenIndex][0] in ['func']:
        # return _function() and _func_def()
        if _function():
            stackChecker()
            if _func_def():
                stackChecker()
                return True
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['main']:
        return True
    else:
        return False


def _func_head():
    stackChecker()
    if tokens[tokenIndex][0] in ['func']:
        # return match('func') and match('id') and _class_method() and match('lpar') and _f_params() and match(
        #     'rpar') and match('colon') and _func_declaration_tail()
        if match('func'):
            if match('id'):
                if _class_method():
                    stackChecker()
                    if match('lpar'):
                        if _f_params():
                            if match('rpar'):
                                if match('colon'):
                                    if _func_declaration_tail():
                                        stackChecker()
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def _func_or_assign_stat():
    stackChecker()
    if tokens[tokenIndex][0] in ['id']:
        # return match('id') and _func_or_assign_stat_idnest()
        if match('id'):
            if _func_or_assign_stat_idnest():
                stackChecker()
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def _func_or_assign_stat_idnest():
    stackChecker()
    if tokens[tokenIndex][0] in ['lsqbr', 'assign', 'lpar', 'dot']:
        # if _indice_rep() and _func_or_assign_stat_idnest_var_tail():
        if _indice_rep():
            stackChecker()
            if _func_or_assign_stat_idnest_var_tail():
                stackChecker()
                return True
            else:
                return False
        # elif match('lpar') and _a_params() and match('rpar') and _func_or_assign_stat_idnest_func_tail():
        elif match('lpar'):
            if _a_params():
                stackChecker()
                if match('rpar'):
                    if _func_or_assign_stat_idnest_func_tail():
                        stackChecker()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def _func_or_assign_stat_idnest_func_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['dot']:
        # return _indice_rep() and match('dot') and match('id') and _func_stat_tail()
        if _indice_rep():
            stackChecker()
            if match('dot'):
                if match('id'):
                    if _func_stat_tail():
                        stackChecker()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['semi']:
        return True
    else:
        return False


def _func_stat_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['lsqbr', 'lpar', 'dot']:
        # if _indice_rep() and match('dot') and match('id') and _func_stat_tail():
        # return True
        if _indice_rep():
            stackChecker()
            if match('dot'):
                if match('id'):
                    if _func_stat_tail():
                        stackChecker()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        # elif match('lpar') and _a_params() and match('rpar') and _func_stat_tail_idnest():
        #     return True
        elif match('lpar'):
            if _a_params():
                stackChecker()
                if match('rpar'):
                    if _func_stat_tail_idnest():
                        stackChecker()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


def _func_stat_tail_idnest():
    stackChecker()
    if tokens[tokenIndex][0] in ['dot']:
        # return match('dot') and match('id') and _func_stat_tail()
        if match('dot'):
            if match('id'):
                if _func_stat_tail():
                    stackChecker()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['semi']:
        return True
    else:
        return False


def _func_or_assign_stat_idnest_var_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['dot', 'assign']:
        # return match('dot') and match('id') and _func_or_assign_stat_idnest() or _assign_stat_tail()
        if match('dot'):
            if match('id'):
                if _func_or_assign_stat_idnest():
                    stackChecker()
                    return True
                else:
                    return False
            else:
                return False
        elif _assign_stat_tail():
            stackChecker()
            return True
        else:
            return False


def _func_or_var():
    stackChecker()
    if tokens[tokenIndex][0] in ['id']:
        # return match('id') and _func_or_var_idnest()
        if match('id'):
            if _func_or_var_idnest():
                stackChecker()
                return True
            else:
                return False
        else:
            return False


def _func_or_var_idnest():
    stackChecker()
    # if _indice_rep() and _func_or_var_idnest_tail():
    # return True
    if _indice_rep():
        stackChecker()
        if _func_or_var_idnest_tail():
            stackChecker()
            return True
        else:
            return False
    # elif match('lpar') and _a_params() and match('rpar') and _func_or_var_idnest_tail():
    #     return True
    elif match('lpar'):
        if _a_params():
            stackChecker()
            if match('rpar'):
                if _func_or_var_idnest_tail():
                    stackChecker()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def _func_or_var_idnest_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['dot']:
        # return match('dot') and match('id') and _func_or_var_idnest()
        if match('dot'):
            if match('id'):
                if _func_or_var_idnest():
                    stackChecker()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['plus', 'minus', 'or', 'comma', 'rsqbr', 'semi', 'rpar', 'colon', 'mult', 'div',
                                   'and', 'eq', 'neq', 'lt', 'gt',
                                   'leq', 'geq']:
        return True
    else:
        return False


def _function():
    stackChecker()
    if tokens[tokenIndex][0] in ['func']:
        # return _func_head() and _func_body()
        if _func_head():
            stackChecker()
            if _func_body():
                stackChecker()
                return True
            else:
                return False
        else:
            return False


def _indice_rep():
    stackChecker()
    if tokens[tokenIndex][0] in ['lsqbr']:
        # return match('lsqbr') and _expr() and match('rsqbr') and _indice_rep()
        if match('lsqbr'):
            if _expr():
                stackChecker()
                if match('rsqbr'):
                    if _indice_rep():
                        stackChecker()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['plus', 'minus', 'or', 'comma', 'rsqbr', 'semi', 'rpar', 'colon', 'mult', 'div',
                                   'and', 'eq', 'neq', 'lt', 'gt',
                                   'leq', 'geq', 'assign', 'dot']:
        return True
    else:
        return False


def _inherits():
    inherits = semantic_stack.pop()

    nested_id = NestedIdNode()
    semantic_stack.append(nested_id)


    stackChecker()
    if tokens[tokenIndex][0] in ['inherits']:
        # return match('inherits') and match('id') and _nested_id()
        if match('inherits'):
            if match('id'):
                if _nested_id():
                    stackChecker()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['lcurbr']:
        return True
    else:
        return False


def _int_num():
    stackChecker()
    if tokens[tokenIndex][0] in ['intnum']:
        # return match('intnum')
        if match('intnum'):
            return True
        else:
            return False
    elif tokens[tokenIndex][0] in ['rsqbr']:
        return True
    else:
        return False


def _member_declaration():
    stackChecker()
    if tokens[tokenIndex][0] in ['id', 'func', 'integer', 'float', 'string']:
        # return _func_declaration() or _var_declaration()
        if _func_declaration():
            stackChecker()
            return True
        elif _var_declaration():
            stackChecker()
            return True
        else:
            return False


def _method_body_var():
    stackChecker()
    if tokens[tokenIndex][0] in ['var']:
        # return match('var') and match('lcurbr') and _var_declaration_rep() and match('rcurbr')
        if match('var'):
            if match('lcurbr'):
                if _var_declaration_rep():
                    stackChecker()
                    if match('rcurbr'):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['id', 'rcurbr', 'if', 'while', 'read', 'write', 'return', 'break', 'continue']:
        return True
    else:
        return False


def _nested_id():
    stackChecker()
    if tokens[tokenIndex][0] in ['comma']:
        # return match('comma') and match('id') and _nested_id()
        if match('comma'):
            if match('id'):
                if _nested_id():
                    stackChecker()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['lcurbr']:
        return True
    else:
        return False


def _prog():
    prog = semantic_stack.pop()
    stackChecker()
    if tokens[tokenIndex][0] in ['class', 'func', 'main']:
        # return _class_declaration() and _func_def() and match('main') and _func_body()

        func_body = funcBodyNode()
        semantic_stack.append(func_body)

        func_def = funcDefNode()
        semantic_stack.append(func_def)

        class_declaration = ClassDeclNode()
        semantic_stack.append(class_declaration)

        if _class_declaration():
            stackChecker()
            if _func_def():
                stackChecker()
                if match('main'):
                    if _func_body():
                        Node.make_familly(ProgNode(), [class_declaration, func_def, func_body])
                        stackChecker()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


def _start():
    start = semantic_stack.pop()
    stackChecker()
    if tokens[tokenIndex][0] in ['class', 'func', 'main']:
        # return _prog()

        prog = ProgNode()
        semantic_stack.append(prog)

        if _prog():
            stackChecker()
            return True
        else:
            return False


def _stat_block():

    stat_block = semantic_stack.pop()


    stackChecker()
    if tokens[tokenIndex][0] in ['id', 'lcurbr', 'if', 'while', 'read', 'write', 'return', 'break', 'continue']:
        # if match('lcurbr') and _statement_list() and match('rcurbr'):
        #     return True

        stat_block = StatBlockNode()
        semantic_stack.append(stat_block)

        if match('lcurbr'):
            if _statement_list():
                stackChecker()
                if match('rcurbr'):
                    return True
                else:
                    return False
            else:
                return False


        elif _statement():
            stackChecker()
            return True
        else:
            return False
    elif tokens[tokenIndex][0] in ['semi', 'else']:
        return True
    else:
        return False


def _statement():
    stackChecker()
    if tokens[tokenIndex][0] in ['id', 'if', 'while', 'read', 'write', 'return', 'break', 'continue']:
        # if _func_or_assign_stat() and match('semi'):
        #     return True
        if _func_or_assign_stat():
            stackChecker()
            if match('semi'):
                return True
        # elif match('if') and match('lpar') and _expr() and match('rpar') and match('then') and _stat_block() and match(
        #         'else') and _stat_block() and match('semi'):
        #     return True
        elif match('if'):
            if match('lpar'):
                if _expr():
                    stackChecker()
                    if match('rpar'):
                        if match('then'):
                            if _stat_block():
                                stackChecker()
                                if match('else'):
                                    if _stat_block():
                                        stackChecker()
                                        if match('semi'):
                                            return True
                                        else:
                                            return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        # elif match('while') and match('lpar') and _expr() and match('rpar') and _stat_block() and match('semi'):
        #     return True
        if match('while'):
            if match('lpar'):
                if _expr():
                    stackChecker()
                    if match('rpar'):
                        if _stat_block():
                            if match('semi'):
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        # elif match('read') and match('lpar') and _variable() and match('rpar') and match('semi'):
        #     return True
        if match('read'):
            if match('lpar'):
                if _variable():
                    stackChecker()
                    if match('rpar'):
                        if match('semi'):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        # elif match('write') and match('lpar') and _expr() and match('rpar') and match('semi'):
        #     return True
        if match('write'):
            if match('lpar'):
                if _expr():
                    stackChecker()
                    if match('rpar'):
                        if match('semi'):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        # elif match('return') and match('lpar') and _expr() and match('rpar') and match('semi'):
        #     return True
        if match('return'):
            if match('lpar'):
                if _expr():
                    stackChecker()
                    if match('rpar'):
                        if match('semi'):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        # elif match('break') and match('semi'):
        #     return True
        elif match('break'):
            if match('semi'):
                return True
            else:
                return False
        # elif match('continue') and match('semi'):
        #     return True
        elif match('continue'):
            if match('semi'):
                return True
            else:
                return False
        else:
            return False


def _statement_list():
    stackChecker()
    if tokens[tokenIndex][0] in ['id', 'if', 'while', 'read', 'write', 'return', 'break']:
        # return _statement() and _statement_list()
        if _statement():
            stackChecker()
            if _statement_list():
                stackChecker()
                return True
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['rcurbr']:
        return True
    else:
        return False


def _term():
    stackChecker()
    if tokens[tokenIndex][0] in ['plus', 'minus', 'id', 'intnum', 'floatnum', 'stringlit', 'lpar', 'not', 'qm']:
        # return _factor() and _term_tail()
        if _factor():
            stackChecker()
            if _term_tail():
                stackChecker()
                return True
            else:
                return False
        else:
            return False


def _term_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['mult', 'div', 'and']:
        # return _multi_op() and _factor() and _term_tail()
        if _multi_op():
            stackChecker()
            if _factor():
                stackChecker()
                if _term_tail():
                    stackChecker()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['plus', 'minus', 'or', 'comma', 'rsqbr', 'semi', 'rpar', 'colon', 'eq', 'neq', 'lt',
                                   'gt', 'leq', 'geq']:
        return True
    else:
        return False


def _var_declaration():
    stackChecker()
    if tokens[tokenIndex][0] in ['id', 'integer', 'float', 'string']:
        # return _type() and match('id') and _array_size_rept() and match('semi')
        if _type():
            stackChecker()
            if match('id'):
                if _array_size_rept():
                    stackChecker()
                    if match('semi'):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def _var_declaration_rep():
    stackChecker()
    if tokens[tokenIndex][0] in ['id', 'integer', 'float', 'string']:
        # return _var_declaration() and _var_declaration_rep()
        if _var_declaration():
            stackChecker()
            if _var_declaration_rep():
                stackChecker()
                return True
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['rcurbr']:
        return True
    else:
        return False


def _variable():
    stackChecker()
    if tokens[tokenIndex][0] in ['id']:
        # return match('id')and _variable_idnest()
        if match('id'):
            if _variable_idnest():
                stackChecker()
                return True
            else:
                return False
        else:
            return False


def _variable_idnest():
    stackChecker()
    if tokens[tokenIndex][0] in ['lsqrbr', 'dot']:
        # return _indice_rep() and _variable_idnest_tail()
        if _indice_rep():
            stackChecker()
            if _variable_idnest_tail():
                stackChecker()
                return True
            else:
                return False
        else:
            return False


def _variable_idnest_tail():
    stackChecker()
    if tokens[tokenIndex][0] in ['dot']:
        # return match('dot') and match('id') and _variable_idnest()
        if match('dot'):
            if match('id'):
                if _variable_idnest():
                    stackChecker()
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokens[tokenIndex][0] in ['rpar']:
        return True
    else:
        return False


#################################################################
semantic_stack = []
if parse():
    derivation_file.write('success')
    print('success')
else:
    print('did not work')
