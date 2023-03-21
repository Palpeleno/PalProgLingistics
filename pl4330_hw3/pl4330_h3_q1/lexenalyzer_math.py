import re

#token for regular expression
#check if the reg exp are correct from the notion sheet
TOKEN_REGEX = [
    (r'[+-]', 'ADDOP'),
    (r'[*/%]', 'MULOP'),
    (r'[()]', 'GROUPING'),
    (r'=', 'ASSIGN'),
    (r'==', 'EQ'),
    (r'<', 'LT'),
    (r'<=', 'LTE'),
    (r'>', 'GT'),
    (r'>=', 'GTE'),
    (r'&&', 'AND'),
    (r'\|\|', 'OR'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),
    (r'\d+\.\d+', 'FLOAT'),
    (r'\d+', 'INT')
]

# present the tokens in to a input string of a list of tokens 
def tokenize(input_string):
    tokens = []
    while len(input_string) > 0:
        match = None
        for token_regex in TOKEN_REGEX:
            pattern, tag = token_regex
            regex = re.compile('^' + pattern)
            match = regex.search(input_string)
            if match:
                value = match.group(0)
                tokens.append((value, tag))
                input_string = input_string[len(value):]
                break
        if not match:
            raise Exception('Invalid input string')
    return tokens



#test/ex
input_string = "x = 2"
tokens = tokenize(input_string)
print(tokens)