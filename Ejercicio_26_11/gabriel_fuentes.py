def apagarVelas(anios, velas):
    vela_mas_grande = max(velas)
    resultado = velas.count(vela_mas_grande)
    print(resultado)

if __name__ == '__main__':
    anios_cumplidos = int(input("Ingrese los años cumplidos: "))
    if not (1 <= anios_cumplidos <= 14):
        print("Error: Los años cumplidos deben estar entre 1 y 14.")
    else:
        cantidad_velas = list(map(int, input("Ingrese las velas: ").split(" ")))
        if len(cantidad_velas) != anios_cumplidos:
            print("Error: El número de velas debe coincidir con los años cumplidos.")
        elif not all(1 <= v <= 10 for v in cantidad_velas):
            print("Error: Las alturas de las velas deben estar entre 1 y 10.")
        else:
            apagarVelas(anios_cumplidos, cantidad_velas)