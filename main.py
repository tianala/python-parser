from Tokenizer import Tokenizer
import os


def main():
    tokenizer = Tokenizer()
    os.system('cls') #"(~A+B)^(A+C)"
    expression = input("NOTE: avoid spaces and only alphabets (a-z/A-Z) and '0' or '1' are allowed, ex. (~A+B)^(A+C)\ninput a boolean expression: ")
    try:
        tokens = tokenizer.tokenize_expression(expression)
        print("Tokens:")
        for token in tokens:
            if token.type.endswith("OPERATOR"):
                print(f"{token.type.split()[0]} OPERATOR, '{token.value}'")
            else:
                print(f"{token.type}, '{token.value}'")

    except ValueError as e:
        print("Error:", e)
if __name__ == "__main__":
    main()
