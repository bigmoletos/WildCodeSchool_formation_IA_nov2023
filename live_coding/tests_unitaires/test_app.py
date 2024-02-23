import unittest
from app import carre, cube

class TestCarre(unittest.TestCase):
    def test_resultat(self):
        valeur = 2
        attendu = 4
        self.assertEqual(carre(2), 4)
        self.assertEqual(carre(3), 9)
        self.assertEqual(carre(4), 16)
        self.assertEqual(carre(7), 49)

 def test_cube(self)





class TestCube(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cube(2), 8)
        self.assertEqual(cube(3), 27)
        self.assertEqual(cube(4), 64)
        self.assertEqual(cube(5), 125)

if __name__ == "__main__":
    unittest.main()