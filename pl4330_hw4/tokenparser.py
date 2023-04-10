tokens = [
    Token('IF', 'if'),
    Token('LPAREN', '('),
    Token('ID', 'x'),
    Token('GT', '>'),
    Token('INT_LIT','0'),
    Token('RPAREN', ')'),
    Token('LBRACE','{'),
    Token('ID', 'x'),
    Token('ASSIGN', '='),
    Token('ID', 'y'),
    Token('SEMICOLON', ';'),
    Token('RBRACE', '}')
]

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