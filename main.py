from lexer import MyLexer
from parser import MyParser

if __name__ == "__main__":
    
    lexer = MyLexer()
    parser = MyParser()

    while True:
        
        text = input('our language > ')
        
        if text:
            
            lex = lexer.tokenize(text)
            #for token in lex:
             #   print(token)
            tree= parser.parse(lex)
            print(tree)


    
    
