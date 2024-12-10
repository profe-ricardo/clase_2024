def datos ():
    vela = []
    while True:
        try:
            años = int(input('Que edad cumplio el regalon: '))   
            cantidad_velas = int(input('Cuantas velas le quieres colocar a la torta del regalon: '))   
            break
        except ValueError:
            print('Muy vivo -_- \n Solo numeros')

    if cantidad_velas >=1 and cantidad_velas <=14: #Limitante 1

        for x in range(cantidad_velas):
            while True:
                try:
                    y = int (input('Ingrese altura (maximo 10): '))
                    
                    #Limitante 2
                    if y <=0:
                        print('Altura negativa no existe \n Dejado como 0 por defecto')
                        y = 0
                        
                    elif y>=10:
                        print('Altura maxima sobrepasada \n Dejado en 10 por defecto')
                        y = 10

                    vela.append(y)

                    break  #Chau While
                except ValueError:
                    print('Muy vivo -_- \n Castigado con un 0')  
                    n = 0
                    vela.append(n)

    #Ordenar para obtener el mayor
        orden_vela = vela.copy()       #Auxiliar
        orden_vela.sort(reverse=True)   
        vela_mas_alta = orden_vela[0]  #Numero mas alto

        contar_total= vela.count(vela_mas_alta)     #Cuenta total mayor

        #Remover 
        for a in range(contar_total): #Recorre desde 0 hasta el
            vela.remove(vela_mas_alta)  

    else:
        print('Mi compadre el vivo')    
        
    return print(f'La edad del regalon es de {años} \n torta {vela}')

datos()