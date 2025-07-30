def Lexer(equation):
    tokens = []
    DIGITS = "0123456789"
    store = ""
    decimal_count = 0
    operator_count = 0

    def tokenize_operators():
        nonlocal store, operator_count, decimal_count
        tokens.append(store)
        operator_count += 1
        if operator_count > 1:
            raise TypeError(f"Illegal characters entered, 2 or more operators are adjacent")
        else:
            tokens.append(character)
            store = ""
            operator_count = 0
            decimal_count = 0  

    for character in equation:

        if character in DIGITS:
            store += character

        elif character == ".":
            store += character
            decimal_count += 1
            if decimal_count > 1:
                raise TypeError(f"Illegal characters entered, a value contains 2 or more decimal points")
            
        elif character == " ":
            pass
        
        elif character == "+":
            tokenize_operators()

        elif character == "-":
            tokenize_operators()

        elif character == "*":
            tokenize_operators()

        elif character == "/":
            tokenize_operators()

    if store:
        tokens.append(store)

    return tokens