lexical_specifications = [
    # Identifier 1 to n letters
    ('id', r'[a-zA-Z]\w*'),
    # Alphanumerics letter | digit | _
    ('ALPHANUM', r'^(?!\d*$)\w+$'),
    # float negative or positive float numbers
    ('floatnum', r'[+-]?(([1-9]+\d*(\.\d*)[eE][+-]?\d+)|[1-9]+\d*(\.\d+))'),
    # integer
    ('intnum', r'\d+'),
    # integer
    ('INTEGER', r'[1-9]+\d*(?!\w)|(0)(?=\s)'),
    # fraction
    ('FRACTION', r'\.\d*\d+|\.0'),
    # letter
    ('LETTER', r'[A-Za-z]'),
    # digit
    ('DIGIT', r'^\d+$'),
    # nonzero
    ('NONZERO', r'^\d+$'),
    # string
    ('STRING', r'\"(.+?)\"'),
    # character
    ('CHARACTER', r'(\w) \1'),
    # inline comment
    ('inlinecmt', r'(//.*)'),
    # single line block comment
    ('blockcmt', r'\/\*[\s\S]*?\*\/'),
    # eq
    ('eq', r'=='),
    # plus
    ('plus', r'\+'),
    # or
    ('or', r'\|'),
    # openpar
    ('lpar', r'\('),
    # semi
    ('semi', r'\;'),
    # noteq
    ('noteq', r'\<>'),
    # minus
    ('minus', r'\-'),
    # and
    ('and', r'\&'),
    # closepar
    ('rpar', r'\)'),
    # comma
    ('comma', r'\,'),
    # lt
    ('lt', r'\<'),
    # leq
    ('leq', r'\<\='),
    # mult
    ('mult', r'\*'),
    # not
    ('not', r'\!'),
    # opencubr
    ('lcurbr', r'\{'),
    # dot
    ('dot', r'\.'),
    # gt
    ('gt', r'\>'),
    # div
    ('div', r'/'),
    # qmark
    ('qmark', r'\?'),
    # closecubr
    ('rcurbr', r'\}'),
    #sr
    ('sr', r'\:\:'),
    # colon
    ('colon', r'\:'),
    # assign
    ('assign', r'\='),
    # opensqbr
    ('lsqbr', r'\['),
    # geq
    ('geq', r'\>='),
    # closesqbr
    ('rsqbr', r'\]'),
    # tab space
    ('SKIP', r'[ \t]+'),
    # newline
    ('NEWLINE', r'\n'),
    # any other character
    ('MISMATCH', r'[^\s]+'),
    # end of file
    ('EOF', r'\Z'),
    # empty
    ('EPSILON', r'^$'),



]