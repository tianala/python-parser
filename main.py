from Tokenizer import Tokenizer

def main():
    tokenizer = Tokenizer()
    expression = "a+b*(c^9)"
    try:
        tokens = tokenizer.tokenize_expression(expression)
        print("Tokens:")
        for token in tokens:
            if token.type.endswith("OPERATOR"):
                print(f"{token.type.split()[0]} OPERATOR '{token.value}'")
            else:
                print(f"{token.type} '{token.value}'")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
