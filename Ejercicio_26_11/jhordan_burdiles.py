def apagarVelas(velas):
    altura_maxima = max(velas)
    
    cantidad_maximas = velas.count(altura_maxima)
    
    return cantidad_maximas

if __name__ == '__main__':
    anios = int(input("¿Cuántos años cumple el niño? "))
    
    if anios < 1 or anios > 14:
        print("El número de años debe estar entre 1 y 14.")
    else:
        velas = input(f"Ingresa la altura de las {anios} velas, separadas por un espacio: ")
        
        velas = velas.split() 
        velas = [int(vela) for vela in velas]  
        
        if any(vela > 10 for vela in velas):
            print("Todas las velas deben tener una altura máxima de 10.")
        else:
            resultado = apagarVelas(velas)
            print(f"Se pueden apagar {resultado} vela(s).")