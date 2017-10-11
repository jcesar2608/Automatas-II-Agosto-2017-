#FAUSTO GREGORIO CIPRIANO
import sys
import ply.lex as lex

viejolexpos=0
viejolineno=0
columna=0

"""
El módulo sys es el encargado de proveer variables y funcionalidades,
directamente relacionadas con el intérprete.
    sys.argv:
        Retorna una lista con todos los argumentos pasados por línea de
        comandos. Al ejecutar python modulo.py arg1 arg2,
        retornará una lista: ['modulo.py', 'arg1', 'arg2']
"""

tokens = (
    'IDENTIFICADOR',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUAL',
    'DIFERENTE',
    'POR',
    'ENTRE',
    'INCREMENTO',
    'DECREMENTO',
    'MAS',
    'MENOS',
    'MODULO',
    'ASIGNACION',
    'INT',
    'FLOAT',
    'PARENTESISOPEN',
    'PARENTESISCLOSE',
    'CORCHETEOPEN',
    'CORCHETECLOSE',
    'LLAVEOPEN',
    'LLAVECLOSE',
    'COMENTARIO',
    'AND',
    'OR',
    'NOT',
    'FINSENTENCIA',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'STRING',
    'NULO',
    'IMPORT',
    'CONSTANT',
    'CONCAT',
    'ELSEIF',
    'RETURN',
    'FUNCTION',
    'ECHO',
    'SCANNER',
    'MAIN',
    'IDFUNCION',
)
#comentario
def t_MAIN(t):
    r'principal'
    return t
def t_SCANNER(t):
    r'entrada'
    return t
def t_ECHO(t):
    r'imprime'
    return t
def t_FUNCTION(t):
    r'funcion'
    return t
def t_RETURN(t):
    r'regresa'
    return t
def t_CONSTANT(t):
    r'constante'
    return t
def t_IMPORT(t):
    r'importar'
    return t
def t_NULO(t):
    r'nulo | NULO'
    return t
def t_IF(t):
    r'si'
    return t
def t_ELSE(t):
    r'sino'
    return t
def t_ELSEIF(t):
    r'osino'
    return t
def t_WHILE(t):
    r'mientras'
    return t
def t_FOR(t):
    r'para'
    return t
def t_COMENTARIO(t):
    r'\#.*'
    return t
def t_FLOAT(t):
    r'(\d{1,}\.\d{1,})'
    return t
def t_INT(t):
    r'\d{1,}'
    return t
def t_IDENTIFICADOR(t):
	r'\&[a-zA-z]\w*'
	return t
def t_FINSENTENCIA(t):
    r'\;'
    return t
def t_MAYORQUE(t):
    r'\>'
    return t
def t_MENORQUE(t):
    r'\<'
    return t
def t_MAYORIGUAL(t):
    r'\>\='
    return t
def t_MENORIGUAL(t):
    r'\<\='
    return t
def t_IGUAL(t):
    r'\=\='
    return t
def t_DIFERENTE(t):
    r'\!\='
    return t
def t_INCREMENTO(t):
    r'\+\+'
    return t
def t_DECREMENTO(t):
    r'\-\-'
    return t
def t_POR(t):
    r'\*'
    return t
def t_ENTRE(t):
    r'\/'
    return t
def t_MAS(t):
    r'\+'
    return t
def t_MENOS(t):
    r'\-'
    return t
def t_MODULO(t):
    r'\%'
    return t
def t_ASIGNACION(t):
	r'='
	return t
def t_PARENTESISOPEN(t):
    r'\('
    return t
def t_STRING(t):
    r'(\".*\")|(\'.*\')'
    return t
def t_PARENTESISCLOSE(t):
    r'\)'
    return t
def t_CORCHETEOPEN(t):
    r'\['
    return t
def t_CORCHETECLOSE(t):
    r'\]'
    return t
def t_LLAVEOPEN(t):
    r'\{'
    return t
def t_LLAVECLOSE(t):
    r'\}'
    return t
def t_AND(t):
    r'\&\&'
    return t
def t_OR(t):
    r'\|\|'
    return t
def t_NOT(t):
    r'\!'
    return t
def t_CONCAT(t):
    r'\.'
    return t
def t_IDFUNCION(t):
    r'[a-zA-z]\w*'
    return t
# Patron para saltos de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    


# Patron que contiene caracteres ignorados (espacios y tabuladores)

t_ignore = ' \t'


# Regla de manejo de errores
def t_error(t):
    print("{:30}|{:15}|{:5}|{:5}|".format(
        t.value[0], "ERROR", t.lineno, t.lexpos+1-viejolexpos))
    t.lexer.skip(1)


"""
t.type   = Token encontrado
t.value  = Valor del lexema.
t.lineno = El numero de la linea donde se encontro el lexema
"""


def analisis_lexico(data):
    analizador = lex.lex()
    analizador.input(data)
    global viejolexpos
    global viejolineno
    global columna
    while True:
        t = analizador.token()
        if not t:
            break
        columna=t.lexpos+1-viejolexpos
        if viejolineno != t.lineno:
            columna=1
            viejolexpos=t.lexpos
        viejolineno=t.lineno
        print("{:30}|{:15}|{:5}|{:5}|".format(t.value, t.type, t.lineno, columna))
        

if __name__ == '__main__':
    file = open("codigo.txt", "r")
    print("{:30}|{:15}|{:5}|{:5}|".format(
        "LEXEMA", "TOKEN", "LINEA", "COLUMNA"))
    analisis_lexico(file.read())
