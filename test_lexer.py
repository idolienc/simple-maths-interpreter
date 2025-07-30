from lexer import Lexer
import pytest

def test_one():
    assert Lexer("2+2") == ["2", "+", "2"]

def test_two():
    assert Lexer("2.2+2") == ["2.2", "+", "2"]

def test_three():
    assert Lexer("2 + 2") == ["2", "+", "2"]

def test_four():
    assert Lexer("2-2*2/2") == ["2", "-", "2", "*", "2", "/", "2"]

def test_bad_input():
    with pytest.raises(TypeError):
        assert Lexer("2.2.2+2")

def test_multi_operators():
    with pytest.raises(TypeError):
        assert Lexer("2++2+2")