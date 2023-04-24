


    
        
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
        self.bool_expr()
        self.match(')')
        self.block()
        if self.tokens[self.index] == 'else':
            self.match('else')
            self.block()
        

    def block(self):
        self.match('{')
        self.stmt_list()
        
    
    def declare(self):
        self.match('DataType')
        self.match(self.tokens[self.index])
        while self.tokens[self.index] == ',':
            self.match(',')
            self.match(self.tokens[self.index])
        

    def assign(self):                           
        self.match(self.tokens[self.index])
        self.match('=')
        self.expr()


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


#start reviewing here! 
    def bool_expr(self):
        self.bterm()
        while self.peek() in ('>','<','>=', '<='):
            self.match()
        

    def bterm(self):
        self.booleanAnd()
        while self.peek() in ('==', '!='):
            self.match()
            self.booleanAnd()
            
        

    def booleanAnd(self):
        self.booleanOr()
        while self.peek() == '&&':
            self.match('&&')
            self.booleanOr()
           
        
    
    def booleanOr(self):
        self.expr()
        while self.peek() == '||':
            self.match('||')
            self.expr()
 

test_stmt = 1+3

p1 = Parser(test_stmt)
