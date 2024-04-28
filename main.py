from Tokenizer import Tokenizer
from Parser import Parser

tokenizer = Tokenizer()
parser = Parser()

expression = input("Enter the boolean expression: ")  # "(A + B) * (~C ^ D)"
tokens = tokenizer.tokenize_expression(expression)
tokenized_list = [(token.type, token.value) for token in tokens]
print("Tokenized expression:")
for token_type, token_value in tokenized_list:
    print(f"Type: {token_type}, Value: {token_value}")

result = parser.parse_expression(tokens)
print("Simplified expression result:", result)
