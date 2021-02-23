import numpy as np


def detectable(floor,V):
    max = np.amax(V)
    min = np.amin(V)
    if abs(min) > max:
        max = abs(min)
    if max > floor:
        return True
    else:
        return False