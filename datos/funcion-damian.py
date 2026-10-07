# Escribe una funcion llamada promedio que reciba una lista
# de numeros y devuelva su media aritmetica.
# Si la lista esta vacia, debe devolver None.
# Incluye docstring y comentarios en espanol.

def promedio(lista):
    """
    Calcula la media aritmetica de una lista de numeros.

    Args:
        lista (list): Una lista de numeros.

    Returns:
        float: La media aritmetica de los numeros en la lista.
        None: Si la lista esta vacia.
    """
    # Verifica si la lista esta vacia
    if not lista:
        return None
    
    # Calcula la suma de los elementos de la lista
    suma = sum(lista)
    
    # Calcula el promedio dividiendo la suma entre el numero de elementos
    promedio = suma / len(lista)
    
    return promedio

#Añade un pequeño bloque de prueba para verificar que la funcion funciona correctamente
if __name__ == "__main__":
    # Prueba con una lista de numeros
    numeros = [10, 20, 30, 40, 50]
    print(f"El promedio de {numeros} es: {promedio(numeros)}")  # Deberia imprimir 30.0

    # Prueba con una lista vacia
    vacia = []
    print(f"El promedio de la lista vacia es: {promedio(vacia)}")  # Deberia imprimir None
