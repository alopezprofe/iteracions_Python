import doctest 

def recorrer_l(l):
    """
    Funció que recorre una llista de nombres i retorna la
    suma total dels números parells. Ignora els imparells.
    >>> recorrer_l([3, 4, 7, 2, 8, 9, 5, 1, 12])
    26
    """
    suma = 0
    for el in l:
        if el % 2 == 0:
            suma += el  
    return suma

def recorrer_l_comp(l):
    """
    Funció que recorre una llista de nombres i retorna la
    suma total dels números parells. Ignora els imparells.
    >>> recorrer_l_comp([3, 4, 7, 2, 8, 9, 5, 1, 12])
    26
    """ 
    return sum([el for el in l if el % 2 == 0])

if __name__ == "__main__":
    doctest.testmod(verbose=True)