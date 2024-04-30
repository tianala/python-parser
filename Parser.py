from Tokenizer import Token, Tokenizer

class Parser:
    def __init__(self):
        self.tokenizer = Tokenizer()

    def parse_expression(self, expression):
        tokens = self.tokenizer.tokenize_expression(expression)
        simplified_tokens = self.simplify_tokens(tokens)
        simplified_expression = ''.join(token.value for token in simplified_tokens)
        return simplified_expression

    def simplify_tokens(self, tokens):
        # Applying simplification rules
        simplified_tokens = []
        i = 0
        while i < len(tokens):
            # Identity laws: A + 0 = A, A * 1 = A
            if tokens[i].value == '0' and tokens[i - 1].value in ['+', '^']:
                i += 1
                continue
            if tokens[i].value == '1' and tokens[i - 1].value in ['*', '^']:
                i += 1
                continue

            # Domination laws: A * 0 = 0, A + 1 = 1
            if tokens[i].value == '0' and tokens[i - 1].value == '*':
                simplified_tokens.pop()  # Remove the previous token
                simplified_tokens.append(Token('VARIABLE', '0'))
                i += 1
                continue
            if tokens[i].value == '1' and tokens[i - 1].value == '+':
                simplified_tokens.pop()  # Remove the previous token
                simplified_tokens.append(Token('VARIABLE', '1'))
                i += 1
                continue

            # Double negation law: ~~A = A
            if tokens[i].value == '~' and tokens[i + 1].value == '~':
                i += 2
                continue

            # Add the token to the simplified tokens list
            simplified_tokens.append(tokens[i])
            i += 1

        return simplified_tokens

def main():
    parser = Parser()
    expression = "a+b*(c^d)"
    simplified_expression = parser.parse_expression(expression)
    print("Simplified expression:", simplified_expression)

if __name__ == "__main__":
    main()
