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
#Me indica como estan conetados aquellos nodos sin color asignado y retorno 
#una matrix que indica dicha caracteristica -> "connections"
    connections = np.zeros((noColor.shape[0], entry.shape[0]))
    for k1 in range(noColor.shape[0]): 
        for k2 in range(entry.shape[0]): 
            if (entry[noColor[k1],k2] == 1):
                connections[k1,k2] = 1
    print(connections)
#//////////////////////////////////////////////////////////////////////////////


#//////////////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////////////////////////    
    
entry = np.array([[1,1,1,1,0,0],[1,2,0,0,0,0],[1,0,0,0,0,1],[1,0,0,0,1,1],
              [0,0,0,1,0,0],[0,0,1,1,1,0]]) #matrientry de entada 
print(entry)
search(entry)   
    
    