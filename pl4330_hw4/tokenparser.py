def tokenize(self):

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
        Token('➖', 'SUBTRACT'),
        Token('➕', 'ADD'),
        Token('✖️', 'MULTIPLY'),
        Token('➗d', 'DIVIDE'),
        Token('%', 'MODULO'),
        Token('\(', 'LEFT_PAREN'),
        Token('\)', 'RIGHT_PAREN'),
        Token('→', 'ASSIGNMENT'),
        Token('==', 'EQUALS'),
        Token('<', 'LESS_THAN'),
        Token('≤', 'LESS_THAN_EQUAL'),
        Token('>', 'GREATER_THAN'),
        Token('≥', 'GREATER_THAN_EQUAL'),
        Token('&', 'LOGICAL_AND'),
        Token('\|', 'LOGICAL_OR'),
        Token('[_a-zA-Z][_a-zA-Z0-9]*', 'IDENTIFIER'),
        Token('[-+]?[0-9]*\.?[0-9]+', 'NUMBER')
    ]

