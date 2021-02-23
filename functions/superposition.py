import numpy as np


def superposition(Vo):
    l, t = np.shape(Vo)
    sup = []
    #Loop through all time steps
    for i in range(t):
        runsum = 0
        #Add up voltages across all locations
        for j in range(l):
            runsum += Vo[j][i]
        sup.append(runsum)
    return sup