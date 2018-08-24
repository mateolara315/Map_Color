from inArray import inArray
from busqueda import search
from draw import drawColor
import numpy as np
print('Digitar la matriz de adyacencia\n\n')
adjMat = inArray()
# adjMat = np.array([[0,1,1,1,0,0],[1,0,1,0,1,0],[1,0,0,1,1,1],[1,1,0,0,1,1],
#                [1,0,1,1,0,1],[1,1,0,1,1,0]]) #matrientry de entada
adjMat[0,0] = 1
adjMat[1,1] = 2
numColor = 2
while True:
    if np.count_nonzero(np.diagonal(adjMat).copy()) == len(np.diagonal(adjMat).copy()):
        break
    [final_list, nodeWeight, numNode] = search(adjMat)
    [numColor,adjMat] = drawColor(adjMat,numNode, nodeWeight,numColor,final_list)
print("El vector de colores queda de la siguiente forma: ",np.diagonal(adjMat))
