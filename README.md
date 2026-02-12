# Simulación de un Autómata Finito Determinista (AFD)

## Descripción

Este programa implementa en Python un Autómata Finito Determinista (AFD)

El autómata reconoce cadenas binarias que **empiezan con 0**.

## Definición Formal del AFD

- Q = {q1, q2, q3}
- Σ = {0,1}
- q₀ = q1
- F = {q2}

### Función de transición f:

- f(q1,0) = q2
- f(q1,1) = q3
- f(q2,0) = q2
- f(q2,1) = q2
- f(q3,0) = q3
- f(q3,1) = q3

El autómata acepta una cadena si después de procesarla termina en el estado q2.

## Uso

Desde la terminal:

```bash
python AFD.py entrada.txt
