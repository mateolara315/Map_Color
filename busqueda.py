# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 

def search(x):

#//////////////////////////////////////////////////////////////////////////////
#Busco las diagonales con cero (eso indica sin color asignado) y retorno que 
#filas de la matrix son aquellas sin color asignado     
    [i,j] = np.where(x==0)
    zero = []
    for k in range(i.shape[0]) :
        if i[k] == j [k]:
            zero = np.append(zero,[i[k]])
    zero = zero.astype(int)
#//////////////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////////////////////////
    
#//////////////////////////////////////////////////////////////////////////////    
    
x = np.array([[1,1,1,1,0,0],[1,2,0,0,0,0],[1,0,0,0,0,1],[1,0,0,0,1,1],
              [0,0,0,1,0,0],[0,0,1,1,1,0]]) #matrix de entada 
search(x)   
    
    