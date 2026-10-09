# Escribe una funcion llamada fibonacci que reciba un numero
# entero n y devuelva una lista con los primeros n terminos
# de la sucesion de Fibonacci.
# La sucesion empieza con 0 y 1: [0, 1, 1, 2, 3, 5, 8, ...]
# Incluye docstring y comentarios en espanol.   

def fibonacci(n):
    """
    Devuelve una lista con los primeros n términos de la sucesión de Fibonacci.
    
    Args:
        n (int): Número de términos a devolver.
        
    Returns:
        list: Lista con los primeros n términos de la sucesión de Fibonacci.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    
    return fib_list
# Explica paso a paso que hace esta funcion
La función `fibonacci` tiene como objetivo generar una lista con los primeros `n` términos de la sucesión de Fibonacci. A continuación, se explica paso a paso cómo funciona:
1. **Definición de la función**: La función se llama `fibonacci` y recibe un parámetro `n`, que es un número entero que indica cuántos términos de la sucesión se desean generar.
2. **Docstring**: Se incluye un docstring que describe brevemente la función, sus argumentos y lo que devuelve.
3. **Condiciones iniciales**:
   - Si `n` es menor o igual a 0, la función devuelve una lista vacía, ya que no hay términos que generar.
   - Si `n` es igual a 1, la función devuelve una lista con un solo elemento: `[0]`, que es el primer término de la sucesión.                                                                           
    - Si `n` es igual a 2, la función devuelve una lista con los dos primeros términos: `[0, 1]`.                   
4. **Generación de la sucesión**: Si `n` es mayor que 2, se inicializa una lista llamada `fib_list` con los dos primeros términos de la sucesión: `[0, 1]`.
5. **Bucle para calcular los términos restantes**: Se utiliza un bucle `for` que itera desde 2 hasta `n-1`. En cada iteración, se calcula el siguiente término de la sucesión sumando los dos términos anteriores (`fib_list[i - 1] + fib_list[i - 2]`) y se agrega a la lista `fib_list`.  
6. **Devolución del resultado**: Una vez que se han calculado todos los términos necesarios, la función devuelve la lista `fib_list`, que contiene los primeros `n` términos de la sucesión de Fibonacci.   

#añade un pequño bloque de prueba para verificar que la funcion funciona correctamente
# Bloque de prueba
if __name__ == "__main__":
    # Prueba con n = 10
    n = 10
    resultado = fibonacci(n)
    print(f"Los primeros {n} términos de la sucesión de Fibonacci son: {resultado}")
    # Prueba con n = 0
    n = 0
    resultado = fibonacci(n)
    print(f"Los primeros {n} términos de la sucesión de Fibonacci son: {resultado}")
    # Prueba con n = 1
    n = 1
    resultado = fibonacci(n)
    print(f"Los primeros {n} términos de la sucesión de Fibonacci son: {resultado}")
    # Prueba con n = 2
    n = 2
    resultado = fibonacci(n)
    print(f"Los primeros {n} términos de la sucesión de Fibonacci son: {resultado}")
    # Prueba con n = 15
    n = 15
    resultado = fibonacci(n)
    print(f"Los primeros {n} términos de la sucesión de Fibonacci son: {resultado}")