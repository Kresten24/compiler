from enum import Enum







class AssignOpEnum(Enum):
    assign = '='

class RelOpEnum(Enum):
    eq = 'eq'  
    neq = 'neq'  
    lt = 'lt'  
    gt = 'gt'  
    leq = 'leq'  
    geq = 'geq'

class MultOpEnum(Enum):
    _multiply = '*'
    _divide = '/'
    _and = 'and'

class AddOpEnum(Enum):
    _plus = '+'
    _minus = '-'
    _or = 'or'
