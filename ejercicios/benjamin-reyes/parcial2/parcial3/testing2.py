def suma(a,b):
    return a + b

import unittest

class testSuma(unittest.TestCase):
    def test_suma_positiva(self):
        self.assertEqual(suma(2,3), 5)

    def test_suma_negativa(self):
        self.assertEqual(suma(-2,-3),-5)

    def test_suma_mixta(self):
        self.assertEqual(suma(-2, 3),1)

        if __name__ == ´__main__