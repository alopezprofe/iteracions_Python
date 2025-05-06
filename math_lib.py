"""
Alexis López Riera
Entorns de desenvolupament 
Llibreria de funcions matemàtiques
"""   
import doctest
def suma(a, b):
    """
    Retorna la suma de dos nombres.
    >>> suma(2, 3)
    5
    >>> suma(2, -5)
    -3
    """
    return a + b

def resta(a, b):
    """
    Retorna la resta de dos nombres.
    >>> resta(2, 3)
    -1
    >>> resta(5, 3)
    2
    """
    return a - b

def multiplica(a, b):
    """
    Retorna el producte de dos nombres.
    >>> multiplica(2, 3)
    6
    >>> multiplica(-2, 3)
    -6
    """
    return a * b

def divideix(a, b):
    """
    Retorna la divisió de dos nombres.
    >>> divideix(2, 3)
    0.6666666666666666
    >>> divideix(0, 2)
    0.0
    """
    return a / b

def calcula_mitjana(*args):
    return(sum(*args)/len(*args))

if __name__ == "__main__":
    #print(doctest.testmod()) 
    assert(calcula_mitjana([3, 7, 5]) == 6.0)
    assert(calcula_mitjana([30, 0]) == 15.0)