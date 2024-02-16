import unittest
import pytest
from app import carre, cube

class TestCarre(unittest.TestCase):
    def test_resultat(self):
        valeur = 2
        attendu = 4
        self.assertEqual(carre(2), 4)
        self.assertEqual(carre(3), 9)
        self.assertEqual(carre(4), 16)
        self.assertEqual(carre(7), 49)

    def test_cube(self):
        pass  # Ajoutez votre code de test ici

if __name__ == "__main__":
    unittest.main()