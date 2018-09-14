from inArray import inArray
from busqueda import search
from draw import drawColor
from map_color import colors
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
sw = int(input('1: Ingresar Matriz Manualmente \n0: Cargar Matriz de un Archivo \nSw = '))
if sw == 1:
    print('Digitar la matriz de adyacencia\n')
    adjMat = inArray()
elif sw == 0:
    name = str(input('Digite el nombre del archivo: '))
    adjMat = np.genfromtxt(name,delimiter="\t", skip_header=1, filling_values=1,dtype = str)
    labels = adjMat[:,0]
    adjMat = np.delete(adjMat, 0, axis=1)
    adjMat = adjMat.astype(int)
    print('\nLa matriz digitada fue: \n', adjMat)
else:
    print('ERROR')
    quit()
adjMat[0,0] = 1
adjMat[1,1] = 2
numColor = 2
print("\nIntroducción: El algoritmo recibe la matriz de adyacencia, de forma que sabe como se encuentran\
\nconectados todos los nodos y asigna dos colores diferentes a los dos primeros nodos, dígase 'A' y 'B',\
\nde esta forma se mira cual de los nodos sin color asignado es el más conectado (él más restringido) y\
\nse determina cual debe ser su color basado en las restricciones, este proceso se repite para cada nodo\
\nsin colorear hasta que se logra completar el árbol de forma optima. A continuación se ven las agnaciones\
\nde colores en cada iteración (0 representa color aún no asignado y los números enteros mayores que 0\
\nrepresentan cada uno de los colores)")
while True:
    if np.count_nonzero(np.diagonal(adjMat).copy()) == len(np.diagonal(adjMat).copy()):
        print("\nColores asignados finales: \n", show.T)
        break
    [final_list, nodeWeight, numNode] = search(adjMat)
    [numColor,adjMat] = drawColor(adjMat,numNode, nodeWeight,numColor,final_list)

    if sw == 0:
        show = np.zeros((2, len(np.diagonal(adjMat).astype(str)))).astype(str)
        show[0, :] = labels
        show[1, :] = np.diagonal(adjMat).astype(str)
        print("\nColores asignados hasta ahora: \n", show.T)



rows, cols = np.where(adjMat == 1)
edges = zip(rows.tolist(), cols.tolist())
gr = nx.Graph()
gr.add_edges_from(edges)
a = colors(show[1,:].astype(int)) # random colors assigned

temp={}
for i in range(len(labels)):
    temp[i] = labels[i]

nx.draw(gr, node_sizes = 5, labels =temp ,with_labels= True, node_color = a[gr.nodes()])


plt.show()