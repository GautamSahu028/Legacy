######################################################################
# CONSTANTS
######################################################################

DIGITS = '0123456789'

######################################################################
# ERRORS
######################################################################

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

######################################################################
# POSITION
######################################################################

'''
- The Position class is designed to keep track of the current position within the source code that is being processed. 
- This is useful for tasks such as error reporting, where you need to know the exact location (line and column) of an issue in the code
'''

class Position:

    ''' This method sets up the initial position (index, line, column) and stores the file name and text.'''
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx # The position of the current character in the text (starting from 0).
        self.ln = ln     # The current line number (starting from 0).
        self.col = col   # The current column number (starting from 0).
        self.fn = fn     #  The name of the file being processed.
        self.ftxt = ftxt # The entire text of the file being processed.


    ''' 
        This method moves the position to the next character in the text.
            - It increments the index (idx) and column (col).
            - If the current character is a newline (\n), it moves to the  next line (ln) and resets the column to 0.
            - It returns the updated Position object itself, allowing for method chaining if needed.
    '''
    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    '''
        In a lexer, if an error occurs, we want to know the exact position in the text where the error happened. The copy method helps us capture the position before we advance further, so we can refer back to it when reporting the error.
    '''
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

######################################################################
# TOKENS
######################################################################

TT_INT		= 'INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

######################################################################
# LEXER
######################################################################

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

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
            else:
                pos_start = self.pos.copy()  # Copy the position where the error starts
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

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

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

######################################################################
# RUN
######################################################################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error