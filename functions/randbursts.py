import numpy as np

def randbursts(currents_big):
    burst = currents_big
    burst1 = burst
    for i in range(56):
        # Action potentials do not overlap
        burst1 = np.concatenate((burst1, burst), axis=1)  # Concatenate waveforms to be ~1 sec burst

    # Make sure action potentials from different neurons do not happen at the exact same time
    burst2 = np.roll(burst1, 100, axis=1)  # pushes entire burst forward by 1.25ms
    burst3 = np.roll(burst2, 100, axis=1)  # pushes entire burst forward by 1.25ms
    burst4 = np.roll(burst3, 100, axis=1)  # pushes entire burst forward by 1.25ms
    burst5 = np.roll(burst4, 100, axis=1)  # pushes entire burst forward by 1.25ms
    burst6 = np.roll(burst5, 100, axis=1)  # pushes entire burst forward by 1.25ms
    burst7 = np.roll(burst6, 100, axis=1)  # pushes entire burst forward by 1.25ms
    burst8 = np.roll(burst7, 100, axis=1)  # pushes entire burst forward by 1.25ms
    burst9 = np.roll(burst8, 100, axis=1)  # pushes entire burst forward by 1.25ms
    burst10 = np.roll(burst9, 100, axis=1)  # pushes entire burst forward by 1.25ms
    return burst1, burst2, burst3, burst4, burst5, burst6, burst7, burst8, burst9, burst10