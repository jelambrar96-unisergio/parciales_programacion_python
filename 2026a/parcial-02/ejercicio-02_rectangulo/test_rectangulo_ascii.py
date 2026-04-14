"""
Tests para la función draw_rectangle usando unittest.
"""

import unittest
from rectangulo import Rectangulo
from rectangulo_ascii import draw_rectangle


class TestDrawRectangle(unittest.TestCase):
    """Clase de tests para la función draw_rectangle."""

    def test_canvas_simple_sin_rectangulo(self):
        """Test: Canvas vacío (rectángulo en (0,0,0,0))."""
        rect = Rectangulo(0, 0, 0, 0)
        canvas = draw_rectangle(3, 5, rect, "#")
        lineas = canvas.split("\n")
        self.assertEqual(len(lineas), 3)
        for linea in lineas:
            self.assertEqual(len(linea), 5)
            self.assertTrue(all(c == " " for c in linea))

    def test_rectangulo_llena_canvas_completo(self):
        """Test: Rectángulo que cubre todo el canvas."""
        rect = Rectangulo(0, 0, 5, 3)
        canvas = draw_rectangle(3, 5, rect, "#")
        lineas = canvas.split("\n")
        self.assertEqual(len(lineas), 3)
        for linea in lineas:
            self.assertEqual(linea, "#####")

    def test_rectangulo_pequeño_en_esquina_superior_izquierda(self):
        """Test: Rectángulo pequeño en la esquina superior izquierda."""
        rect = Rectangulo(0, 0, 2, 2)
        canvas = draw_rectangle(4, 5, rect, "X")
        lineas = canvas.split("\n")
        self.assertEqual(lineas[0], "XX   ")
        self.assertEqual(lineas[1], "XX   ")
        self.assertEqual(lineas[2], "     ")
        self.assertEqual(lineas[3], "     ")

    def test_rectangulo_en_centro(self):
        """Test: Rectángulo en el centro del canvas."""
        rect = Rectangulo(2, 1, 5, 3)
        canvas = draw_rectangle(5, 7, rect, "#")
        lineas = canvas.split("\n")
        self.assertEqual(len(lineas), 5)
        self.assertEqual(lineas[0], "       ")
        self.assertEqual(lineas[1], "  ###  ")
        self.assertEqual(lineas[2], "  ###  ")
        self.assertEqual(lineas[3], "       ")
        self.assertEqual(lineas[4], "       ")

    def test_rectangulo_con_simbolo_personalizado(self):
        """Test: Rectángulo con símbolo diferente."""
        rect = Rectangulo(1, 1, 3, 3)
        canvas = draw_rectangle(5, 5, rect, "+")
        lineas = canvas.split("\n")
        self.assertEqual(lineas[0], "     ")
        self.assertEqual(lineas[1], " ++  ")
        self.assertEqual(lineas[2], " ++  ")
        self.assertEqual(lineas[3], "     ")
        self.assertEqual(lineas[4], "     ")

    def test_rectangulo_linea_horizontal(self):
        """Test: Rectángulo que forma una línea horizontal (alto = 1)."""
        rect = Rectangulo(1, 2, 5, 3)
        canvas = draw_rectangle(4, 6, rect, "-")
        lineas = canvas.split("\n")
        self.assertEqual(lineas[0], "      ")
        self.assertEqual(lineas[1], "      ")
        self.assertEqual(lineas[2], " ---- ")
        self.assertEqual(lineas[3], "      ")

    def test_rectangulo_linea_vertical(self):
        """Test: Rectángulo que forma una línea vertical (ancho = 1)."""
        rect = Rectangulo(2, 1, 3, 4)
        canvas = draw_rectangle(5, 4, rect, "|")
        lineas = canvas.split("\n")
        self.assertEqual(lineas[0], "    ")
        self.assertEqual(lineas[1], "  | ")
        self.assertEqual(lineas[2], "  | ")
        self.assertEqual(lineas[3], "  | ")
        self.assertEqual(lineas[4], "    ")

    def test_rectangulo_con_numero_como_simbolo(self):
        """Test: Rectángulo con símbolo numérico."""
        rect = Rectangulo(0, 0, 3, 2)
        canvas = draw_rectangle(3, 4, rect, "1")
        lineas = canvas.split("\n")
        self.assertEqual(lineas[0], "111 ")
        self.assertEqual(lineas[1], "111 ")
        self.assertEqual(lineas[2], "    ")

    def test_canvas_grande_rectangulo_pequeño(self):
        """Test: Canvas grande con rectángulo pequeño."""
        rect = Rectangulo(5, 5, 7, 7)
        canvas = draw_rectangle(10, 10, rect, "#")
        lineas = canvas.split("\n")
        self.assertEqual(len(lineas), 10)
        for i, linea in enumerate(lineas):
            self.assertEqual(len(linea), 10)
            if i >= 5 and i < 7:
                self.assertEqual(linea, "     ##   ")
            else:
                self.assertTrue(all(c == " " for c in linea))

    def test_estructura_del_canvas(self):
        """Test: Verificar que la estructura del canvas es correcta."""
        rect = Rectangulo(1, 1, 3, 2)
        canvas = draw_rectangle(4, 5, rect, "O")
        lineas = canvas.split("\n")
        # Verificar número de líneas
        self.assertEqual(len(lineas), 4)
        # Verificar longitud de cada línea
        for linea in lineas:
            self.assertEqual(len(linea), 5)

    def test_rectangulo_en_esquina_inferior_derecha(self):
        """Test: Rectángulo en la esquina inferior derecha."""
        rect = Rectangulo(3, 2, 5, 4)
        canvas = draw_rectangle(4, 5, rect, "*")
        lineas = canvas.split("\n")
        self.assertEqual(lineas[0], "     ")
        self.assertEqual(lineas[1], "     ")
        self.assertEqual(lineas[2], "   **")
        self.assertEqual(lineas[3], "   **")

    def test_rectangulo_unitario(self):
        """Test: Rectángulo de una sola celda."""
        rect = Rectangulo(2, 2, 3, 3)
        canvas = draw_rectangle(5, 5, rect, "#")
        lineas = canvas.split("\n")
        self.assertEqual(lineas[0], "     ")
        self.assertEqual(lineas[1], "     ")
        self.assertEqual(lineas[2], "  #  ")
        self.assertEqual(lineas[3], "     ")
        self.assertEqual(lineas[4], "     ")

    def test_rectangulo_espacio_como_simbolo(self):
        """Test: Usar espacio como símbolo (visualización especial)."""
        rect = Rectangulo(1, 1, 3, 2)
        canvas = draw_rectangle(3, 5, rect, " ")
        lineas = canvas.split("\n")
        self.assertEqual(lineas[0], "     ")
        self.assertEqual(lineas[1], "     ")
        self.assertEqual(lineas[2], "     ")


if __name__ == "__main__":
    unittest.main()
