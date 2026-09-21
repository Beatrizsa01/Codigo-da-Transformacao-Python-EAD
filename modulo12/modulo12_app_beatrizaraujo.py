import unittest


class Calculadora:

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")

        return a / b


class TesteCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calculadora.dividir(10, 0)


if __name__ == "__main__":
    unittest.main()