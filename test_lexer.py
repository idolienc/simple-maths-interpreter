from lexer import Lexer
import pytest

def test_basic_equation():
    assert Lexer("2+2") == ["2", "+", "2"]

def test_decimals():
    assert Lexer("2.2+2") == ["2.2", "+", "2"]

def test_whitespace():
    assert Lexer("2 + 2") == ["2", "+", "2"]

def test_operators():
    assert Lexer("2-2*2/2") == ["2", "-", "2", "*", "2", "/", "2"]

def test_multi_dps():
    with pytest.raises(TypeError):
        assert Lexer("2.2.2+2")

def test_multi_operators():
    with pytest.raises(TypeError):
        assert Lexer("2++2+2")