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

#Añade un pequeño bloque de prueba para verificar que la funcion funciona correctamente
if __name__ == "__main__":
    # Lista de prueba
    lista_numeros = [10, 20, 30, 40, 50]
    
    # Calcular el promedio
    resultado = promedio(lista_numeros)
    
    # Imprimir el resultado
    print(f"El promedio de {lista_numeros} es: {resultado}")
    
    # Probar con una lista vacia
    lista_vacia = []
    resultado_vacio = promedio(lista_vacia)
    print(f"El promedio de una lista vacia es: {resultado_vacio}")

