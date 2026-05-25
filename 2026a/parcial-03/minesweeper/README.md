# Buscaminas (25 puntos)

Bienvenido a Buscaminas en la pista de Python de Exercism.
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, consulta `HELP.md`.

## 1. Introducción

[Buscaminas][wikipedia] es un juego popular donde el usuario tiene que encontrar las minas usando pistas numéricas que indican cuántas minas están directamente adyacentes (horizontal, vertical, diagonalmente) a un cuadrado.

![minesweeper](media/image.png)

[wikipedia]: https://en.wikipedia.org/wiki/Minesweeper_(video_game)

## 2. Instrucciones

Tu tarea es agregar los conteos de minas a los cuadrados vacíos en un tablero de Buscaminas completado.
El tablero es un rectángulo compuesto de cuadrados que son vacíos (`' '`) o minas (`'*'`).

Para cada cuadrado vacío, cuenta el número de minas adyacentes (horizontal, vertical, diagonalmente).
Si el cuadrado vacío no tiene minas adyacentes, déjalo vacío.
De lo contrario, reemplázalo con el conteo de minas adyacentes.

Por ejemplo, puedes recibir un tablero de 5 x 4 como este (los espacios vacíos se representan aquí con el carácter '·' para mostrar en pantalla):

```text
·*·*·
··*··
··*··
·····
```

Que tu código debería transformar en esto:

```text
1*3*1
13*31
·2*2·
·111·
```

### 3. Ejemplos adicionales

Basándonos en los casos de prueba, aquí hay algunos ejemplos con explicaciones:

1. **Mina rodeada de espacios**:
   - Entrada: `["   ", " * ", "   "]`
   - Salida: `["111", "1*1", "111"]`
   - Explicación: La mina en el centro tiene 8 espacios adyacentes. Cada espacio cuenta 1 mina adyacente (la del centro), por lo que se convierten en '1'. La mina permanece como '*'.

2. **Espacio rodeado de minas**:
   - Entrada: `["***", "* *", "***"]`
   - Salida: `["***", "*8*", "***"]`
   - Explicación: El espacio en el centro tiene 8 minas adyacentes (todas las posiciones alrededor), por lo que se reemplaza con '8'. Las minas permanecen como '*'.

3. **Línea horizontal**:
   - Entrada: `[" * * "]`
   - Salida: `["1*2*1"]`
   - Explicación: Los espacios a los lados de cada mina cuentan 1 mina adyacente. El espacio entre las dos minas cuenta 2 minas adyacentes (ambas).

4. **Línea vertical**:
   - Entrada: `[" ", "*", " ", "*", " "]`
   - Salida: `["1", "*", "2", "*", "1"]`
   - Explicación: Los espacios arriba y abajo de cada mina cuentan 1 mina adyacente. El espacio entre las dos minas cuenta 2 minas adyacentes.

5. **Sin minas**:
   - Entrada: `["   ", "   ", "   "]`
   - Salida: `["   ", "   ", "   "]`
   - Explicación: No hay minas, por lo que todos los espacios permanecen vacíos.

6. **Solo minas**:
   - Entrada: `["***", "***", "***"]`
   - Salida: `["***", "***", "***"]`
   - Explicación: No hay espacios vacíos para contar, por lo que el tablero permanece igual.

## 4. Mensajes de excepción

A veces es necesario [lanzar una excepción](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). Cuando lo hagas, siempre incluye un **mensaje de error significativo** para indicar cuál es la fuente del error. Esto hace que tu código sea más legible y ayuda significativamente con la depuración. Para situaciones donde sabes que la fuente del error será de cierto tipo, puedes elegir lanzar uno de los [tipos de error incorporados](https://docs.python.org/3/library/exceptions.html#base-classes), pero aún así incluye un mensaje significativo.

Este ejercicio en particular requiere que uses la [sentencia raise](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) para "lanzar" un `ValueError` cuando la función `board()` recibe entrada malformada. Las pruebas solo pasarán si lanzas la excepción e incluyes un mensaje con ella.

Para lanzar un `ValueError` con un mensaje, escribe el mensaje como argumento al tipo de excepción:

```python
# cuando el tablero recibe entrada malformada
raise ValueError("The board is invalid with current input.")
```

## 5. Fuente

### Tomado de

- [exercism.org](https://exercism.org/tracks/python/exercises/minesweeper)

### Creado por

- @betegelse

### Contribuido por

- @alexpjohnson
- @behrtam
- @BethanyG
- @cmccandless
- @Dog
- @fluxusfrequency
- @ikhadykin
- @kytrinyx
- @N-Parsons
- @peterblazejewicz
- @pheanex
- @sjakobi
- @smalley
- @tqa236
