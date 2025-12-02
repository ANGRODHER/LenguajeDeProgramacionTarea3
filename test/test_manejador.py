import unittest
from manejador_tipos import ManejadorTipos

class TestManejadorTipos(unittest.TestCase):
    def setUp(self):
        self.manejador = ManejadorTipos()
        self.manejador.definir_atomico("char", 1, 1)
        self.manejador.definir_atomico("int", 4, 4)

    def test_atomico(self):
        self.assertEqual(self.manejador.describir("char")["sin_empaquetar"]["tamaño"], 1)
        self.assertEqual(self.manejador.describir("int")["sin_empaquetar"]["alineación"], 4)

    def test_struct(self):
        self.manejador.definir_struct("foo", ["char", "int"])
        resultados = self.manejador.describir("foo")
        self.assertEqual(resultados["sin_empaquetar"]["tamaño"], 8)
        self.assertEqual(resultados["empaquetado"]["tamaño"], 5)
        self.assertEqual(resultados["reordenado"]["tamaño"], 8)

    def test_union(self):
        self.manejador.definir_union("bar", ["char", "int"])
        resultados = self.manejador.describir("bar")
        self.assertEqual(resultados["sin_empaquetar"]["tamaño"], 4)

if __name__ == "__main__":
    unittest.main()
