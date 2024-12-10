def apagarVelas(anios, velas):
    altura_maxima = max(velas)
    cantidad_maximas = velas.count(altura_maxima)
    resultado = cantidad_maximas    
    print(resultado)
    

if __name__ == '__main__':
    anios_cumplidos = int(input("Ingrese los años cumplidos: "))
    if anios_cumplidos < 1 or anios_cumplidos > 14:
        print("Ingrese los años cumplidos, debe ser un número entero entre 1 y 14.")
    else:
        cantidad_velas = list(map(int, input("Ingrese las velas (tamaño 1 a 10) separadas por un espacio (misma cantidad de años cumplidos): ").split(" ")))
        if len(cantidad_velas) != anios_cumplidos:
            print("Ingrese las velas, la cantidad de velas debe ser igual a los años cumplidos.")
        else:
            if any(altura < 1 or altura > 10 for altura in cantidad_velas):
                print("La altura de cada vela debe ser un número entero entre 1 y 10.")
            else:
                apagarVelas(anios_cumplidos, cantidad_velas)
                resultado = "Debera apagar las mas altas"
                print("velas debes apagar")
