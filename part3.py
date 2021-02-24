from functions import *
import os
import csv
import numpy as np
import matplotlib.pyplot as plt


#1.1
currents_big, XYZ_big, currents_small, XYZ_small = loaddata()
cwd = os.getcwd()
#Load big currents from CSV
comsol = csv.reader(open(cwd+'/functions/data/headvoltage.csv', 'rt'), delimiter=',')
comsol_out = np.transpose(np.array(list(comsol)))
X = comsol_out[0]
Y = comsol_out[1]
Z = comsol_out[2]
V = comsol_out[3]

K = V/1000000 #Need to reconcile units, what is COMSOL's output? Assume microvolt


