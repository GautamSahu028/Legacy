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

#######################################################################
# DEMO-RUN
#######################################################################
    
tk_1 = Token('INT', 9)
tk_2 = Token('PLUS')
tk_3 = Token('FLOAT', 1.4)


print(tk_1) # ==> INT:9
print(tk_2) # ==> PLUS
print(tk_3) # ==> FLOAT:1.4

#######################################################################


list_of_tokens = []

list_of_tokens.append(tk_1)
list_of_tokens.append(tk_2)
list_of_tokens.append(tk_3)

print(list_of_tokens) # ==> [INT:9, PLUS, FLOAT:1.4]

#######################################################################



