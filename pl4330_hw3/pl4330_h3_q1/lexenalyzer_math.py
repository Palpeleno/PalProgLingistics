import re

#Recognize a single token by pointing to the current object using the symbol and name of token, symbol is token type, value is the name
class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

#output 
    def __repr__(self):
        return f"({self.token_type}, '{self.value}')"

#file reader not working ?!something file not found when its path and name are right there!!
class Lexalyzer:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.text = f.read()

#tokens for math operation
    def tokenize(self):
        tokens = []
        regex_patterns = [
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

        combined_pattern = '|'.join('(?P<%s>%s)' % pair for pair in regex_patterns)
        token_regex = re.compile(combined_pattern)
        for match in token_regex.finditer(self.text):
            token_type = match.lastgroup
            token_value = match.group(token_type)
            tokens.append(Token(token_type, token_value))
        return tokens

#instance of lexalyzer class, not working, cant open file 
mrlexer = Lexalyzer('test.txt')
tokens = mrlexer.tokenize()
print(tokens)