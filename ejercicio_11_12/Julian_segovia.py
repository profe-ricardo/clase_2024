def paresDivisibles(k, n):
    parejas = []
    
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if (n[i] + n[j]) % k == 0:
                parejas.append((n[i], n[j]))
    
    if parejas:
        print("Pares:",f"{len(parejas)}, la suma de estos numeros es divisible por el numero divisor:",*parejas,)
    else:
        print("no se encontraron pares que cumplan con las condiciones")

if __name__ == '__main__':
    k = int(input("Ingrese el número divisor: "))
    n = list(map(int, input("Ingrese el contenido del arreglo: ").split()))
    
    paresDivisibles(k, n)
