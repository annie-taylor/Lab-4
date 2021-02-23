import numpy as np
import random
import pickle as p

def randbursts(currents_big):
    burst = currents_big
    burst1 = burst
    for i in range(56):
        # Action potentials do not overlap
        burst1 = np.concatenate((burst1, burst), axis=1)  # Concatenate waveforms to be ~1 sec burst
    # Make sure action potentials from different neurons do not happen at the exact same time
    starts = []
    for i in range(10):
        starts.append(int(random.random()*4000))
    burst2 = np.roll(burst1, starts[0], axis=1)  # pushes entire burst forward by a random value between 0 and 50ms
    burst3 = np.roll(burst1, starts[1], axis=1)  # pushes entire burst forward by a random value between 0 and 50ms
    burst4 = np.roll(burst1, starts[2], axis=1)  # pushes entire burst forward by a random value between 0 and 50ms
    burst5 = np.roll(burst1, starts[3], axis=1)  # pushes entire burst forward by a random value between 0 and 50ms
    burst6 = np.roll(burst1, starts[4], axis=1)  # pushes entire burst forward by a random value between 0 and 50ms
    burst7 = np.roll(burst1, starts[5], axis=1)  # pushes entire burst forward by a random value between 0 and 50ms
    burst8 = np.roll(burst1, starts[6], axis=1)  # pushes entire burst forward by a random value between 0 and 50ms
    burst9 = np.roll(burst1, starts[7], axis=1)  # pushes entire burst forward by a random value between 0 and 50ms
    burst10 = np.roll(burst1, starts[8], axis=1)  # pushes entire burst forward by a random value between 0 and 50ms
    bursts = [burst1, burst2, burst3, burst4, burst5, burst6, burst7, burst8, burst9, burst10]
    return bursts
