class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = tokens[0]
        self.index = 0

    def parse(self):
        self.stmt()
        if self.current_token != '$':
            raise Exception('parsing Error')        

    def stmt_list(self):
        self.stmt()
        while self.current_token == ';':
            self.match(';')
            self.stmt()

    def stmt(self):
        if self.peek() == 'if':
            return self.if_stmt()
        elif self.peek() == '{':
            return self.block()
        elif self.peek() == 'DataType':
            return self.declare()
        elif self.peek() == 'while':
            return self.while_loop()
        else:
            return self.assign()
    
    def if_stmt(self):
        self.eat('if')
        self.eat('(')
        bool_expr = self.bool_expr()
        self.eat(')')
        if_block = self.block()
        else_block = None
        if self.peek() == 'else':
            self.eat('else')
            else_block = self.block()
        return ('if', bool_expr, if_block, else_block)

    def block(self):
        self.eat('{')
        stmt_list = self.stmt_list()
        return ('block', stmt_list)
    
    def declare(self):
        self.eat('DataType')
        id_handful = [self.eat_id()]
        while self.peek() == ',':
            self.eat(',')
            id_handful.append(self.eat_id())
        return ('deckare', id_handful)

    def assign(self):
        id = self.eat_id()
        self.eat('=')
        expr = self.expr()
        return ('assign', id, expr)

    def expr(self):
        term = self.term()
        while self.peek() in ('+','-','*','/','%'):
            operator = self.eat()
            term2 = self.term()
            term = (operator, term, term2)
        return term
    
    def term(self):
        fact = self.fact()
        while self.peek() in ('*','/','%'):
            operator = self.eat()
            fact2 = self.fact()
            fact = (operator, fact2, fact)
        return fact

    def fact(self):
        if self.peek_type() == 'ID':
            return self.eat_id()
        elif self.peek_type() in ('INT_LIT', 'FLOAT_LIT'):
            return self.eat()
        else:
            self.eat('(')
            expr = self.expr()
            self.eat(')')
            return expr

    def bool_expr(self):
        bterm = self.bterm()
        while self.peek() in ('>','<','>=', '<='):
            operator = self.eat()
            bterm2 = self.bterm()
            bterm = (operator, bterm, bterm2)
        return bterm

    def bterm(self):
        booleanAnd = self.booleanAnd()
        while self.peek() in ('==', '!='):
            operator = self.eat()
            booleanAnd2= self.booleanAnd()
            booleanAnd = (operator, booleanAnd, booleanAnd2)
        return booleanAnd

    def booleanAnd(self):
        booleanOr = self.booleanOr()
        while self.peek() == '&&':
            self.eat('&&')
            booleanOr2 = self.booleanOr()
            booleanOr = ('&&', booleanOr, booleanOr2)
        return booleanOr
    
    def booleanOr(self):
        expr = self.expr()
        while self.peek() == '||':
            self.eat('||')
            expr2 = self.expr()
 

