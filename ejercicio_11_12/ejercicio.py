"""
    Dado un arreglo de enteros positivos 'n' y un número 'k',
    determine el número de parejas (i, j) en donde se cumple que 
     - i < j
     - i + j es divisible por k

    El usuario deberá hacer 2 inputs:
        1.- k
        2.- n

    Ejemplo de input:
        5
        1 2 3 4 5 6

    Ejemplo de output:
        3, (1, 4) (2, 3) (4, 6)

    Explicación:
        1 + 4 = 5 / 5 = 1
        2 + 3 = 5 / 5 = 1
        4 + 6 = 10 / 5 = 2
        3 pares cumplen el 'i < j' y, además, son divisibles por 5.

    Limitantes:
        1.- El largo del arreglo de n debe ser entre 2 y 100.
        2.- 1 <= k <= 10
        3.- 1 <= i <= 10
        4.- 1 <= j <= 10

    Debe completar la actividad usando el código de ejemplo que se le entrega
"""

import math

def paresDivisibles(k, n):
    print("Completa el ejercicio")

if __name__ == '__main__':
    k = int(input("Ingrese el número divisor: "))
    n = list(map(int, input("Ingrese el contenido del arreglo: ").split(" ")))
    
    paresDivisibles(k, n)