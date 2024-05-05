class Token:
    def __init__(self, type, value=None):
        self.type = type  # Type of the token (e.g., VARIABLE, LEFT_PAREN)
        self.value = value  # Value of the token if applicable (e.g., the actual character)

class Tokenizer:
    def __init__(self):
        self.tokens = []  # List to store the tokens

    def tokenize_expression(self, expression):
        self.tokens = []  # Reset tokens list for each new expression
        tokens_with_spaces = expression.split()  # Split the expression by spaces to get individual tokens
        for token in tokens_with_spaces:  # Iterate through each token
            i = 0
            while i < len(token):
                char = token[i]  # Get the character at position i in the token
                if char == '(':
                    self.tokens.append(Token('LEFT_PAREN', '('))  # Add a LEFT_PAREN token
                elif char == ')':
                    self.tokens.append(Token('RIGHT_PAREN', ')'))  # Add a RIGHT_PAREN token
                elif char in ['+', '*', '~', '&', '|', '!']:  # Check if the character is an operator
                    operator_type = ''
                    if char in ['*', '&']:  # Check if the operator is AND
                        operator_type = 'AND'
                    elif char in ['+', '|']:  # Check if the operator is OR
                        operator_type = 'OR'
                    elif char in ['~', '!']:  # Check if the operator is NOT
                        operator_type = 'NOT'
                        
                    self.tokens.append(Token(f'{operator_type} OPERATOR', char))  # Add an operator token
                elif char.isalpha() or char in ['0', '1']:  # Check if the character is a variable (letter or digit)
                    self.tokens.append(Token('VARIABLE', char))  # Add a VARIABLE token
                else:
                    raise ValueError(f"Invalid character '{char}' in token '{token}'. Only alphabets (a-z/A-Z) and '0' or '1' are allowed.")
                i += 1  # Move to the next character in the token
        return self.tokens  # Return the list of tokens






from sympy.logic import simplify_logic

def Parser(tokens):
    simplified_exp = []  # List to store the simplified expression
    
    for item in tokens:  # Iterate through each token
        
        if item.isalnum():  # If the token is alphanumeric (a variable)
            simplified_exp.append(item)  # Add it to the simplified expression
            
        elif item == "!":  # If the token is '!'
            simplified_exp.append("~")  # Replace it with '~' (NOT)
            
        elif item == "+":  # If the token is '+'
            simplified_exp.append("|")  # Replace it with '|' (OR)
            
        elif item == "*":  # If the token is '*'
            simplified_exp.append("&")  # Replace it with '&' (AND)
            
        elif item == "~":  # If the token is '~'
            simplified_exp.append(item)  # Add it to the simplified expression (already '~' for NOT)
            
        elif item == "|":  # If the token is '|'
            simplified_exp.append(item)  # Add it to the simplified expression (already '|' for OR)
            
        elif item == "&":  # If the token is '&'
            simplified_exp.append(item)  # Add it to the simplified expression (already '&' for AND)
            
        elif item == "(":  # If the token is '('
            simplified_exp.append(item)  # Add it to the simplified expression
            
        elif item == ")":  # If the token is ')'
            simplified_exp.append(item)  # Add it to the simplified expression

    simplified_exp = ''.join(simplified_exp)  # Join the simplified expression into a string
    return simplify_logic(simplified_exp)  # Return the simplified expression after applying logical simplification






from Tokenizer import Tokenizer  # Import the Tokenizer class from Tokenizer.py
from Parser import Parser  # Import the Parser function from Parser.py
import os  # Import the os module for clearing the screen

def main():
    tokenizer = Tokenizer()  # Instantiate a Tokenizer object
    os.system('cls')  # Clear the screen (works on Windows systems)

    # Prompt the user to input a boolean expression
    expression = input("NOTE: only alphabets (a-z/A-Z) and '0' or '1' are allowed, ex. (~A & B) | (A & C)\ninput a boolean expression: ")

    try:
        tokens = tokenizer.tokenize_expression(expression)  # Tokenize the input expression
        print("Tokens:")  
        expression_list = []  # List to store the expression as tokens
        for token in tokens:  # Iterate through each token
            if token.type.endswith("OPERATOR"):  # If the token is an operator
                expression_list.append(token.value)  # Append the operator to the expression list
                print(f"{token.type.split()[0]} OPERATOR, '{token.value}'")  # Print the operator type and value
            else:
                expression_list.append(token.value)  # Append the non-operator token to the expression list
                print(f"{token.type}, '{token.value}'")  # Print the token type and value

        simplified_expression = Parser(expression_list)  # Parse and simplify the expression
        print("\nSimplified expression:", simplified_expression)  # Print the simplified expression

    except ValueError as e:
        print("Error:", e)  # Print any error that occurs during tokenization or parsing

if __name__ == "__main__":
    main()  # Call the main function if this script is executed directly
