import sympy as sp

# Definiere die Variable a und die Unbekannten x, y, z
a = sp.symbols('a')
x, y, z = sp.symbols('x y z')

# Definiere die Koeffizientenmatrix
matrix = sp.Matrix([
    [a, a + 1, a + 2],
    [a + 3, a + 4, a + 5],
    [a + 6, a + 7, a + 8]
])

print(matrix.det())
