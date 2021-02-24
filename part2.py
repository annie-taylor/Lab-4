from functions import *
import matplotlib.pyplot as plt
import pickle as p
import numpy as np


#1.1 again, loading data
currents_big, XYZ_big, currents_small, XYZ_small = loaddata()

# --------------- Part 2
#2.1 Randomly place 10 neurons in a 100um cube
XYZ = randplacement(XYZ_big)
bursts = randbursts(currents_big)

p_electrode2 = [0, 0, 0]
first = False #Only reload voltage arrays if necessary -> time intensive
if first:
    savevoltages(bursts,XYZ,p_electrode2,False)
    savesup(False)

sup1 = p.load(open('sup1.p', 'rb'))
sup2 = p.load(open('sup2.p', 'rb'))
sup3 = p.load(open('sup3.p', 'rb'))
sup4 = p.load(open('sup4.p', 'rb'))
sup5 = p.load(open('sup5.p', 'rb'))
sup6 = p.load(open('sup6.p', 'rb'))
sup7 = p.load(open('sup7.p', 'rb'))
sup8 = p.load(open('sup8.p', 'rb'))
sup9 = p.load(open('sup9.p', 'rb'))
sup10 = p.load(open('sup10.p', 'rb'))

bigsup = np.add(np.add(np.add(np.add(np.add(np.add(np.add(np.add(np.add(sup1,sup2),sup3),sup4),sup5),sup6),sup7),sup8),sup9),sup10)

#Build time vector for reference (steps in 0.025ms)
time = [0]
for i in range(len(sup1)-1):
    time.append(time[i] + 0.025)

plt.plot(time,sup1,label='Neuron 1')
plt.plot(time,sup2,label='Neuron 2')
plt.plot(time,sup3,label='Neuron 3')
plt.plot(time,sup4,label='Neuron 4')
plt.plot(time,sup5,label='Neuron 5')
plt.plot(time,sup6,label='Neuron 6')
plt.plot(time,sup7,label='Neuron 7')
plt.plot(time,sup8,label='Neuron 8')
plt.plot(time,sup9,label='Neuron 9')
plt.plot(time,sup10,label='Neuron 10')

plt.figure(figsize=(15,5))
plt.title('Voltages Separated by Neuron')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.savefig('all10.png')
#plt.show()
plt.clf()

plt.figure(figsize=(15,5))
plt.plot(time,bigsup,label='Superposition')
plt.title('Superposition of Voltages from All Neurons')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
#plt.legend()
plt.savefig('super10.png')
#plt.show()
plt.clf()

beta = 1 #Pink noise is beta=1
samples = len(time)
cn = colorednoise.powerlaw_psd_gaussian(beta,samples)*(0.5*(10**-5)) #Scale by 10uV pk-pk

plt.plot(time,cn)
plt.title('Test Colored Noise')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
#plt.legend()
plt.savefig('testnoise.png')
#plt.show()
plt.clf()

plt.figure(figsize=(15,5))
plt.plot(time,np.add(cn,bigsup))
plt.title('Noise with Cumulative Signal')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
#plt.legend()
plt.savefig('realoutput.png')
#plt.show()
plt.clf()

#Add dead zone
p_electrode2 = [0, 0, 0]
l = len(bursts)
a = bursts[0]
#XYZ = np.transpose(XYZ)
b = XYZ[0]
for i in range(l):
    bursts[i] = deadzone(bursts[i],XYZ[i],p_electrode2)

first = False #Only reload voltage arrays if necessary -> time intensive
if first:
    #Argument true means dead zone
    savevoltages(bursts,XYZ,p_electrode2,True)
    savesup(True)

sup1_dz = p.load(open('sup1_dz.p', 'rb'))
sup2_dz = p.load(open('sup2_dz.p', 'rb'))
sup3_dz = p.load(open('sup3_dz.p', 'rb'))
sup4_dz = p.load(open('sup4_dz.p', 'rb'))
sup5_dz = p.load(open('sup5_dz.p', 'rb'))
sup6_dz = p.load(open('sup6_dz.p', 'rb'))
sup7_dz = p.load(open('sup7_dz.p', 'rb'))
sup8_dz = p.load(open('sup8_dz.p', 'rb'))
sup9_dz = p.load(open('sup9_dz.p', 'rb'))
sup10_dz = p.load(open('sup10_dz.p', 'rb'))

bigsup_dz = np.add(np.add(np.add(np.add(np.add(np.add(np.add(np.add(np.add(sup1_dz,sup2_dz),sup3_dz),sup4_dz),sup5_dz),sup6_dz),sup7_dz),sup8_dz),sup9_dz),sup10_dz)

#Build time vector for reference (steps in 0.025ms)
time = [0]
for i in range(len(sup1)-1):
    time.append(time[i] + 0.025)

plt.plot(time,sup1_dz,label='Neuron 1')
plt.plot(time,sup2_dz,label='Neuron 2')
plt.plot(time,sup3_dz,label='Neuron 3')
plt.plot(time,sup4_dz,label='Neuron 4')
plt.plot(time,sup5_dz,label='Neuron 5')
plt.plot(time,sup6_dz,label='Neuron 6')
plt.plot(time,sup7_dz,label='Neuron 7')
plt.plot(time,sup8_dz,label='Neuron 8')
plt.plot(time,sup9_dz,label='Neuron 9')
plt.plot(time,sup10_dz,label='Neuron 10')

plt.figure(figsize=(15,5))
plt.title('Voltages Separated by Neuron (inc. dead zone)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.savefig('all10_dz.png')
#plt.show()
plt.clf()

plt.figure(figsize=(15,5))
plt.plot(time,bigsup_dz,label='Superposition')
plt.title('Superposition of Voltages from All Neurons (inc. dead zone)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
#plt.legend()
plt.savefig('super10_dz.png')
#plt.show()
plt.clf()

beta = 1 #Pink noise is beta=1
samples = len(time)
cn = colorednoise.powerlaw_psd_gaussian(beta,samples)*(0.5*(10**-5)) #Scale by 10uV pk-pk

plt.figure(figsize=(15,5))
plt.plot(time,np.add(cn,bigsup_dz))
plt.title('Noise with Cumulative Signal (inc. dead zone)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
#plt.legend()
plt.savefig('realoutput_dz.png')
#plt.show()
plt.clf()

f, (ax1, ax2) = plt.subplots(2, 1, sharey=True)
ax1.plot(time,np.add(cn,bigsup_dz),label='With Dead Zone')
ax2.plot(time,np.add(cn,bigsup),label='Without Dead Zone')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
ax1.legend()
ax2.legend()
plt.savefig('realoutput_subplots.png')
#plt.show()
plt.clf()