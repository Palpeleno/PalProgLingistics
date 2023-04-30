import re


class Token:
    def __init__(self, value, lexem):
        self.lexem = lexem
        self.value = value


class PalLangComp:
    def __init__(self, file, index ):
        self.file = file 
        self.index = 0
        file = open("final_test.txt"," r")
        index = file.read()
        index = data.split("\n")
        
        print(data_into_list)
        my_file.close()
        
        #something from file should = a string 
        print(index)

        extLex = Lexer()


    
class Lexer:
    def __init__(self,tokens ):
        self.self = self
        self.tokens = [Token]

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


    # from exam 1 and hw3 
    def is_valid_flotingP(str):
        floatingPointPattern = r'^[+-]?(\d+\.\d*)|\.\d+)([eE]\d+)?$'
        return bool(re.match(floatingPointPattern, str))


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
        
        
        #Develop a Lexer class: (Code 10, defintions 5) 
        # a. An instant of this class should exist In the Complier Class 
        # b. Takes in a string in its constructor 
        # c. Converts a string into a list of Token object if there exist no errors 
        #  i. Should ignore block comments 
        #  ii. Should ignore single line commentsd. 
        #      Should contain the following tokens and clear patterns or automata to