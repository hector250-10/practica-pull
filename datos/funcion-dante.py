# Escribe una funcion llamada raiz_cuadrada que reciba un numero
# positivo n y devuelva su raiz cuadrada aproximada usando
# el metodo de Newton (aproximaciones sucesivas).
# Si n es negativo, lanza un error.
# Incluye docstring y comentarios en espanol.

def raiz_cuadrada(n):
    """
    Calcula la raiz cuadrada aproximada de un numero positivo n usando el metodo de Newton (aproximaciones sucesivas).
    Si n es negativo, lanza un error.
    :param n: Numero positivo del cual se desea calcular la raiz cuadrada.
    :return: Raiz cuadrada aproximada de n.
    """
    # Verificar si n es negativo
    if n < 0:
        raise ValueError("El numero debe ser positivo.")
    
    # Inicializar la aproximacion
    x = n / 2
    
    # Realizar aproximaciones sucesivas
    while True:
        # Calcular la siguiente aproximacion
        x_new = (x + n / x) / 2
        
        # Verificar si la aproximacion es suficientemente precisa
        if abs(x_new - x) < 1e-10:
            return x_new
        
        # Actualizar la aproximacion
        x = x_new
# Explica paso a paso que hace esta funcion
# La función `raiz_cuadrada` tiene como objetivo calcular la raíz cuadrada aproximada de un número positivo `n` utilizando el método de Newton, también conocido como aproximaciones sucesivas. A continuación, se explica paso a paso lo que hace la función:
# 1. **Docstring**: La función comienza con un docstring que describe su propósito, los parámetros que recibe y lo que devuelve. Esto es útil para la documentación y para que otros desarrolladores comprendan rápidamente la función.
# 2. **Verificación de entrada**: La función verifica si el número `n` es negativo. Si lo es, lanza un error `ValueError` con un mensaje indicando que el número debe ser positivo. Esto asegura que la función solo procese números positivos, ya que la raíz cuadrada de un número negativo no está definida en el conjunto de los números reales.
# 3. **Inicialización de la aproximación**: La función inicializa una variable `x` con la mitad del valor de `n`. Esta será la primera aproximación de la raíz cuadrada.
# 4. **Bucle de aproximación**: La función entra en un bucle `while True`, que continuará ejecutándose hasta que se cumpla una condición de convergencia.
# 5. **Cálculo de la nueva aproximación**: Dentro del bucle, se calcula una nueva aproximación `x_new` utilizando la fórmula de Newton: `(x + n / x) / 2`. Esta fórmula combina la aproximación actual `x` con el valor de `n` dividido por `x`, y luego se promedia.
# 6. **Verificación de convergencia**: La función verifica si la diferencia absoluta entre la nueva aproximación `x_new` y la aproximación anterior `x` es menor que un umbral de precisión (1e-10). Si es así, significa que la aproximación es suficientemente precisa y la función devuelve `x_new` como resultado.
# 7. **Actualización de la aproximación**: Si la condición de convergencia no se cumple, la función actualiza `x` con el valor de `x_new` y continúa el bucle para calcular una nueva aproximación.
# En resumen, la función utiliza un método iterativo para aproximar la raíz cuadrada de un número positivo, asegurando que la aproximación sea precisa y manejando adecuadamente los casos de entrada inválida.

# añade un pequeño bloque de prueba para verificar que la funcion funciona correctamente
# Bloque de prueba para verificar que la función funciona correctamente
if __name__ == "__main__":
    # Prueba con un número positivo
    numero = 25
    resultado = raiz_cuadrada(numero)
    print(f"La raíz cuadrada aproximada de {numero} es {resultado}")

    # Prueba con otro número positivo
    numero = 2
    resultado = raiz_cuadrada(numero)
    print(f"La raíz cuadrada aproximada de {numero} es {resultado}")

    # Prueba con un número negativo para verificar el manejo de errores
    try:
        numero = -9
        resultado = raiz_cuadrada(numero)
    except ValueError as e:
        print(f"Error: {e}")
