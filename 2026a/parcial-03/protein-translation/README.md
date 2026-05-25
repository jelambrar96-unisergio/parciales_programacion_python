# Traducción de Proteínas (25 puntos)

Bienvenido a Traducción de Proteínas en la pista de Python de Exercism.
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, consulta `HELP.md`.

![alt text](media/protein_translation_image.png)

## 1. Instrucciones

Traduce secuencias de ARN en proteínas.

El ARN se puede dividir en secuencias de tres nucleótidos llamadas codones, y cada codón se traduce en un aminoácido.
Por ejemplo:

ARN: `"AUGUUUUCU"` => se traduce en

Codones: `"AUG", "UUU", "UCU"`
=> que se convierten en la secuencia de proteínas =>

Proteína: `"Methionine", "Phenylalanine", "Serine"`

Hay 64 codones que corresponden a 20 aminoácidos; sin embargo, no es necesario manejar todos los codones de forma explícita para este ejercicio.
Si tu solución funciona para un codón, debería funcionar para todos los que aparecen en esta lista.

También existen tres codones de terminación (codones 'STOP'); si se encuentra alguno de estos codones, la traducción termina y todas las secuencias posteriores se ignoran.

Por ejemplo:

ARN: `"AUGUUUUCUUAAAUG"` =>

Codones: `"AUG", "UUU", "UCU", "UAA", "AUG"` =>

Proteína: `"Methionine", "Phenylalanine", "Serine"`

Ten en cuenta que el codón de parada `"UAA"` detiene la traducción y el último codón `"AUG"` no se traduce.

## 2. Codones y aminoácidos necesarios

| Codón               | Aminoácido     |
| :------------------ | :------------- |
| AUG                 | Methionine     |
| UUU, UUC            | Phenylalanine  |
| UUA, UUG            | Leucine        |
| UCU, UCC, UCA, UCG  | Serine         |
| UAU, UAC            | Tyrosine       |
| UGU, UGC            | Cysteine       |
| UGG                 | Tryptophan     |
| UAA, UAG, UGA       | STOP           |

## 3. Ejemplos basados en los tests

1. **Un codón que no es STOP**:
   - Entrada: `"AUG"`
   - Salida: `["Methionine"]`
   - Explicación: "AUG" se mapea a Methionine.

2. **Dos codones iguales**:
   - Entrada: `"UUUUUU"`
   - Salida: `["Phenylalanine", "Phenylalanine"]`
   - Explicación: Se divide en `"UUU"`, `"UUU"`; cada codón es Phenylalanine.

3. **Dos codones distintos**:
   - Entrada: `"UUAUUG"`
   - Salida: `["Leucine", "Leucine"]`
   - Explicación: Se divide en `"UUA"`, `"UUG"`; ambos codones son Leucine.

4. **Secuencia con STOP al principio**:
   - Entrada: `"UAGUGG"`
   - Salida: `[]`
   - Explicación: El primer codón es STOP (`"UAG"`), así que no se traduce nada.

5. **STOP al final de una secuencia**:
   - Entrada: `"UGGUAG"`
   - Salida: `["Tryptophan"]`
   - Explicación: `"UGG"` es Tryptophan y `"UAG"` detiene la traducción.

6. **STOP en medio de la secuencia**:
   - Entrada: `"AUGUUUUAA"`
   - Salida: `["Methionine", "Phenylalanine"]`
   - Explicación: `"AUG"` => Methionine, `"UUU"` => Phenylalanine, y `"UAA"` detiene la traducción.

7. **Secuencia larga que se detiene en STOP**:
   - Entrada: `"UGGUGUUAUUAAUGGUUU"`
   - Salida: `["Tryptophan", "Cysteine", "Tyrosine"]`
   - Explicación: Se toman los codones `"UGG"`, `"UGU"`, `"UAU"`, `"UAA"`; luego de `"UAA"` no se traducen más codones.

## 4. Fuente

### Tomado de

- [exercism.org](https://exercism.org/tracks/python/exercises/protein-translation)

### Creado por

- @cptjackson

### Contribuido por

- @behrtam
- @cmccandless
- @Dog
- @ikhadykin
- @N-Parsons
- @nmbrgts
- @sjwarner-bp
- @thomasjpfan
- @tqa236
- @yawpitch

### Basado en

Tyler Long
