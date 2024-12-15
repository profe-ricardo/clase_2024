def paresDivisibles(k, n):
    
    if len(n) < 2 or len(n) > 100:
        print("Error: El largo del arreglo debe estar entre 2 y 100.")
        return
    if k < 1 or k > 10:
        print("Error: El número divisor k debe estar entre 1 y 10.")
        return

    
    pares = []

   
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            suma = n[i] + n[j]
            if suma % k == 0:
                pares.append((n[i], n[j]))

   
    print(len(pares), end=", ")
    for par in pares:
        print(par, end=" ")
    print()  

if __name__ == '__main__':
    try:
        
        k = int(input("Ingrese el número divisor: "))

        
        n = input("Ingrese el contenido del arreglo: ").split()
        n = list(map(int, n))

        
        paresDivisibles(k, n)
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese números válidos.")
