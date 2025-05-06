"""
Alexis López Riera
Entorns de desenvolupament 
Tests de la Llibreria de funcions matemàtiques (Pytest)
"""  
from math_lib import *
import pytest

# def test_1():
#     resultat = calcula_mitjana([10, 10, 10])
#     assert resultat == 10

# def test_2():
#     resultat = calcula_mitjana([5, 3, 4])
#     assert resultat == 4.0

@pytest.mark.parametrize("llista, res_esperat",[([10, 10, 10],10),([5, 3, 4],4)])
def test_mitjana(llista,res_esperat):
    resultat = calcula_mitjana(llista)
    assert resultat == res_esperat

# @pytest.mark.parametrize("test_input, expected_output", [("2+2", 4), ("2-2", 0), ("2*2", 4), ("2/2", 1.0)])
# def test_eval(test_input, expected_output):
#     assert eval(test_input) == expected_output

# def test_in():
#     assert 1 == [1, 2, 3]

# def test_is():
#     a = [1, 2, 3]
#     b = a
#     assert a == b

# def test_upper():
#     assert 'foo'.upper() == 'FOO'

# def test_isupper():
#     assert 'FOO'.isupper()
#     assert 'Foo'.isupper()