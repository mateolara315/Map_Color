import numpy as np
def colors(vec):
    colors = np.empty((0,3))
    for i in range(np.amax(vec)):
        tmp = (np.random.rand(1,3))
        colors = np.append(colors,tmp,axis = 0)

    vec = np.asarray(vec)-1
    a = [colors[i,:] for i in vec]
    return np.asarray(a)
