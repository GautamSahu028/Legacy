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

#######################################################################
# DEMO-RUN
#######################################################################
    
tk_1 = Token('ANK', 9)
tk_2 = Token('YOJAN')
tk_3 = Token('DASHAMLAV', 1.4)


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



