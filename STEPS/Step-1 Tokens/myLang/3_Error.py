DIGITS = '0123456789'

###########################################################################################################
# TOKENS
###########################################################################################################
TT_INT		= 'ANK'
TT_FLOAT    = 'DASHAMLAV'
TT_PLUS     = 'YOJAN'
TT_MINUS    = 'GHATNM'
TT_MUL      = 'GUNM'
TT_DIV      = 'BHAG'
TT_LPAREN   = '_KOSHTHAKM'
TT_RPAREN   = 'KOSHTHAKM_'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
    

###########################################################################################################
# ERROR
###########################################################################################################
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        return result
    
# Child of Error class that deals with a specific type of error i.e Illegal Character error
class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Awaidh Chinh ', details)

###########################################################################################################
# LEXER
###########################################################################################################
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos< len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            
            # if there is an invalid character
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        print(num_str)

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

###########################################################################################################
# DEMO-RUN
###########################################################################################################

lx_1 = Lexer('2 + 3&')
tokens, error = lx_1.make_tokens()
if error:
    print(error.as_string())
else:
    print(tokens)