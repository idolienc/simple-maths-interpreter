from lexer import Lexer
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
    assert Lexer(equation) == tokens
    
@pytest.mark.parametrize(
    "equation, error",
    [
        ("2.2.2+2", SyntaxError),
        ("2++2+2", SyntaxError),
    ]
)
def test_errors(equation, error):
    with pytest.raises(error):
        assert Lexer(equation)