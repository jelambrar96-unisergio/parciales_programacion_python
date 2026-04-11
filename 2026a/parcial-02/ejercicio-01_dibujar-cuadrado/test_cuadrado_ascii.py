"""
Tests para la función dibujar_cuadrado usando unittest.
"""

import unittest
from cuadrado_ascii import dibujar_cuadrado


class TestDibujarCuadrado(unittest.TestCase):
    """Clase de tests para la función dibujar_cuadrado."""

    def test_lado_cero(self):
        """Test 1: Debe devolver una cadena vacía cuando el lado es cero."""
        resultado = dibujar_cuadrado(0, "*")
        self.assertEqual(resultado, "")

    def test_lado_uno(self):
        """Test 2: Debe devolver un único símbolo cuando el lado es 1."""
        resultado = dibujar_cuadrado(1, "*")
        self.assertEqual(resultado, "*")

    def test_cuadrado_almohadilla(self):
        """Test 3: Debe devolver un cuadrado con símbolos #."""
        resultado = dibujar_cuadrado(3, "#")
        esperado = "###\n###\n###"
        self.assertEqual(resultado, esperado)

    def test_cuadrado_cinco_espaciado(self):
        """Test 4: Debe devolver un cuadrado de 5x5 con espacios como separadores."""
        resultado = dibujar_cuadrado(5, "*", separador=" ")
        esperado = "* * * * *\n* * * * *\n* * * * *\n* * * * *\n* * * * *"
        self.assertEqual(resultado, esperado)

    def test_cuadrado_dos_por_dos(self):
        """Test adicional: Debe devolver un cuadrado de 2x2."""
        resultado = dibujar_cuadrado(2, "+")
        esperado = "++\n++"
        self.assertEqual(resultado, esperado)

    def test_cuadrado_cuatro_sin_separador(self):
        """Test adicional: Debe devolver un cuadrado de 4x4 sin separador."""
        resultado = dibujar_cuadrado(4, "X")
        esperado = "XXXX\nXXXX\nXXXX\nXXXX"
        self.assertEqual(resultado, esperado)

    def test_separador_guion(self):
        """Test adicional: Debe usar el separador personalizado."""
        resultado = dibujar_cuadrado(3, "*", separador="-")
        esperado = "*-*-*\n*-*-*\n*-*-*"
        self.assertEqual(resultado, esperado)

    def test_simbolo_numerico(self):
        """Test adicional: Debe funcionar con caracteres numéricos."""
        resultado = dibujar_cuadrado(3, "1")
        esperado = "111\n111\n111"
        self.assertEqual(resultado, esperado)

    def test_cuadrado_grande(self):
        """Test adicional: Debe funcionar con cuadrados más grandes."""
        resultado = dibujar_cuadrado(6, "=")
        lineas = resultado.split("\n")
        self.assertEqual(len(lineas), 6)
        for linea in lineas:
            self.assertEqual(linea.count("="), 6)


if __name__ == "__main__":
    unittest.main()
