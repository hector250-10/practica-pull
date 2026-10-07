# Escribe una función para generar la serie de Fibonacci hasta un número n dado. La función debe devolver una lista con los números de la serie.Aquí tienes una función en Python que genera la serie de Fibonacci hasta un número n dado:```python
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    while a <= n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
# Ejemplo de uso:
n = 10
print(fibonacci(n))  # Salida: [0, 1, 1, 2, 3, 5, 8]

# dame código de prueba adicional para verificar que la función funciona correctamente con diferentes valores de n. Aquí tienes algunos casos de prueba adicionales:
# Caso de prueba 1: n = 0
print(fibonacci(0))  # Salida: [0]
# Caso de prueba 2: n = 1
print(fibonacci(1))  # Salida: [0, 1]
# Caso de prueba 3: n = 5
print(fibonacci(5))  # Salida: [0, 1, 1, 2, 3]