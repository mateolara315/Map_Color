import numpy as np
def inArray():
    array = list()
    i = int(input("Numero de Nodos: "))
    j = i


    for x in range(i):
        if i <= 0 or i>20:
             print("Failure!")
             break
        elif j <= 0 or j>20:
             print("Failure!")
             break
        else:
            for y in range(j):
                num = input('[{0}, {1}] = '.format(x,y))
                array.append(int(num))


    a = np.reshape(array,(i,j))
    print('La matriz de juego ingresada es: \n',a)
    return(a)