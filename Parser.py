class Parser:
    def __init__(self):
        self.operations = {'+': lambda x, y: x or y, '*': lambda x, y: x and y, '^': lambda x, y: x != y, '~': lambda x: not x}

    def parse_expression(self, tokens):
        result = self._expression(tokens)
        return result

    def _expression(self, tokens):
        stack = []
        for token in tokens:
            if token.type == 'OPERATOR':
                if token.value == '~':
                    operand = stack.pop()
                    stack.append(self.operations[token.value](operand))
                else:
                    right_operand = stack.pop()
                    left_operand = stack.pop()
                    stack.append(self.operations[token.value](left_operand, right_operand))
            else:
                stack.append(token.value)
        if stack:
            return stack[-1]
        else:
            return None