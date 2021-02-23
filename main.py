from functions import *
import matplotlib.pyplot as plt
import numpy as np


#1.1
currents_big, XYZ_big, currents_small, XYZ_small = loaddata()
#Build time vector for reference (steps in 0.025ms)
time = [0]
for i in range(len(currents_big[0])-1):
    time.append(time[i] + 0.025)

#1.2
p_electrode = [0,50,0] # 50um displaced in y-axis from axon hillock

#1.3 and 1.7
Vo_big = cindysfav(currents_big,XYZ_big,p_electrode)
Vo_small = cindysfav(currents_small,XYZ_small,p_electrode)
plt.plot(time,Vo_big[0],label='Big Currents')
plt.plot(time,Vo_small[0],label='Small Currents')
plt.title('Voltage Reading at 50um from origin (y-axis)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.savefig('Part3.png')
plt.clf()

#1.4 and 1.7
sup_big = superposition(Vo_big)
sup_small = superposition(Vo_small)
plt.plot(time,sup_big,label='Big Currents')
plt.plot(time,sup_small,label='Small Currents')
plt.title('Superposition across all locations')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.savefig('Part4.png')
plt.clf()

#1.5 and 1.7
p_electrode = [0,100,0]
Vo_big1 = superposition(cindysfav(currents_big,XYZ_big,p_electrode))
Vo_small1 = superposition(cindysfav(currents_small,XYZ_small,p_electrode))
p_electrode = [0,200,0]
Vo_big2 = superposition(cindysfav(currents_big,XYZ_big,p_electrode))
Vo_small2 = superposition(cindysfav(currents_small,XYZ_small,p_electrode))
p_electrode = [0,300,0]
Vo_big3 = superposition(cindysfav(currents_big,XYZ_big,p_electrode))
Vo_small3 = superposition(cindysfav(currents_small,XYZ_small,p_electrode))

plt.plot(time,sup_big,label='50um')
plt.plot(time,Vo_big1,label='100um')
plt.plot(time,Vo_big2,label='200um')
plt.plot(time,Vo_big3,label='300um')
plt.axhline(y=(.5)*10**-5, color='black', linestyle='--')
plt.axhline(y=-(.5)*10**-5, color='black', linestyle='--')
plt.title('Voltage Readings at Varying Electrode Locations (Big Currents)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.savefig('Part5_big.png')
plt.clf()

plt.plot(time,sup_small,label='50um')
plt.plot(time,Vo_small1,label='100um')
plt.plot(time,Vo_small2,label='200um')
plt.plot(time,Vo_small3,label='300um')
plt.axhline(y=(.5)*10**-5, color='black', linestyle='--')
plt.axhline(y=-(.5)*10**-5, color='black', linestyle='--')
plt.title('Voltage Readings at Varying Electrode Locations (Small Currents)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.savefig('Part5_small.png')
plt.clf()

#1.6
floor = (.5)*(10**-5) #10uV pk-pk
verbose = False # Suppress print statements unless need to rerun this part
if verbose:
    print('Detectable at 50um, big currents: %r'% detectable(floor,sup_big))
    print('Detectable at 50um, small currents: %r'%detectable(floor,sup_small))
    print('Detectable at 100um, big currents: %r'%detectable(floor,Vo_big1))
    print('Detectable at 100um, small currents: %r'%detectable(floor,Vo_small1))
    print('Detectable at 200um, big currents: %r'%detectable(floor,Vo_big2))
    print('Detectable at 200um, small currents: %r'%detectable(floor,Vo_small2))
    print('Detectable at 300um, big currents: %r'%detectable(floor,Vo_big3))
    print('Detectable at 300um, small currents: %r'%detectable(floor,Vo_small3))

# --------------- Part 2
#2.1

#Randomly place 10 neurons in a 100um cube
XYZ1, XYZ2, XYZ3, XYZ4, XYZ5, XYZ6, XYZ7, XYZ8, XYZ9, XYZ10 = randplacement(XYZ_big)
burst1, burst2, burst3, burst4, burst5, burst6, burst7, burst8, burst9, burst10 = randbursts(currents_big)

p_electrode2 = [0, 50, 0]
V1 = cindysfav(burst1,XYZ1,p_electrode2)
V2 = cindysfav(burst2,XYZ2,p_electrode2)
V3 = cindysfav(burst3,XYZ3,p_electrode2)
V4 = cindysfav(burst4,XYZ4,p_electrode2)
V5 = cindysfav(burst5,XYZ5,p_electrode2)
V6 = cindysfav(burst6,XYZ6,p_electrode2)
V7 = cindysfav(burst7,XYZ7,p_electrode2)
V8 = cindysfav(burst8,XYZ8,p_electrode2)
V9 = cindysfav(burst9,XYZ9,p_electrode2)
V10 = cindysfav(burst10,XYZ10,p_electrode2)

sup1 = superposition(V1)
sup2 = superposition(V2)
sup3 = superposition(V3)
sup4 = superposition(V4)
sup5 = superposition(V5)
sup6 = superposition(V6)
sup7 = superposition(V7)
sup8 = superposition(V8)
sup9 = superposition(V9)
sup10 = superposition(V10)

bigsup = sup1 + sup2 + sup3 + sup4 + sup5 + sup6 + sup7 + sup8 + sup9 + sup10

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

plt.axhline(y=(.5)*10**-5, color='black', linestyle='--')
plt.axhline(y=-(.5)*10**-5, color='black', linestyle='--')
plt.title('Eek!')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
#plt.savefig('Part5_big.png')
plt.show()



