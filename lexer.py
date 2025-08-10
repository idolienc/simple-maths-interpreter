def Lexer(equation):
    tokens = []
    DIGITS = "0123456789"
    store = ""
    decimal_count = 0

    def tokenize_operators():
        nonlocal store, decimal_count
        tokens.append(store)
        tokens.append(character)
        store = ""
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
        
        elif character in "+-*/":
            if store == "":
                raise TypeError("Illegal characters entered, 2 or more operators are adjacent")
            tokenize_operators()

    if store:
        tokens.append(store)

    return tokens