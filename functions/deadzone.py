import numpy as np


def deadzone(current,XYZ,electrodep):
    distances = []
    # Loop across entire neuron (along x)
    l = len(current)
    print(np.shape(XYZ))
    print(np.shape(electrodep))
    for i in range(l):
        # Calculate radius (in microns) for a given location
        radius = np.sqrt((float(XYZ[i][0]) - float(electrodep[0])) ** 2
                         + (float(XYZ[i][1]) - float(electrodep[1])) ** 2
                         + (float(XYZ[i][2]) - float(electrodep[2])) ** 2)
        if radius <= 50:
            #If within 50um radius of electrode, force currents to zero
            current[i] = 0
    return current