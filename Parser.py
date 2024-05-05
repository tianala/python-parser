from sympy.logic import simplify_logic

def Parser(tokens):
    simplified_exp = []
    
    for item in tokens:
        
        if item.isalnum():
            simplified_exp.append(item)
            
        elif item == "!":
            simplified_exp.append("~")
            
        elif item == "+":
            simplified_exp.append("|")
            
        elif item == "*":
            simplified_exp.append("&")
            
        elif item == "~":
            simplified_exp.append(item)
            
        elif item == "|":
            simplified_exp.append(item)
            
        elif item == "&":
            simplified_exp.append(item)
            
        elif item == "(":
            simplified_exp.append(item)
            
        elif item == ")":
            simplified_exp.append(item)

    simplified_exp = ''.join(simplified_exp)
    return simplify_logic(simplified_exp)



# def main():
#     # Example usage
#     tokens = ["A", "*", "(", "B", "+", "C", ")", "*", "~", "D"]
#     simplified_expression = Parser(tokens)
#     print("Original expression:", ''.join(tokens))
#     print("Simplified expression:", simplified_expression)
    
# if __name__ == "__main__":
#     main()

