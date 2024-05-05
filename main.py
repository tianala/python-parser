from Tokenizer import Tokenizer
from Parser import Parser
import os

def main():
    tokenizer = Tokenizer()
    os.system('cls') 
    expression = input("NOTE: only alphabets (a-z/A-Z) and '0' or '1' are allowed, ex. (~A & B) | (A & C)\ninput a boolean expression: ") # "A & ~D & (B | C)" 
    try: 
        tokens = tokenizer.tokenize_expression(expression)
        print("Tokens:")
        expression_list = []
        for token in tokens:
            if token.type.endswith("OPERATOR"):
                expression_list.append(token.value)
                print(f"{token.type.split()[0]} OPERATOR, '{token.value}'")
            else:
                expression_list.append(token.value)
                print(f"{token.type}, '{token.value}'")

        #print("Expression format:", expression_list)
        simplified_expression = Parser(expression_list)
        print("\nSimplified expression:", simplified_expression) 

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

