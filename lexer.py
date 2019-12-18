from sly import Lexer

class MyLexer(Lexer):
    #Every Terminals our programming languages understands 
    tokens = { VARIABLE_NAME, NUMBER, STRING, IF, THEN, ELSE, FOR, FUNC, TO, ARROW, EQUALEQUAL }

    #Ignores Taps and Spaces
    ignore = '\t '
    #operators and others
    literals = { '=', '+', '-', '/', '*',')','(' }
    


    """The r means that the string is to be treated as a raw string, which means all escape codes will be ignored.

    For an example:

    '\n' will be treated as a newline character, while r'\n' will be treated as the characters \ followed by n.
    
    """
    
    """
    [0-9]	Returns a match for any digit between 0 and 9	
    [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
    [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
    []	A set of characters	"[a-m]"
    *	Zero or more occurrences		
    +	One or more occurrences
    .	Any character (except newline character)
    check "https://www.w3schools.com/python/python_regex.asp" for more 
    """
    #Our Tokens 
    IF = r'IF'
    THEN=r'THEN'
    ELSE=r'ELSE'
    FUNC=r'FUNC'
    FOR=r'FOR'
    TO=r'TO'
    ARROW=r'->'
    VARIABLE_NAME=r'[a-zA-Z_][a-zA-Z0-9]*'  #Variable VARIABLE_NAMEs must start with (a~z or A~Z or _) then anything in the second character

    STRING=r'"[a-zA-Z0-9_=+-]*"'         #.*? => zero or more occurances of any charachter except new line   
    EQUALEQUAL=r'=='


    #To make control of number tokens

    #\d+ means it has to be one or more digits
    @_(r'\d+')
    def NUMBER(self,t):
        t.value=int(t.value)
        return t

    #.* => zero or more occurances of any charachter except new line    
    @_(r'#.*')
    def COMMENT(self,comm):
        pass



"""
What does actually the parser do ?
    -Parser takes the tokens in the order that they where given
    -Check if this pattern actually means anything
    -example:
    -FUNC VARIABLE_NAME() -> a+b;
    -means if found -> after the FUNC return this operation
    -The Parser has to figure out if the language matches our grammar  
"""





