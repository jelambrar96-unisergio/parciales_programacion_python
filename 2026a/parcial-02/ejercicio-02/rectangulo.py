

"""
Módulo que define la clase Rectangulo con atributos y métodos para
calcular propiedades geométricas de un rectángulo.
"""


class Rectangulo:
    """
    Clase que representa un rectángulo en el plano cartesiano.
    
    Atributos:
        x0 (int): Coordenada x de la esquina inferior-izquierda (por defecto 0).
        y0 (int): Coordenada y de la esquina inferior-izquierda (por defecto 0).
        x1 (int): Coordenada x de la esquina superior-derecha (por defecto 0).
        y1 (int): Coordenada y de la esquina superior-derecha (por defecto 0).
    """

    def __init__(self, x0=0, y0=0, x1=0, y1=0):
        """
        Inicializa un rectángulo con las coordenadas especificadas.
        
        Args:
            x0 (int): Coordenada x de la esquina inferior-izquierda (por defecto 0).
            y0 (int): Coordenada y de la esquina inferior-izquierda (por defecto 0).
            x1 (int): Coordenada x de la esquina superior-derecha (por defecto 0).
            y1 (int): Coordenada y de la esquina superior-derecha (por defecto 0).
        """
        # TODO: Reemplaza la linea pass y escribe tu código aquí
        pass

    def alto(self):
        """
        Calcula la altura del rectángulo.
        
        Returns:
            int: La altura del rectángulo (diferencia en y).
        """
        # TODO: Reemplaza la linea pass y escribe tu código aquí
        pass

    def ancho(self):
        """
        Calcula el ancho del rectángulo.
        
        Returns:
            int: El ancho del rectángulo (diferencia en x).
        """
        # TODO: Reemplaza la linea pass y escribe tu código aquí
        pass

    def perimetro(self):
        """
        Calcula el perímetro del rectángulo.
        
        Returns:
            int: El perímetro del rectángulo (2 * (ancho + alto)).
        """
        # TODO: Reemplaza la linea pass y escribe tu código aquí
        pass

    def area(self):
        """
        Calcula el área del rectángulo.
        
        Returns:
            int: El área del rectángulo (ancho * alto).
        """
        # TODO: Reemplaza la linea pass y escribe tu código aquí
        pass

    def es_cuadrado(self):
        """
        Verifica si el rectángulo es un cuadrado.
        
        Returns:
            bool: True si el rectángulo es un cuadrado, False en caso contrario.
        """
        # TODO: Reemplaza la linea pass y escribe tu código aquí
        pass

    def desplazar(self, dx, dy):
        """
        Desplaza el rectángulo por dx unidades en x y dy unidades en y.
        
        Args:
            dx (int): Desplazamiento en el eje x.
            dy (int): Desplazamiento en el eje y.
        """
        # TODO: Reemplaza la linea pass y escribe tu código aquí
        pass
