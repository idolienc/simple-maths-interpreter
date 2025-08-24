from lexer import lex
import pytest

@pytest.mark.parametrize(
        "equation, tokens",
        [
            ("2 + 2", ["2", "+", "2"]),
            ("2.2 + 2", ["2.2", "+", "2"]),
            ("2-2*2/2", ["2", "-", "2", "*", "2", "/", "2"])
        ]
)
def test_basic_equation(equation, tokens):
    assert lex(equation) == tokens
    
@pytest.mark.parametrize(
    "equation, error",
    [
        ("2.2.2+2", SyntaxError),
        ("2++2+2", SyntaxError),
    ]
)
def test_errors(equation, error):
    with pytest.raises(error):
        assert lex(equation)