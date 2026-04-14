"""
Tests para la clase Rectangulo usando unittest.
"""

import unittest
from rectangulo import Rectangulo


class TestRectangulo(unittest.TestCase):
    """Clase de tests para la clase Rectangulo."""

    def test_inicializacion_valores_por_defecto(self):
        """Test: Inicialización con valores por defecto (0, 0, 0, 0)."""
        rect = Rectangulo()
        self.assertEqual(rect.x0, 0)
        self.assertEqual(rect.y0, 0)
        self.assertEqual(rect.x1, 0)
        self.assertEqual(rect.y1, 0)

    def test_inicializacion_valores_personalizados(self):
        """Test: Inicialización con valores personalizados."""
        rect = Rectangulo(1, 2, 5, 8)
        self.assertEqual(rect.x0, 1)
        self.assertEqual(rect.y0, 2)
        self.assertEqual(rect.x1, 5)
        self.assertEqual(rect.y1, 8)

    def test_validacion_x0_mayor_x1(self):
        """Test: ValueError cuando x0 > x1."""
        with self.assertRaises(ValueError) as context:
            Rectangulo(10, 0, 5, 10)
        self.assertEqual(str(context.exception), "x0 debe ser menor o igual a x1")

    def test_validacion_y0_mayor_y1(self):
        """Test: ValueError cuando y0 > y1."""
        with self.assertRaises(ValueError) as context:
            Rectangulo(0, 10, 10, 5)
        self.assertEqual(str(context.exception), "y0 debe ser menor o igual a y1")

    def test_ancho(self):
        """Test: Método ancho() retorna la diferencia en x."""
        rect = Rectangulo(2, 3, 8, 7)
        self.assertEqual(rect.ancho(), 6)  # 8 - 2 = 6

    def test_alto(self):
        """Test: Método alto() retorna la diferencia en y."""
        rect = Rectangulo(2, 3, 8, 7)
        self.assertEqual(rect.alto(), 4)  # 7 - 3 = 4

    def test_area(self):
        """Test: Método area() retorna ancho * alto."""
        rect = Rectangulo(0, 0, 5, 4)
        self.assertEqual(rect.area(), 20)  # 5 * 4 = 20

    def test_area_rectangulo_cero(self):
        """Test: Área de un rectángulo con coordenadas iguales."""
        rect = Rectangulo(0, 0, 0, 0)
        self.assertEqual(rect.area(), 0)

    def test_perimetro(self):
        """Test: Método perimetro() retorna 2 * (ancho + alto)."""
        rect = Rectangulo(0, 0, 6, 4)
        self.assertEqual(rect.perimetro(), 20)  # 2 * (6 + 4) = 20

    def test_perimetro_rectangulo_pequeño(self):
        """Test: Perímetro de un rectángulo pequeño."""
        rect = Rectangulo(1, 1, 4, 3)
        self.assertEqual(rect.perimetro(), 10)  # 2 * (3 + 2) = 10

    def test_es_cuadrado_verdadero(self):
        """Test: es_cuadrado() retorna True para cuadrados."""
        rect = Rectangulo(0, 0, 5, 5)
        self.assertTrue(rect.es_cuadrado())

    def test_es_cuadrado_falso(self):
        """Test: es_cuadrado() retorna False para rectángulos no cuadrados."""
        rect = Rectangulo(0, 0, 5, 3)
        self.assertFalse(rect.es_cuadrado())

    def test_es_cuadrado_diagonal(self):
        """Test: es_cuadrado() con coordenadas no (0, 0)."""
        rect = Rectangulo(2, 3, 7, 8)
        self.assertTrue(rect.es_cuadrado())  # ancho = 5, alto = 5

    def test_desplazar_positivo(self):
        """Test: desplazar() con valores positivos."""
        rect = Rectangulo(1, 2, 5, 6)
        rect.desplazar(3, 4)
        self.assertEqual(rect.x0, 4)  # 1 + 3
        self.assertEqual(rect.y0, 6)  # 2 + 4
        self.assertEqual(rect.x1, 8)  # 5 + 3
        self.assertEqual(rect.y1, 10)  # 6 + 4

    def test_desplazar_negativo(self):
        """Test: desplazar() con valores negativos."""
        rect = Rectangulo(5, 6, 10, 12)
        rect.desplazar(-2, -3)
        self.assertEqual(rect.x0, 3)  # 5 - 2
        self.assertEqual(rect.y0, 3)  # 6 - 3
        self.assertEqual(rect.x1, 8)  # 10 - 2
        self.assertEqual(rect.y1, 9)  # 12 - 3

    def test_desplazar_cero(self):
        """Test: desplazar() con (0, 0) no cambia coordenadas."""
        rect = Rectangulo(2, 3, 7, 9)
        rect.desplazar(0, 0)
        self.assertEqual(rect.x0, 2)
        self.assertEqual(rect.y0, 3)
        self.assertEqual(rect.x1, 7)
        self.assertEqual(rect.y1, 9)

    def test_rectangulo_offset(self):
        """Test: Rectángulo con coordenadas no comenzando en (0, 0)."""
        rect = Rectangulo(3, 4, 8, 9)
        self.assertEqual(rect.ancho(), 5)  # 8 - 3
        self.assertEqual(rect.alto(), 5)  # 9 - 4
        self.assertEqual(rect.area(), 25)  # 5 * 5
        self.assertTrue(rect.es_cuadrado())

    def test_validacion_x0_igual_x1(self):
        """Test: x0 igual a x1 debe ser válido (ancho = 0)."""
        rect = Rectangulo(0, 0, 0, 5)
        self.assertEqual(rect.ancho(), 0)

    def test_validacion_y0_igual_y1(self):
        """Test: y0 igual a y1 debe ser válido (alto = 0)."""
        rect = Rectangulo(0, 0, 5, 0)
        self.assertEqual(rect.alto(), 0)


if __name__ == "__main__":
    unittest.main()
