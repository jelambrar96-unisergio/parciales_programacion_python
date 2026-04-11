"""
Módulo para dibujar rectángulos en un canvas ASCII.

Este módulo proporciona funciones para generar representaciones visuales
de rectángulos dentro de un canvas de dimensiones especificadas.
"""

from rectangulo import Rectangulo


def draw_rectangle(alto_canvas: int, ancho_canvas: int, rectangulo: Rectangulo, simbolo: str = "#") -> str:
    """
    Dibuja un rectángulo dentro de un canvas de caracteres ASCII.
    
    Args:
        alto_canvas (int): La altura (número de filas) del canvas.
        ancho_canvas (int): El ancho (número de columnas) del canvas.
        rectangulo (Rectangulo): Objeto Rectangulo con las coordenadas (x0, y0, x1, y1).
        simbolo (str): El carácter a utilizar para rellenar el rectángulo (por defecto "#").
    
    Returns:
        str: Una cadena que representa el canvas con el rectángulo dibujado.
             Las filas se separan con saltos de línea (\\n).
    
    Ejemplo:
        >>> rect = Rectangulo(2, 1, 6, 3)
        >>> canvas = draw_rectangle(5, 10, rect, "#")
        >>> print(canvas)
                  
          ####    
          ####    
                  
                  
    """
    # TODO: Reemplaza la linea pass y escribe tu codigo aqui
    pass
