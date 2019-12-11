from sly import Lexer
from sly import Parser
from lexer import MyLexer
class MyParser(Parser):
    tokens = MyLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
        )

  
    @_('')
    def statement(self, p):
        pass


    #The for loop grammar is 
    #FOR  x=0 TO 5 THEN x
    #                             for_loop
    #                           /          \
    #                    for_loop_setup     'var'       
    #                      /    \             |  
    #               var_assign   num          x  
    #                /     \      |
    #               x       num   5
    #                        |
    #                        5

    @_('FOR var_assign TO expr THEN statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)

     
    #                            if_stmt
    #                           /       \
    #                    condition            
    #                                   /    \
    #                              statment   statement
    #                               "THEN"      "ELSE"

    @_('IF condition THEN statement ELSE statement')
    def statement(self, p):
        return ('if_stmt', p.condition, ('branch', p.statement0, p.statement1))

    @_('FUNC VARIABLE_NAME "(" ")" ARROW statement')
    def statement(self, p):
        return ('fun_def', p.VARIABLE_NAME, p.statement)


    #THE NAME OF THE FUNCTION HERE IS TREATED AS A VARIABLE NAME TOO
    @_('VARIABLE_NAME "(" ")"')
    def statement(self, p):
        return ('fun_call', p.VARIABLE_NAME)

    @_('expr EQUALEQUAL expr')
    def condition(self, p):
        return ('condition_eqeq', p.expr0, p.expr1)


    """Variable can be assigned to another variable or to an expression "x=1+2" or to a String 'x="Ahmed"'
        Expression also could be a number x=1
        it can also be another variable x=a "only if a is a predefined variable"
    """
    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('VARIABLE_NAME "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.VARIABLE_NAME, p.expr)

    @_('VARIABLE_NAME "=" STRING')
    def var_assign(self, p):
        return ('var_assign', p.VARIABLE_NAME, ('String',p.STRING))

    @_('expr')
    def statement(self, p):
        return (p.expr)

    @_('expr "+" expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)

    @_('expr "*" expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)

    @_('expr "/" expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)

    @_('"-" expr %prec UMINUS') #To accept the minus sign before a number
    def expr(self, p):
        return p.expr

    @_('VARIABLE_NAME')
    def expr(self, p):
        return ('var', p.VARIABLE_NAME)

    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)
