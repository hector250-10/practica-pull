# Escribe una funcion llamada promedio que reciba una lista
# de numeros y devuelva su media aritmetica.
# Si la lista esta vacia, debe devolver None.
# Incluye docstring y comentarios en espanol.
def promedio(numeros):
    """
    Calcula el promedio de una lista de numeros.

    Args:
        numeros (list): Una lista de numeros.

    Returns:
        float: El promedio de los numeros, o None si la lista esta vacia.
    """
    if not numeros:
        return None
    return sum(numeros) / len(numeros)
# Explica paso a paso que hace esta funcion
# 1. Recibe una lista de numeros como argumento
# 2. Verifica si la lista esta vacia
# 3. Si esta vacia, devuelve None
# 4. Si no esta vacia, calcula la suma de los numeros y la divide por la cantidad de elementos

#añade un pequeño bloque de prueba para verificar que la funcion funciona correctamente
# Bloque de prueba
print(promedio([1, 2, 3, 4, 5]))  # Debe imprimir 3.0
print(promedio([]))  # Debe imprimir None
