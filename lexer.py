def lex(equation):
    tokens = []
    DIGITS = "0123456789"
    store = ""
    decimal_count = 0

    def flush_store():
        nonlocal store, decimal_count
        if store:
            tokens.append(store)
            store = ""
            decimal_count = 0

    equation = equation.strip()

    for character in equation:
        if character in DIGITS:
            store += character

        elif character == ".":
            store += character
            decimal_count += 1
            if decimal_count > 1:
                raise SyntaxError("Illegal characters entered, a value contains 2 or more decimal points")

        elif character == " ":
            flush_store()

        elif character in "+-*/":
            if not store and (not tokens or tokens[-1] in "+-*/"):
                raise SyntaxError("Illegal characters entered, 2 or more operators are adjacent")
            flush_store()
            tokens.append(character)

        else:
            raise SyntaxError(f"Illegal character: {character}")

    flush_store()
    return tokens
