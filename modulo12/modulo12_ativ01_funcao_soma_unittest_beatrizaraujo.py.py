import unittest


def somar(a, b):
    return a + b


class TesteSoma(unittest.TestCase):

    def test_soma(self):
        resultado = somar(2, 3)
        self.assertEqual(resultado, 5)


if __name__ == "__main__":
    unittest.main()