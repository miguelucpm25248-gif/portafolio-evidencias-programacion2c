import unittest
from parcial2.CalculadoraBasica import suma, resta, multi, div

class testOperaciones(unittest.TestCase):

    def test_suma_positivo(self):
        self.assertEqual(suma(300,3),303)

    def test_suma_negativos(self):
        self.assertEqual(suma(-4,-6), -10)

    def test_resta_basica(self):
        self.assertEqual(resta(10,5), 5)

    def test_resta_negativa(self):
        self.assertEqual