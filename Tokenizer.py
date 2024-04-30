class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

class Tokenizer:
    def __init__(self):
        self.tokens = []

    def tokenize_expression(self, expression):
        self.tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char == '(':
                self.tokens.append(Token('LEFT_PAREN', '('))
            elif char == ')':
                self.tokens.append(Token('RIGHT_PAREN', ')'))
            elif char in ['+', '*', '^', '~']:
                operator_type = ''
                if char == '+':
                    operator_type = 'AND'
                elif char == '*':
                    operator_type = 'OR'
                elif char == '^':
                    operator_type = 'XOR'
                elif char == '~':
                    operator_type = 'NOT'
                self.tokens.append(Token(f'{operator_type} OPERATOR', char))
            elif char.isalpha() or char in ['0', '1']:
                self.tokens.append(Token('VARIABLE', char))
            else:
                raise ValueError(f"Invalid character '{char}' at position {i}. Only alphabets (a-z/A-Z) and '0' or '1' are allowed.")
            i += 1
        return self.tokens