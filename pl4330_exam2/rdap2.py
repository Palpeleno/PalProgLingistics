
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parse(self):
        return self.stmt_list()
    
    def match(self, ex_token):
        if self.tokens[self.index] == ex_token:
            self.index += 1
        else:
            raise Exception(f"Expected {ex_token}, but instead got {self.tokens[self.index]}")

        
    def stmt(self):
            if self.tokens[self.index] == 'if':
                return self.if_stmt()
            elif self.tokens[self.index] == '{':
                return self.block()
            elif self.tokens[self.index] == 'DataType':
                return self.declare()
            elif self.tokens[self.index]  == 'while':
                return self.while_loop()
            else:
                return self.assign()

    def stmt_list(self):
        self.match('{')
        while self.tokens[self.index] != '}':
            self.stmt()
            self.match(';')
        self.match('}')

    def while_loop(self):
        self.match("while")
        self.match("(")
        self.bool_expr()
        self.match(")")
        self.block()

    
    def if_stmt(self):
        self.match =='if'
        self.match == '('
        self.bool_expr()
        self.match == ')'
        self.block()
        if self.tokens[self.index] == 'else':
            self.match == 'else'
        return self.block()

    def block(self):
        self.match == '{'
        self.stmt_list()
        self.match('}')
    
    def declare(self):
        self.match('DataType')
        self.match(self.tokens[self.index]) == 'id'
        while self.tokens[self.index]  == ',':
            self.match(',')
            self.match(self.tokens[self.index]) == 'id'

    def assign(self):                           
        self.match('ID')
        self.match('=')
        self.expr()


    def expr(self):
        self.term()
        while self.tokens[self.index] in ('+','-'):
            self.match(self.tokens[self.index])
            self.term()
    
    def term(self):
        self.fact()
        while self.tokens[self.index] in ('*','/','%'):
            self.match(self.tokens[self.index])
            self.fact()
            
    def fact(self):
        if self.tokens[self.index] == 'ID':
            self.match('ID')
        elif self.tokens[self.index] in ('INT_LIT', 'FLOAT_LIT'):
            self.match(self.tokens[self.index])
        elif self.tokens[self.index] == '(':
            self.match('(')
            self.expr()
            self.match(')')
        else:
            raise Exception(f"Invalid factor: {self.tokens[self.index]}")

    def bool_expr(self):
        self.boolTerm()
        while self.tokens[self.index] in ('>','<','>=', '<='): 
            self.match(self.tokens[self.index])
            self.boolTerm()

    def boolTerm(self):
        self.boolAnd()
        while self.tokens[self.index] in ('==', '!='):
            self.match(self.tokens[self.index])
            self.boolAnd()
            
    def boolAnd(self):
        self.boolOr()
        while self.tokens[self.index] == '&&':
            self.match('&&')
            self.boolOr()
           
    def boolOr(self):
        self.expr()
        while self.tokens[self.index] == '||':
            self.match('||')
            self.expr()
 

tokens = ["DataType", "int", "x", ",", "y", ";", "if", "(", "x", ">", "y", ")", "{", "x", "=", "y", ";", "}", "while", "(", "y", "<", "100", ")", "{", "y", "=", "y", "+", "1", ";", "}", "x", "=", "y", "+", "2", ";"]
parser = Parser(tokens)
parser.parse()