def apagarVelas(anios, velas):
    if anios < 1 or anios > 14:
        return print("Edad fuera de rango")
    elif len(velas) != anios:
        return print("Las velas no coinciden con los años")
    else:
        for vela in velas:
            if vela > 10:
                return print("La vela es muy alta")
        
        altura_maxima = max(velas)

        velas_apagadas = velas.count(altura_maxima)

        return print(f"Se apagaran {velas_apagadas} velas")

if __name__ == '__main__':
    anios_cumplidos = int(input("Ingrese los años cumplidos: "))
    cantidad_velas = list(map(int, input("Ingrese las velas: ").split(" ")))
    
    apagarVelas(anios_cumplidos, cantidad_velas)