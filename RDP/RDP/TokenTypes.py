from enum import Enum, auto

#types of syntactical constructs https://youtu.be/4mXbLRH2p1Q?t=1670


class MultOpEnum(Enum):
    _multiply = '*'
    _divide = '/'
    _and = 'and'


class IntNum(Enum):
    intnum = 'intnum'
    floatnum = 'floatnum'
    ALPHANUM = 'ALPHANUM'
    FRACTION = 'FRACTION'
    LETTER = 'LETTER'
    DIGIT = 'DIGIT'
    NONZERO = 'NONZERO'
    STRING = 'STRING'
    CHARACTER = 'CHARACTER'

class ID(Enum):
    id = 'id'

class Operator(Enum):
    inlinecmt = 'inlinecmt'
    blockcmt = 'blockcmt'
    eq = 'eq'
    plus = '+'
    OR = 'or'
    lpar = 'lpar'
    semi = 'semi'
    noteq = 'noteq'
    minus = 'minus'
    AND = 'and'
    rpar = 'rpar'
    comma = 'comma'
    lt = 'lt'
    leq = 'leq'
    mult = '*'
    NOT = 'not'
    lcurbr = 'lcurbr'
    dot = 'dot'
    gt = 'gt'
    div = 'div'
    qmark = 'qmark'
    rcurbr = 'rcurbr'
    sr = 'sr'
    colon = 'colon'
    assign = 'assign'
    lsqbr = 'lsqbr'
    geq = 'geq'
    rsqbr = 'rsqbr'
    SKIP = 'SKIP'
    NEWLINE = 'NEWLINE'
    MISMATCH = 'MISMATCH'
    EOF = 'EOF'
    EPSILON = 'EPSILON'
