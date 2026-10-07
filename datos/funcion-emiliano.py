# Escribe una funcion llamada suma_digitos que reciba un numero
# entero positivo y devuelva la suma de sus digitos.
# Ejemplo: suma_digitos(123) debe devolver 6.
# Incluye docstring y comentarios en espanol.
def suma_digitos(numero):
    # Convertir el numero a string para poder iterar sobre sus digitos
    str_numero = str(numero)
    # Inicializar la suma
    suma = 0
    # Iterar sobre cada digito y sumarlo
    for digito in str_numero:
        suma += int(digito)
    # Devolver la suma
    return suma

#añade un bloque de prueba para verificar que la función funciona correctamente
if __name__ == "__main__":
    # Prueba con el numero 123, la suma de sus digitos es 6
    assert suma_digitos(123) == 6, "Error: La suma de los digitos de 123 debe ser 6"
    # Prueba con el numero 456, la suma de sus digitos es 15
    assert suma_digitos(456) == 15, "Error: La suma de los digitos de 456 debe ser 15"
    # Prueba con el numero 7890, la suma de sus digitos es 24
    assert suma_digitos(7890) == 24, "Error: La suma de los digitos de 7890 debe ser 24"
    # Prueba con el numero 0, la suma de sus digitos es 0
    assert suma_digitos(0) == 0, "Error: La suma de los digitos de 0 debe ser 0"
    
    print("Todas las pruebas pasaron correctamente.")
    