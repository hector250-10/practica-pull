# Escribe una funcion llamada promedio que reciba una lista
# de numeros y devuelva su media aritmetica.
# Si la lista esta vacia, debe devolver None.
# Incluye docstring y comentarios en espanol.
def promedio(numeros):
    # Verificar si la lista esta vacia
    if not numeros:
        return None
    
    # Calcular la suma de los numeros
    suma = sum(numeros)
    
    # Calcular y devolver el promedio
    return suma / len(numeros)