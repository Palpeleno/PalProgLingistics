import re

print()

    #1
class Token:
    def __init__(self, value: int, tokens: str ):
        self.lexem = tokens
        self.value = value
            #constructor for Token object 
            #accepts string to represent the tokens of token and symbol for token code
        tokens = [
        (r'➕', 'ADD'),
        (r'➖', 'SUBTRACT'),
        (r'✖️', 'MULTIPLY'),
        (r'➗d', 'DIVIDE'),
        (r'%', 'MODULO'),
        (r'\(', 'LEFT_PAREN'),
        (r'\)', 'RIGHT_PAREN'),
        (r'→', 'ASSIGNMENT'),
        (r'==', 'EQUALS'),
        (r'<', 'LESS_THAN'),
        (r'≤', 'LESS_THAN_EQUAL'),
        (r'>', 'GREATER_THAN'),
        (r'≥', 'GREATER_THAN_EQUAL'),
        (r'&', 'LOGICAL_AND'),
        (r'\|', 'LOGICAL_OR'),
        (r'[_a-zA-Z][_a-zA-Z0-9]*', 'IDENTIFIER'),
        (r'[-+]?[0-9]*\.?[0-9]+', 'NUMBER')
        ]

    #2
class PalLangComp:
    def __init__(self ):
        pass
    
    def read_input_file(self, file: str) -> str:
        with open(file, "r") as f:
            input_string = f.read()
            
        extLex = Lexer()


    #3
class Lexer:
    def __init__(self, input_str:str ):
        self.input_str = input_str 
        self.tokens = []
        self.place_of_intrest = 0    # place_of_intrest = place of intrest as said in most fps open world games 

    def tokenize(self) -> list[Token]:
        
        #tracker for current element in the string and checks if at EOL
        while self.place_of_intrest < len (self.input_str):
            current_char = self.input_str[self.place_of_intrest]
        
        #ignore single line comment
        if current_char == '#' and self.place_of_intrest + 1 < len(self.input_str) and self.input_str[self.place_of_intrest + 1] == '#':
            end_of_line = self.input_str.find('\n', self.place_of_intrest)
            if end_of_line == -1:
                breakpoint
            self.place_of_intrest = end_of_line + 1
            
        #ignore block comment
        if current_char == '#' and self.place_of_intrest + 1 < len(self.input_str) and self.input_str[self.place_of_intrest + 1] == '*':
            end_of_comment = self.input_str.find('\n', self.place_of_intrest)
            if end_of_comment == -1:
                breakpoint
            self.place_of_intrest = end_of_comment + 2
                    
        #check for token
        if current_char.isaplpha():
            end_pos = self.place_of_intrest + 1
            while end_pos < len(self.input_str) and self.input_str[end_pos].isalnum():
                end_pos += 1
            tokens = self.input_str[self.place_of_intrest:end_pos]
            self.tokens.append(Token(tokens, 10)) # for identifiers 
            self.place_of_intrest = end_pos
        elif current_char.isadigit():
            end_pos = self.place_of_intrest + 1
            while end_pos < len(self.input_str) and self.input_str[end_pos].isadigit():
                end_pos += 1
                tokens = self.input_str[self.place_of_intrest:end_pos]
                self.tokens.append(Token(tokens, 20)) # #20 for integers
                self.place_of_intrest = end_pos
            else:
                self.place_of_intrest += 1       
                return self.tokens
        
        
        #check for real literals
        if current_char.isdigit():
            end_pos = self.place_of_intrest + 1
            while end_pos < len(self.input_str) and self.input_str[end_pos].isdigit():
                end_pos += 1
            if end_pos < len(self.input_str) and self.input_str[end_pos] == '.':
                end_pos += 1
                while end_pos < len(self.input_str) and self.input_str[end_pos].isdigit():
                    end_pos += 1
                tokens = self.input_str[self.place_of_intrest:end_pos]
                self.tokens.append(Token(tokens, 30)) # Code 30 for real literals
                self.place_of_intrest = end_pos
                
                
        #check for bool literals
        if self.input_str[self.current_pos:self.current_pos+4] == 'true':
            self.tokens.append(Token('true', 50)) # Code 50 for bool literals
            self.current_pos += 4
                
        elif self.input_str[self.current_pos:self.current_pos+5] == 'false':
            self.tokens.append(Token('false', 50)) # Code 50 for bool literals
            self.current_pos += 5
                
        
        #check for char literals
        if current_char == "'" and self.current_pos + 2 < len(self.input_str) and self.input_str[self.current_pos + 2] == "'":
            if self.input_str[self.current_pos + 1] == '\\':
                # Check for escape character
                if self.input_str[self.current_pos + 3] in ('\\', '\'', '\"', 'n', 'r', 't', 'b', 'f'):
                    tokens = self.input_str[self.current_pos:self.current_pos + 4]
                    self.tokens.append(Token(tokens, 13)) # Code 13 for char_literal
                    self.current_pos += 4
                else:
                    tokens = self.input_str[self.current_pos:self.current_pos + 3]
                    self.tokens.append(Token(tokens, 13)) # Code 13 for char_literal
                    self.current_pos += 3
                    
        
        #check for string literals
        if current_char == '"': # string literal
            string_literal = self._get_string_literal()
            self.tokens.append(Token(string_literal, 40)) # string literal code
            self._skip_whitespace()


    # from exam 1 and hw3 
    def is_valid_flotingP(str):
        floatingplace_of_intrestntPattern = r'^[+-]?(\d+\.\d*)|\.\d+)([eE]\d+)?$'
        return bool(re.match(floatingplace_of_intrestntPattern, str))


        #10 lets you know if a string is an integer literal or not.
    def is_valid_integerConstant(str):
        integerconstantpattern = r'^[+-]?\d+$'
        return bool(re.match(integerconstantpattern, str))

        #14 determine if a string matches even number of a’s and an odd number of b’s followed by any number of c’s or d’s OR a pattern of even occurrences of the string ‘cbad
    def is_valid_EaOb(name):
        patternEaOb = '(aa|bb|aabb |abab| abba | baba |baab |bbaa)b| b(aa|bb|aabb |abab| abba | baba |baab |bbaa)| (aa|bb|aabb |abab| abba | baba |baab |bbaa)b(aa|bb|aabb |abab| abba | baba |baab |bbaa) ie evenAB = (aa|bb|aabb |abab| abba | baba |baab |bbaa)* b(evenAB) | (evenAB)b | evenAB (b) evenAB'
        return re.match(patternEaOb, name) is not None

        #a regular expression to see if a string could be a variable, class, or method
    def is_valid_name(name):
        pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
        return re.match(pattern, name) is not None




        # combined_pattern = '|'.join('(?P<%s>%s)' % pair for pair in regex_patterns)
        # token_regex = re.compile(combined_pattern)
        # for match in token_regex.finditer(self.text):
        #     token_type = match.lastgroup
        #     token_value = match.group(token_type)
        #     tokens.append(Token(token_type, token_value))
        # return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        
    def parse (self):
        parse_tree = []
        while self.current_token_index < len(self.tokens):
            statement = self.statement()
            if statement is not None:
                parse_tree.append(statement)
        return parse_tree
    
    def statement(self):
        token = self.peek_token()
        if token.tokens == "{":
            return self.block()
        elif token.tokens == "if":
            return self.if_stmt()
        elif token.tokens == "while":
            return self.while_loop()
        elif token.tokens == "let":
            return self.declare()
        elif token.token_code == Token.IDENTIFIER:
            return self.assign()
        elif token.tokens == "function":
            return self.function()
        else:
            self.raise_parse_error("Expected a statement")
            
    def stmt_list(self):
        self.match('{')
        while self.tokens[self.index] != '}':
            self.stmt()
            self.match(';')
        self.match('}')

    def while_loop(self):
        self.expect_token("while")
        self.expect_token("(")
        condition = self.expression()
        self.expect_token(")")
        loop_block = self.statement()
        return ("LOOP", condition, loop_block)

    
    def if_stmt(self):
        self.expect_token("if")
        self.expect_token("(")
        condition = self.expression()
        self.expect_token(")")
        then_block = self.statement()
        else_block = None
        if self.peek_token().tokens == "else":
            self.advance_token()
            else_block = self.statement()
        return ("SELECTION", condition, then_block, else_block)

    def block(self):
        self.expect_token("{")
        statements = []
        while self.peek_token().tokens != "}":
            statement = self.statement()
            if statement is not None:
                statements.append(statement)
        self.expect_token("}")
        return ("CODE_BLOCK", statements)
    
    def declare(self):
        self.expect_token("let")
        name = self.expect_identifier()
        self.expect_token("=")
        value = self.parse_expression()
        return ("DECLARATION", name, value)

    def assign(self):                           
        name = self.expect_identifier()
        self.expect_token("=")
        value = self.expression()
        return ("ASSIGNMENT", name, value)

    def function(self):
        self.expect_token("function")
        name = self.expect_identifier()
        self.expect_token("(")
        parameters = []
        while self.peek_token().tokens != ")":
            param = self.expect_identifier()
            parameters.append(param)
            if self.peek_token().tokens == ",":
                self.advance_token()
        self.expect_token(")")
        function_block = self.statement()
        return ("FUNCTION", name, parameters, function_block)

    def expression(self):
        return self.logical_expression()
    
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
        left = self.boolTerm()
        while self.tokens[self.index] in ('>','<','>=', '<='): 
            self.match(self.tokens[self.index])
            self.boolTerm()
        return left

    def boolTerm(self):
        left = self.boolTerm()
        while self.peek_token().tokens in ["==", "!="]:
            operator = self.advance_token().tokens
            right = self.boolTerm()
            left = ("EQUALITY_EXPRESSION", operator, left, right)
        return left
    
    def logical_expression(self):
        left = self.equality_expression()
        while self.peek_token().tokens in ["and", "or"]:
            operator = self.advance_token().tokens
            right = self.equality_expression()
            left = ("LOGICAL_EXPRESSION", operator, left, right)
        return left
    
    def equality_expression(self):
        left = self.boolTerm()
        while self.peek_token().tokens in ["==", "!="]:
            operator = self.advance_token().tokens
            right = self.boolTerm()
            left = ("EQUALITY_EXPRESSION", operator, left, right)
        return left

            
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


        
        
palLangComp = PalLangComp()
palLangComp.read_input_file("final_test.txt")