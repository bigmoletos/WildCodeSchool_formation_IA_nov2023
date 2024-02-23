#  doc test
import doctest
import pytest
import time
doctest.testmod()


def carre(nbre):
    '''
    Cette fonction prend un nombre en entrée et retourne son carré.

    >>> carre(2)
    4
    >>> carre(3)
    9
    >>> carre(4)
    16
    '''
    return nbre*nbre




