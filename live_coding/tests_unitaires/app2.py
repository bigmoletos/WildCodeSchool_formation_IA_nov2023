


def cube(nbre):
    '''
    Cette fonction prend un nombre en entrée et retourne son cube.

    >>> carre(2)
    8
    >>> carre(3)
    81
    >>> carre(4)
    343
    '''
    valeur=int(input("indiquez un nombre"))
    return nbre*nbre*nbre





def test_cube(monkeypatch):
    # Cette fonction sera utilisée pour remplacer 'input'
    def mock_input(prompt):
        return '2'

    # Utilisez monkeypatch pour remplacer 'input' par 'mock_input'
    monkeypatch.setattr('builtins.input', mock_input)

    # Testez la fonction 'cube'
    assert cube(2) == 8