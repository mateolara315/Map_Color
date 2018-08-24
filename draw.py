# Esta función colorea el nodo revisando cada caso correspondiente
import numpy as np
def drawColor(adjMat, numNode, nodeWeight, numColor, adjColor):
    tmp = list(np.linspace(1,numColor,numColor,dtype=int))
    if nodeWeight == numColor:
        numColor = numColor + 1
        adjMat[numNode,numNode] = numColor
    else:
        if len(adjColor) == 1:
            print(tmp)
            i = tmp.index(adjColor)
            del tmp[i]
            adjMat[numNode, numNode] = tmp[0]
        else:
            i = list(set(tmp) - set(adjColor))
            adjMat[numNode, numNode] = i[0]
    return(numColor, adjMat)

