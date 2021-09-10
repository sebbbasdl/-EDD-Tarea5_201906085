reserved ={
    'MES':'TMES',
    'DIA':'TDIA',
    'HORA':'THORA',
    'CARNET':'TCARNET',
    'NOMBRE':'TNOMBRE',
    'DESCRIPCION':'TDESCRIPCION',
    'MATERIA':'TMATERIA',
    'FECHA':'TFECHA',
    'ESTADO':'TESTADO',

}

tokens=[
    'COMA','ID','NUMBER','NORMSTRING'
]+list(reserved.values())

t_COMA = r'\,'
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print('Error en print %d', t.value)
        t.value = 0
    return t

def t_NORMSTRING(t):
    r'\"(\\.|[^"\\])*\"'
    print("la cadena es: '%s" % t.value)
    return t

# Ignored characters
t_ignore = ' \t\r\n'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
import re
lexer = lex.lex(reflags=re.IGNORECASE)
