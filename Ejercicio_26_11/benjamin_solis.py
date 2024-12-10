def imprimir_escalera():

# Pedir al usuario el tamano de la escalera
    try:
        n = int(input("Ingrese el tamano de la escalera (entre 0 y 100): "))

        # Validar el rango de la entrada
        if n < 0 or n > 100:
            print("El numero debe estar entre 0 y 100.")
            return

        # Imprimir la escalera
        for i in range(1, n + 1):
            print(" " * (n - i) + "#" * i)

    except ValueError:
        print("Por favor, ingrese un numero entero valido.")

# Llamar a la funcion
imprimir_escalera()