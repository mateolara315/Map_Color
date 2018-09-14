# -*- coding: utf-8 -*-

# !!! RECORDAR QUE CONTEO DE MATRICES EMPIEZA EN 0
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 

def search(entry):
    """ Funcion de busqueda, con entrada de matrix de adyacencia siempre actual
    y con salida para funcion de Haroldo: nodo con mayor numero de colores 
    diferentes conectados a el "heuristica" (af), lista de dichos colores 
    (final_list) y el nodo de interes cuyas propiedades se listaron 
    ariba (bf)"""

#////////////////////////////////////ONE///////////////////////////////////////
#Busco las diagonales con cero (eso indica sin color asignado) y retorno que 
#filas de la matrix de adyacencia son aquellas sin color asignado -> "noColor" 
    # print(entry)
    # print("*")
    [i,j] =  np.where(entry==0)
    noColor = []
    for k in range(i.shape[0]) :
        if i[k] == j[k]:
            noColor = np.append(noColor,[i[k]])
    noColor = noColor.astype(int)
    # print(noColor)
    # print("*")
#//////////////////////////////////////////////////////////////////////////////
    
    
#///////////////////////////////////TWO////////////////////////////////////////
#Me indica con que colores estan conectados aquellos puntos sin color asignado,
#retorno una matrix de colores donde cada columna de esta corresponde a una
#fila de la matriz noColor. La matrix colores posee en cada elemnto de una fila 
#los colores con los que el nodo esta conectado -> "colores"
    colors = np.zeros((noColor.shape[0], entry.shape[0]))
    af = -1
    for k1 in range(noColor.shape[0]):
        for k2 in range(entry.shape[0]):
            if (entry[noColor[k1],k2] == 1):
                colors[k1,k2] = entry[k2,k2]
        med_list = []
        for num in colors[k1,:]:
            if (num not in med_list) and (num != 0) :
                med_list.append(num)
        a = len(med_list)
        b = noColor[k1]
        if a > af:
            af = a
            bf = b
            final_list = list(map(int, med_list))
    
    return (final_list,af,bf)
