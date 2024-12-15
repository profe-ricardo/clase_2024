def paresDivisibles(k, n):
    pares = []  

    for i in range(len(n)):  # Largo del arreglo
        for j in range(i + 1, len(n)): 
            #Si es divisible lo guarda              #Recorre en forma matricial
            if (n[i] + n[j]) % k == 0:
                pares.append((n[i], n[j]))  

    cantidad_pares = len(pares)  
    return print(f"{cantidad_pares}, {pares}")  


if __name__ == '__main__':  
    while True:

        k = int(input("Ingrese el número divisor: "))
        
        if k < 1 or k > 10:  # Limitante
            print('Limitante no cumplida para k')
            continue
        

        n = list(map(int, input("Ingrese el contenido del arreglo: ").split()))

        if len(n) < 2 or len(n) > 100:  # Limitante
            print('Limitante no cumplida para la longitud del arreglo')
            continue
        
        break

    paresDivisibles(k, n)

#En caso de necesitar el output de la forma igual a la pedida
"""
formato = tuple(pares)  #Inicio del codigo

return print(f"{cantidad_pares}, {formato}") #En el retorno

"""