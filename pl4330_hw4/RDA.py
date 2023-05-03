class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value
class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.pos = 0
    def match(self,expected):
        if self.tokens[self.pos].type == expected:
            self.pos += 1
            return True
        else:
            return False
    def expect(self, expected):
        if not self.match(expected):
            raise Exception(f"Expected '{expected}', found '{self.token[self.pos].value}'")
    def parse(self):
        self.stmt()
    def stmt(self):
        if self.match('IF'):
            self.expect('LPAREN')
            self.bool_expr()
            self.expect('RPAREN')
            if self.match('LBRACE'):
                self.stmt_list()
                self.expect('RBRACE')
            else:
                self.stmt()
            if self.match('ELSE'):
                if self.match('LBRACE'):
                    self.stmt_list()
                    self.expect('RBRACE')
                else:
                    self.stmt()
        elif self.match('LBRACE'):
            self.stmt_list()
            self.expect('RBRACE')
        elif self.match('WHILE'):
            self.expect('LPAREN')
            self.bool_expr()
            self.expect('RPAREN')
            if self.match('LBRACE'):
                self.stmt_list()
                self.expect('RBRACE')
            else:
                self.stmt()
        else:
            self.expr()
    def stmt_list(self):
         while self.tokens[self.pos].type != 'RBRACE':
            self.stmt()
            self.expect('SEMICOLON')
    def bool_expr(self):
        self.bterm()
        while self.match('LT') or self.match('GT') or self.match('LE') or self.match('GE'):
            self.bterm()
    def bterm(self):
        self.band()
        while self.match('EQ') or self.match('NE'):
            self.band()
    def band(self):
        self.bor()
        while self.match('AND'):
            self.bor()
    def bor(self):
        self.expr()
        while self.match('OR'):
            self.expr()
    def expr(self):
        self.term()
        while self.match('PLUS') or self.match('MINUS'):
            self.term()
    def term(self):
        self.fact()
        while self.match('MULT') or self.match('DIV') or self.match('MOD'):
            self.fact()
    def fact(self):
        if self.match('ID') or self.match('INT_LIT') or self.match('FLOAT_LIT'):
            pass
        elif self.match('LPAREN'):
            self.expr()
            self.expect('RPAREN')
        else:
            raise Exception(f"Expected identifier, integer literal, or floating point literal, found '{self.tokens[self.pos].value}'")