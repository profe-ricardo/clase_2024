def apagarVelas(años, velas):
    altura_maxima = max(velas)
    
    resultado = velas.count(altura_maxima)
    
    print(f"las velas que podrá apagar: {resultado}")

if __name__ == '__main__':
    try:
        años_cumplidos = int(input("ingrese los años cumplidos: "))
        
        cantidad_velas = list(map(int, input("ingrese las velas (separadas por un espacio): ").split()))
        
        if not (1 <= len(cantidad_velas) <= 14):
            print("error: la cantidad de velas debe ser entre 1 y 14")
        elif not all(1 <= vela <= 10 for vela in cantidad_velas):
            print("error: la altura de cada vela entre 1 y 10")
        else:
            apagarVelas(años_cumplidos, cantidad_velas)
    except ValueError:
        print("error: ingrese valores válidos (números enteros)")
