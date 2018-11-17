#
# Mauricio Cortes A00816689
# Eduardo Castro A00816926
# 04/11/2018

import ply.lex as lex

# PALABRAS RESERVADAS
reserved = {
    'program': 'PROGRAM',
    'if': 'IF',
    'else': 'ELSE',
    'var': 'VAR',
    'True' : 'TRUE',
    'False' : 'FALSE',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'boolean': 'BOOLEAN',
    'void': 'VOID',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    'print' : 'PRINT',
    'input' : 'READ',
    'func' : 'FUNC',
    'while' : 'WHILE',
    'main' : 'MAIN',
    'return' : 'RETURN',

    # FUNCIONES PREDEFINIDAS
    'start' : 'START',
    'reset' : 'RESET',
    'end' : 'END',
    'gira_izq' : 'GIRA_IZQ',
    'gira_der' : 'GIRA_DER',
    'camina' : 'CAMINA',
    'si_dibuja' : 'SI_DIBUJA',
    'no_dibuja' : 'NO_DIBUJA',
    'dibuja_poligono' : 'DIBUJA_POLIGONO',
    'dibuja_circulo' : 'DIBUJA_CIRCULO',
    'dibuja_estrella' : 'DIBUJA_ESTRELLA',
    'color_pluma' : 'COLOR_PLUMA'
}

# Token list (Tuple)
tokens = list(reserved.values()) + [
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDES',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_OR_EQUAL_THAN',
    'LESS_OR_EQUAL_THAN',
    'EQUAL_THAN',
    'NOT_EQUAL_THAN',
    'COMMA',
    'COLON',
    'SEMICOLON',
    'CONST_INT',
    'CONST_FLOAT',
    'CONST_STRING'
]

# Regular expressions for each token
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDES = r'/'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE= r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_GREATER_OR_EQUAL_THAN = r'>='
t_LESS_OR_EQUAL_THAN = r'<='
t_EQUAL_THAN = r'=='
t_NOT_EQUAL_THAN = r'!='
t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';'
t_CONST_STRING = r'\".*\" | \'.*\''

# Characteres that will be ignored
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Verifies that is not a reserved word
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CONST_INT(t):
    r'-?[0-9]+'
    return t

def t_CONST_FLOAT(t):
    r'-?[0-9]+\.[0-9][0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error lexico
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
file = open("archivo_entrada.txt", "r")
if file.mode == 'r':
    input_data = file.read()
lexer = lex.lex()
lexer.input(input_data)
file.close()
while True:
    token = lexer.token()
    if not token:        
        break
    #print(token)


