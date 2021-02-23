import numpy as np


def cindysfav(current, currentposition, electrodeposition):
    sig = 3.333*(10**-7) #S/um
    Vo = []
    l = len(current)
    #Loop across entire neuron (along x)
    for i in range(l):
        #Calculate radius (in microns) for a given location
        radius = np.sqrt((float(currentposition[i][0]) - float(electrodeposition[0]))**2
                         + (float(currentposition[i][1]) - float(electrodeposition[1]))**2
                         + (float(currentposition[i][2]) - float(electrodeposition[2]))**2)
        #Calculate voltages across all time for a given location
        V_temp = [float(current_t) / (4*np.pi*sig*radius) for current_t in current[i]]
        Vo.append(V_temp)
    #Returns a vector of the voltage over time, in Volts
    return Vo