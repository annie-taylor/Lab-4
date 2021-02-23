from functions import *
import matplotlib.pyplot as plt


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
