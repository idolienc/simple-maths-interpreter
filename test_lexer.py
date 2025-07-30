from lexer import Lexer

def test_one():
    assert Lexer("2+2") == ["2", "+", "2"]