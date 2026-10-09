gi# Escribe una funcion llamada maximo_comun_divisor que reciba
# dos numeros enteros positivos y devuelva su MCD
# usando el algoritmo de Euclides.
# Incluye docstring y comentarios en espanol.
def maximo_comun_divisor(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números enteros positivos
    utilizando el algoritmo de Euclides.

    Parámetros:
    a (int): Primer número entero positivo.
    b (int): Segundo número entero positivo.

    Retorna:
    int: El máximo común divisor de a y b.
    """
    # Verificar que los números sean enteros positivos
    if a <= 0 or b <= 0:
        raise ValueError("Los números deben ser enteros positivos.")

    # Aplicar el algoritmo de Euclides
    while b != 0:
        a, b = b, a % b  # Reemplazar a con b y b con el residuo de a dividido por b

    return a  # Cuando b es 0, a es el MCD  

# Explica paso a paso que hace esta funcion
"""
1. Verifica que ambos números sean enteros positivos.
2. Aplica el algoritmo de Euclides:
   - Mientras b no sea 0, reemplaza a con b y b con el residuo de a dividido por b.
3. Cuando b sea 0, a contiene el MCD de los dos números originales.
"""

#añade un pequeño bloque de prueba para verificar que la funcion funciona correctamente
if __name__ == "__main__":
    # Prueba de la función maximo_comun_divisor
    num1 = 48
    num2 = 18
    resultado = maximo_comun_divisor(num1, num2)
    print(f"El MCD de {num1} y {num2} es: {resultado}")  # Debería imprimir 