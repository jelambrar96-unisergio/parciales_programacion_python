# El Juego de la Vida de Conway (25 puntos)

Bienvenido al Juego de la Vida de Conway en la pista de Python de Exercism.
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, consulta `HELP.md`.

## 1. Introducción

[El Juego de la Vida de Conway][game-of-life] es un autómata celular fascinante creado por el matemático británico John Horton Conway en 1970.

El juego consiste en una cuadrícula bidimensional de células que pueden estar "vivas" o "muertas".

Después de cada generación, las células interactúan con sus ocho vecinos a través de un conjunto de reglas, que definen la nueva generación.

[game-of-life]: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

![vis-game-of-life](media/game-of-life-loop-cropped.gif)

Imagen tomada de [datawrapper.de](https://www.datawrapper.de/blog/game-of-life)

## 2. Instrucciones

Después de cada generación, las células interactúan con sus ocho vecinos, que son células adyacentes horizontal, vertical o diagonalmente.

### 🎯 Las Reglas

Para cada célula, cuentas sus **8 vecinos** (horizontal, vertical y diagonal):

- ❌ **Regla 1: Celula viva con menos de dos vecinos vivos** → muere
- ✅ **Regla 2: Célula viva con 2-3 vecinos vivos** → sobrevive
- ❌ **Regla 3: Celula viva más menos de tres vecinos vivos** → muere
- ✅ **Regla 4: Célula muerta con exactamente 3 vecinos vivos** → nace  

![alt text](media/rules-gol-image.png)

Imagen tomada de [researchgate.net](https://www.researchgate.net/figure/Rules-of-Conways-Game-of-Life_fig5_339605473)

## 3. ¿Qué hay que hacer?

Debes implementar la función `tick(matrix)` que simula **una generación** del Juego de la Vida de Conway. El código en game_of_life.py

Dada una matriz de 1s y 0s (correspondientes a células vivas y muertas), aplica las reglas a cada célula y devuelve la siguiente generación.

---

## 4. 📌 Ejemplos de Salida Esperada

### Ejemplo 1: Célula solitaria (muere por soledad)

```python
matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]
# ↓ Resultado después de tick:
[
    [0, 0, 0],
    [0, 0, 0],  # La célula del centro muere (0 vecinos vivos)
    [0, 0, 0],
]
```

### Ejemplo 2: Dos células verticales (ambas mueren)

```python
matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 1, 0],
]
# ↓ Resultado:
[
    [0, 0, 0],
    [0, 0, 0],  # Ambas mueren (tienen solo 1 vecino vivo)
    [0, 0, 0],
]
```

### Ejemplo 3: Patrón estable (3 esquinas vivas)

```python
matrix = [
    [1, 1, 0],
    [0, 0, 0],
    [1, 0, 0],
]
# ↓ Resultado:
[
    [0, 0, 0],
    [1, 1, 0],  # Nace una célula en [1,0] y [1,1] (3 vecinos vivos)
    [0, 0, 0],
]
```

### Ejemplo 4: Matriz llena (explosiones)

```python
matrix = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],  # 9 células vivas
]
# ↓ Resultado (sobreviven solo las 4 esquinas):
[
    [1, 0, 1],  # Centro muere (4+ vecinos), esquinas sobreviven (3 vecinos)
    [0, 0, 0],  # Centro de cada lado muere (4+ vecinos)
    [1, 0, 1],
]
```

---

## 4. 🧪 Verificar tu solución

El código ya está listo. Puedes ejecutar los tests con:

```bash
python -m pytest game_of_life_test.py
```

Los 8 tests validan diferentes escenarios de las reglas del juego. ✨

Made changes.

## 5. Fuente

### Tomado de

- [exercism.org](https://exercism.org/tracks/python/exercises/game-of-life)

### Creado por

- @BNAndras

### Basado en

Wikipedia - [https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
