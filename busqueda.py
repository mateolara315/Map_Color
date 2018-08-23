# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 

def search(entry):

#//////////////////////////////////////////////////////////////////////////////
#Busco las diagonales con cero (eso indica sin color asignado) y retorno que 
#filas de la matrix de adyacencia son aquellas sin color asignado -> "noColor"   
    [i,j] = np.where(entry==0)
    noColor = []
    for k in range(i.shape[0]) :
        if i[k] == j[k]:
            noColor = np.append(noColor,[i[k]])
    noColor = noColor.astype(int)
    print(noColor)
#//////////////////////////////////////////////////////////////////////////////
    
    
#//////////////////////////////////////////////////////////////////////////////
#Me indica con que colores estan conectados aquellos puntos sin color asignado,
#retorno una matrix de colores donde cada columna de esta corresponde a una
#fila de la matriz noColor. La matrix colores posee en cada elemnto de una fila 
#los colores con los que el nodo esta conectado -> "colores"
    colors = np.zeros((noColor.shape[0], entry.shape[0]))
    for k1 in range(noColor.shape[0]):
        for k2 in range(entry.shape[0]):
            if (entry[noColor[k1],k2] == 1):
                colors[k1,k2] = entry[k2,k2]
    print(colors)
#//////////////////////////////////////////////////////////////////////////////


#//////////////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////////////////////////    
    
entry = np.array([[1,1,1,1,0,0],[1,2,0,0,0,0],[1,0,0,0,0,1],[1,0,0,0,1,1],
              [0,0,0,1,0,0],[0,0,1,1,1,0]]) #matrientry de entada 
print(entry)
search(entry)   
    
    