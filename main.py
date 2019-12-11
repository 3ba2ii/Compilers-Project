from lexer import MyLexer
from parser import MyParser

def main():
    lexer = MyLexer()
    parser = MyParser()

    while True:
        try:
            text = input('our language > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)
main()

    
    
