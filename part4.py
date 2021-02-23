import numpy as np
from neuron import h, rxd
from neuron.units import ms, mV
import matplotlib.pyplot as plt

#Setup: construct model neuron (Lab 2, Part 2)

#Two axons: both 5mm long with 1000 compartments, one with diameter 10um, one with 20um
Rm = 40000 #ohm*cm^2
Ra = 200 #ohm*cm
d2 = 20 #20um = 0.002cm
r2 = 0.002/2
n2 = h.Section(name='n2')
n2.nseg = 1000
n2.L = 5000
n2.diam = d2
n2.Ra = Ra
n2.insert('hh')

stims = np.linspace(1,100,5)
currents = []

#Loop through stimulation currents to estimate threshold current
for amp in stims:
    iclamp2 = h.IClamp(n2(0)) #Puts current clamp at beginning of neuron
    iclamp2.delay = 10 # Time stim starts (ms)
    iclamp2.dur = 1 # Length of stim (ms)
    iclamp2.amp = amp # Magnitude of stim (nA)

    c = h.Vector().record(n2(0.5)._ref_i_membrane) #Record membrane current midway along axon
    t = h.Vector().record(h._ref_t) #Record time stamps
    h.load_file('stdrun.hoc') #Load library to run simulation
    h.finitialize(-65*mV) #Initialize with r_pot of -65 mV
    h.continuerun(40*ms) #Set duration of simulation to 40 ms
    currents.append(c)

plt.figure()
plt.plot(t,currents)
plt.xlabel('t (ms)')
plt.ylabel('V (mV)')
plt.legend()
plt.savefig('diameter.png')
plt.show()