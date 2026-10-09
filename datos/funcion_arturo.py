# Escribe una funcion llamada promedio que reciba una lista
# de numeros y devuelva su media aritmetica.
# Si la lista esta vacia, debe devolver None.
# Incluye docstring y comentarios en espanol.
def promedio(numeros):
    if not numeros:
        return None
    return sum(numeros) / len(numeros)

# añade un pequeño bloque de prueba para verificar que la función funciona correctamente. 
if __name__ == "__main__":
    print(promedio([1, 2, 3, 4, 5]))