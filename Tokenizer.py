import re

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

class Tokenizer:
    def __init__(self):
        self.tokens = []

    def tokenize_expression(self, expression):
        self.tokens = []
        tokens = re.findall(r'\(|\)|[+*^~]|[A-Za-z]+', expression)
        for token in tokens:
            if token == '(':
                self.tokens.append(Token('LEFT_PAREN', '('))
            elif token == ')':
                self.tokens.append(Token('RIGHT_PAREN', ')'))
            elif token in ['+', '*', '^', '~']:
                operator_type = ''
                if token == '+':
                    operator_type = 'AND'
                elif token == '*':
                    operator_type = 'OR'
                elif token == '^':
                    operator_type = 'XOR'
                elif token == '~':
                    operator_type = 'NOT'
                self.tokens.append(Token(f'{operator_type} OPERATOR', token))
            else:
                self.tokens.append(Token('VARIABLE', token))
        return self.tokens
