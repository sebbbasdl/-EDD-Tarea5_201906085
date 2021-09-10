from analizadorest5.lexicot5 import tokens

# dictionary of names
names = {}


def p_statement_separacioncomas(t):
    'statement : dato COMA dato COMA dato COMA dato COMA dato COMA dato COMA dato COMA dato COMA dato'
    print("ok")
"""def p_dato_group(t):
    dato : TMES
            | TDIA
            | THORA
            | TCARNET
            | TNOMBRE
            | TDESCRIPCION
            | TMATERIA
            | TFECHA
            | TESTADO
            | info
    """

def p_dato(t):
    """dato : NORMSTRING
            | NUMBER


    """
def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()