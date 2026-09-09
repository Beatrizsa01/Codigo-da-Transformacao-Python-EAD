import unittest


class Calculadora:

    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        return a / b


class TesteCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def test_somar(self):
        resultado = self.calculadora.somar(5, 3)
        self.assertEqual(resultado, 8)

    def test_dividir(self):
        resultado = self.calculadora.dividir(10, 2)
        self.assertEqual(resultado, 5)


if __name__ == "__main__":
    unittest.main()