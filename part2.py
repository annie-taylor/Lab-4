from functions import *
import matplotlib.pyplot as plt

#1.1 again, loading data
currents_big, XYZ_big, currents_small, XYZ_small = loaddata()
#Build time vector for reference (steps in 0.025ms)
time = [0]
for i in range(len(currents_big[0])-1):
    time.append(time[i] + 0.025)

# --------------- Part 2
#2.1 Randomly place 10 neurons in a 100um cube
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



