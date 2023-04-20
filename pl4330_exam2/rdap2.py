        
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parse(self):
        self.stmt()
        if self.index != '$': #end of file 
            raise Exception('parsing Error')        

    # def peek(self):
    #     if self.index < len(self.tokens):
    #         return self.tokens[self.index]
        
    def match(self, expected_token):
        if self.tokens[self.index] == expected_token:
            self.index += 1
        else:
            raise Exception(f"Expected {expected_token}, got {self.tokens[self.index]}")    

    def stmt(self):
            if self.tokens[self.index] == 'if':
                return self.if_stmt()
            elif self.peek() == '{':
                return self.block()
            elif self.peek() == 'DataType':
                return self.declare()
            elif self.peek() == 'while':
                return self.while_loop()
            else:
                return self.assign()
    
    def stmt_list(self):
        self.stmt()
        while self.current_token == ';':
            self.match(';')
            self.stmt()
    
    def if_stmt(self):
        self.match('if')
        self.match('(')
        bool_expr = self.bool_expr()
        self.match(')')
        if_block = self.block()
        else_block = None
        if self.tokens[self.index] == 'else':
            self.match('else')
            else_block = self.block()
        return ('if', bool_expr, if_block, else_block)

    def block(self):
        self.match('{')
        stmt_list = self.stmt_list()
        return ('block', stmt_list)
    
    def declare(self):
        self.match('DataType')
        id_handful = self.match(self.tokens[self.index])
        while self.tokens[self.index] == ',':
            self.match(',')
            id_handful
        return ('declare', id_handful)

#here we are returning function statement of the next valid token, but 
# is the return statments necessary or can seld.(statment type) be like that stright up 
    def assign(self):                           
        id = self.match(self.tokens[self.index])
        self.match('=')
        expr = self.expr()
        return ('assign', id, expr)                 #<--- necessary ?

    def expr(self):
        self.term()
        while self.tokens[self.index] in ['+','-','*','/','%']:
            self.match(self.tokens[self.index])
            self.term()
    
    def term(self):
        self.fact()
        while self.tokens[self.index] in ('*','/','%'):
            self.match(self.tokens[self.index])
            self.fact()
            
        

    def fact(self):
        if self.peek_type() == 'ID':
            return self.match_id()
        elif self.peek_type() in ('INT_LIT', 'FLOAT_LIT'):
            return self.match()
        elif self.tokens[self.index] == '(':
            self.match('(')
            self.expr()
            self.match(')')
        else:
            raise Exception(f"Invalid factor: {self.tokens[self.index]}")

    def bool_expr(self):
        bterm = self.bterm()
        while self.peek() in ('>','<','>=', '<='):
            operator = self.match()
            bterm2 = self.bterm()
            bterm = (operator, bterm, bterm2)
        return bterm

    def bterm(self):
        booleanAnd = self.booleanAnd()
        while self.peek() in ('==', '!='):
            operator = self.match()
            booleanAnd2= self.booleanAnd()
            booleanAnd = (operator, booleanAnd, booleanAnd2)
        return booleanAnd

    def booleanAnd(self):
        booleanOr = self.booleanOr()
        while self.peek() == '&&':
            self.match('&&')
            booleanOr2 = self.booleanOr()
            booleanOr = ('&&', booleanOr, booleanOr2)
        return booleanOr
    
    def booleanOr(self):
        expr = self.expr()
        while self.peek() == '||':
            self.match('||')
            expr2 = self.expr()
 

