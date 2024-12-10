"""
    Estás a cargo de la torta para el cumpleaños de un niño.
    Decidiste que la torta tendría una vela por cada año.
    Las velas tendrán distintos tamaños, pero solo podrán apagar las más grandes.
    
    El usuario deberá hacer 2 inputs:
        1.- Los años cumplidos.
        2.- Tamaño de cada vela (separada por un espacio).

    Ejemplo de input:
        4
        3 2 1 3

    Ejemplo de output:
        2

    Explicación:
        Las alturas de las velas son [3, 2, 1, 3].
        Hay 2 velas de altura 3, por lo que solo esas podrá apagar.

    Limitantes:
        1.- La cantidad de velas debe ser un número entero entre 1 y 14.
        2.- La altura máxima de cada vela es de 10.

    Debe completar la actividad usando el código de ejemplo que se le entrega
"""

def apagarVelas(anios, velas):
    resultado = 0
    print(resultado)

if __name__ == '__main__':
    anios_cumplidos = int(input("Ingrese los años cumplidos: "))
    cantidad_velas = list(map(int, input("Ingrese las velas: ").split(" ")))
    
    apagarVelas(anios_cumplidos, cantidad_velas)