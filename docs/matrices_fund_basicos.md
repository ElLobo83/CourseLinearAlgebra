# Matriz fundamentos básicos

Una **matriz** es una colección rectangular de números, símbolos o expresiones, dispuestos en filas y columnas. Es una herramienta fundamental en álgebra lineal y se utiliza para representar sistemas de ecuaciones lineales, transformaciones lineales, entre otros.

## Características Principales

- **Orden o Dimensión**: El tamaño de una matriz se define por su número de filas (m) y columnas (n), y se denota como m × n.
- **Elementos**: Cada valor en la matriz se llama elemento, y se identifica por su posición (i, j), donde i es el índice de la fila y j el de la columna.
- **Tipo de Matrices**: Existen varios tipos, como matrices cuadradas, diagonales, identidad, simétricas, entre otras.

## Elementos de una Matriz

- **Elemento aᵢⱼ**: Es el valor que se encuentra en la intersección de la i-ésima fila y la j-ésima columna.
- **Diagonal Principal**: Es el conjunto de elementos aᵢⱼ donde i = j.
- **Diagonal Secundaria**: En matrices cuadradas, es el conjunto de elementos aᵢⱼ donde i + j = n + 1.

## Operaciones con Matrices

- **Suma y Resta**: Se pueden sumar o restar matrices del mismo orden, sumando o restando sus elementos correspondientes.
- **Multiplicación por un Escalar**: Cada elemento de la matriz se multiplica por el escalar.
- **Multiplicación de Matrices**: El producto de dos matrices A (m × n) y B (n × p) resulta en una nueva matriz C (m × p) cuyos elementos se calculan como la suma de los productos de los elementos correspondientes de las filas de A y las columnas de B.
- **Transposición**: La transposición de una matriz A es otra matriz Aᵀ donde los elementos de las filas de A se convierten en columnas y viceversa.
- **Determinante**: Solo para matrices cuadradas, es un valor que puede indicar si el sistema de ecuaciones asociado tiene solución única.
- **Inversa**: También para matrices cuadradas, es una matriz A⁻¹ tal que A × A⁻¹ = I, donde I es la matriz identidad.

## Ejemplo en LaTeX

La representación de una matriz 2x2 en LaTeX sería:

$$
A = \begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
$$

Este documento puede servir como base para introducir conceptos más avanzados en álgebra lineal, como el cálculo de autovalores y autovectores, espacios vectoriales, y más.
