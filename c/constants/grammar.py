my_grammar = {
    'AParams': ['AParamsTail', 'Expr'],
    'AParamsTail': ['AParamsTail', 'Expr', 'comma'],
    'AddOp': ['plus'],
    'AddOp1': ['minus'],
    'AddOp2': ['or'],
    'ArithExpr': ['ArithExprTail', 'Term'],
    'ArithExprTail': ['ArithExprTail', 'Term', 'AddOp'],
    'ArraySizeRept': ['ArraySizeRept', 'rsqbr', 'IntNum', 'lsqbr'],
    'AssignOp': ['assign'],
    'AssignStatTail': ['Expr', 'AssignOp'],
    'ClassDecl': ['ClassDecl', 'semi', 'rcurbr', 'ClassDeclBody', 'lcurbr', 'Inherit', 'id', 'class'],
    'ClassDeclBody': ['ClassDeclBody', 'MemberDecl', 'Visibility'],
    'ClassMethod': ['id', 'sr'],
    'Expr': ['ExprTail', 'ArithExpr'],
    'ExprTail': ['ArithExpr', 'RelOp'],
    'FParams': ['FParamsTail', 'ArraySizeRept', 'id', 'Type'],
    'FParamsTail': ['FParamsTail', 'ArraySizeRept', 'id', 'Type', 'semi'],
    'Factor': ['FuncOrVar'],
    'Factor1': ['intnum'],
    'Factor2': ['floatnum'],
    'Factor3': ['stringlit'],
    'Factor4': ['rpar', 'Expr', 'lpar'],
    'Factor5': ['Factor', 'not'],
    'Factor6': ['Factor', 'Sign'],
    'Factor7': ['rsqbr', 'Expr', 'colon', 'Expr', 'colon', 'Expr', 'lsqbr', 'qm'],
    'FuncBody': ['rcurbr', 'StatementList', 'MethodBodyVar', 'lcurbr'],
    'FuncDecl': ['semi', 'FuncDeclTail', 'colon', 'rpar', 'FParams', 'lpar', 'id', 'func'],
    'FuncDeclTail': ['Type'],
    'FuncDeclTail1': ['void'],
    'FuncDef': ['FuncDef', 'Function'],
    'FuncHead': ['FuncDeclTail', 'colon', 'rpar', 'FParams', 'lpar', 'ClassMethod', 'id', 'func'],
    'FuncOrAssignStat': ['FuncOrAssignStatIdnest', 'id'],
    'FuncOrAssignStatIdnest': ['FuncOrAssignStatIdnestVarTail', 'IndiceRep'],
    'FuncOrAssignStatIdnest1': ['FuncOrAssignStatIdnestFuncTail', 'rpar', 'AParams', 'lpar'],
    'FuncOrAssignStatIdnestFuncTail': ['FuncStatTail', 'id', 'dot'],
    'FuncStatTail': ['FuncStatTail', 'id', 'dot', 'IndiceRep'],
    'FuncStatTail1': ['FuncStatTailIdnest', 'rpar', 'AParams', 'lpar'],
    'FuncStatTailIdnest': ['FuncStatTail', 'id', 'dot'],
    'FuncOrAssignStatIdnestVarTail': ['FuncOrAssignStatIdnest', 'id', 'dot'],
    'FuncOrAssignStatIdnestVarTail1': ['AssignStatTail'],
    'FuncOrVar': ['FuncOrVarIdnest', 'id'],
    'FuncOrVarIdnest': ['FuncOrVarIdnestTail', 'IndiceRep'],
    'FuncOrVarIdnest2': ['FuncOrVarIdnestTail', 'rpar', 'AParams', 'lpar'],
    'FuncOrVarIdnestTail': ['FuncOrVarIdnest', 'id', 'dot'],
    'Function': ['FuncBody', 'FuncHead'],
    'IndiceRep': ['IndiceRep', 'rsqbr', 'Expr', 'lsqbr'],
    'Inherit': ['NestedId', 'id', 'inherits'],
    'IntNum': ['intnum'],
    'MemberDecl': ['FuncDecl'],
    'MemberDecl1': ['VarDecl'],
    'MethodBodyVar': ['rcurbr', 'VarDeclRep', 'lcurbr', 'var'],
    'MultOp': ['mult'],
    'MultOp1': ['div'],
    'MultOp2': ['and'],
    'NestedId': ['NestedId', 'id', 'comma'],
    'Prog': ['FuncBody', 'main', 'FuncDef', 'ClassDecl'],
    'RelOp': ['eq'],
    'RelOp1': ['neq'],
    'RelOp2': ['lt'],
    'RelOp3': ['gt'],
    'RelOp4': ['leq'],
    'RelOp5': ['geq'],
    'START': ['Prog'],
    'Sign': ['plus'],
    'Sign1': ['minus'],
    'StatBlock': ['rcurbr', 'StatementList', 'lcurbr'],
    'StatBlock1': ['Statement'],
    'Statement': ['semi', 'FuncOrAssignStat'],
    'Statement1': ['semi', 'StatBlock', 'else', 'StatBlock', 'then', 'rpar', 'Expr', 'lpar', 'if'],
    'Statement2': ['semi', 'StatBlock', 'rpar', 'Expr', 'lpar', 'while'],
    'Statement3': ['semi', 'rpar', 'Variable', 'lpar', 'read'],
    'Statement4': ['semi', 'rpar', 'Expr', 'lpar', 'write'],
    'Statement5': ['semi', 'rpar', 'Expr', 'lpar', 'return'],
    'Statement6': ['semi', 'break'],
    'Statement7': ['semi', 'continue'],
    'StatementList': ['StatementList', 'Statement'],
    'Term': ['TermTail', 'Factor'],
    'TermTail': ['TermTail', 'Factor', 'MultOp'],
    'Type': ['integer'],
    'Type1': ['float'],
    'Type2': ['string'],
    'Type3': ['id'],
    'VarDecl': ['semi', 'ArraySizeRept', 'id', 'Type'],
    'VarDeclRep': ['VarDeclRep', 'VarDecl'],
    'Variable': ['VariableIdnest', 'id'],
    'VariableIdnest': ['VariableIdnestTail', 'IndiceRep'],
    'VariableIdnestTail': ['VariableIdnest', 'id', 'dot'],
    'Visibility': ['public'],
    'Visibility1': ['private'],
}
# AParams = ['AParamsTail', 'Expr']
# AParamsTail = ['AParamsTail', 'Expr', 'comma']
# AddOp = ['plus']
# AddOp1 = ['minus']
# AddOp2 = ['or']
# ArithExpr = ['ArithExprTail', 'Term']
# ArithExprTail = ['ArithExprTail', 'Term', 'AddOp']
# ArraySizeRept = ['ArraySizeRept', 'rsqbr', 'IntNum', 'lsqbr']
# AssignOp = ['assign']
# AssignStatTail = ['Expr', 'AssignOp']
# ClassDecl = ['ClassDecl', 'semi', 'rcurbr', 'ClassDeclBody', 'lcurbr', 'Inherit', 'id', 'class']
# ClassDeclBody = ['ClassDeclBody', 'MemberDecl', 'Visibility']
# ClassMethod = ['id', 'sr']
# Expr = ['ExprTail', 'ArithExpr']
# ExprTail = ['ArithExpr', 'RelOp']
# FParams = ['FParamsTail', 'ArraySizeRept', 'id', 'Type']
# FParamsTail = ['FParamsTail', 'ArraySizeRept', 'id', 'Type', 'semi']
# Factor = ['FuncOrVar']
# Factor1 = ['intnum']
# Factor2 = ['floatnum']
# Factor3 = ['stringlit']
# Factor4 = ['rpar', 'Expr', 'lpar']
# Factor5 = ['Factor', 'not']
# Factor6 = ['Factor', 'Sign']
# Factor7 = ['rsqbr', 'Expr', 'colon', 'Expr', 'colon', 'Expr', 'lsqbr', 'qm']
# FuncBody = ['rcurbr', 'StatementList', 'MethodBodyVar', 'lcurbr']
# FuncDecl = ['semi', 'FuncDeclTail', 'colon', 'rpar', 'FParams', 'lpar', 'id', 'func']
# FuncDeclTail = ['Type']
# FuncDeclTail1 = ['void']
# FuncDef = ['FuncDef', 'Function']
# FuncHead = ['FuncDeclTail', 'colon', 'rpar', 'FParams', 'lpar', 'ClassMethod', 'id', 'func']
# FuncOrAssignStat = ['FuncOrAssignStatIdnest', 'id']
# FuncOrAssignStatIdnest = ['FuncOrAssignStatIdnestVarTail', 'IndiceRep']
# FuncOrAssignStatIdnest1 = ['FuncOrAssignStatIdnestFuncTail', 'rpar', 'AParams', 'lpar']
# FuncOrAssignStatIdnestFuncTail = ['FuncStatTail', 'id', 'dot']
# FuncStatTail = ['FuncStatTail', 'id', 'dot', 'IndiceRep']
# FuncStatTail1 = ['FuncStatTailIdnest', 'rpar', 'AParams', 'lpar']
# FuncStatTailIdnest = ['FuncStatTail', 'id', 'dot']
# FuncOrAssignStatIdnestVarTail = ['FuncOrAssignStatIdnest', 'id', 'dot']
# FuncOrAssignStatIdnestVarTail1 = ['AssignStatTail']
# FuncOrVar = ['FuncOrVarIdnest', 'id']
# FuncOrVarIdnest = ['FuncOrVarIdnestTail', 'IndiceRep']
# FuncOrVarIdnest2 = ['FuncOrVarIdnestTail', 'rpar', 'AParams', 'lpar']
# FuncOrVarIdnestTail = ['FuncOrVarIdnest', 'id', 'dot']
# Function = ['FuncBody', 'FuncHead']
# IndiceRep = ['IndiceRep', 'rsqbr', 'Expr', 'lsqbr']
# Inherit = ['NestedId', 'id', 'inherits']
# IntNum = ['intnum']
# MemberDecl = ['FuncDecl']
# MemberDecl1 = ['VarDecl']
# MethodBodyVar = ['rcurbr', 'VarDeclRep', 'lcurbr', 'var']
# MultOp = ['mult']
# MultOp1 = ['div']
# MultOp2 = ['and']
# NestedId = ['NestedId', 'id', 'comma']
# Prog = ['FuncBody', 'main', 'FuncDef', 'ClassDecl']
# RelOp = ['eq']
# RelOp1 = ['neq']
# RelOp2 = ['lt']
# RelOp3 = ['gt']
# RelOp4 = ['leq']
# RelOp5 = ['geq']
# START = ['Prog']
# Sign = ['plus']
# Sign1 = ['minus']
# StatBlock = ['rcurbr', 'StatementList', 'lcurbr']
# StatBlock1 = ['Statement']
# Statement = ['semi', 'FuncOrAssignStat']
# Statement1 = ['semi', 'StatBlock', 'else', 'StatBlock', 'then', 'rpar', 'Expr', 'lpar', 'if']
# Statement2 = ['semi', 'StatBlock', 'rpar', 'Expr', 'lpar', 'while']
# Statement3 = ['semi', 'rpar', 'Variable', 'lpar', 'read']
# Statement4 = ['semi', 'rpar', 'Expr', 'lpar', 'write']
# Statement5 = ['semi', 'rpar', 'Expr', 'lpar', 'return']
# Statement6 = ['semi', 'break']
# Statement7 = ['semi', 'continue']
# StatementList = ['StatementList', 'Statement']
# Term = ['TermTail', 'Factor']
# TermTail = ['TermTail', 'Factor', 'MultOp']
# Type = ['integer']
# Type1 = ['float']
# Type2 = ['string']
# Type3 = ['id']
# VarDecl = ['semi', 'ArraySizeRept', 'id', 'Type']
# VarDeclRep = ['VarDeclRep', 'VarDecl']
# Variable = ['VariableIdnest', 'id']
# VariableIdnest = ['VariableIdnestTail', 'IndiceRep']
# VariableIdnestTail = ['VariableIdnest', 'id', 'dot']
# Visibility = ['public']
# Visibility1 = ['private']
